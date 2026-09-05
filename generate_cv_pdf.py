#!/usr/bin/env python3
"""Render the Jekyll-built /cv/ page to a PDF and a PNG thumbnail via WeasyPrint.

The PDF is a build artifact, not a source file, and is never committed:

  - .github/workflows/deploy.yml renders it straight into _site/assets/ so it
    ships with every deployment of the site;
  - .github/workflows/ci.yml renders it on every pull request as a smoke test
    and uploads the result as an artifact;
  - `just cv` renders it into assets/ (gitignored) for a local preview.

See CLAUDE.md, "CV PDF: a build artifact, never a committed file".

The output is byte-deterministic: SOURCE_DATE_EPOCH is set to the timestamp of
the last git commit that touches CV inputs (overridable via the env var), so
two builds of the same commit produce identical PDFs.
"""
from __future__ import annotations

import argparse
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SITE = ROOT / "_site"
CV_HTML = SITE / "cv" / "index.html"
PRINT_CSS = SITE / "assets" / "css" / "cv-print.css"
SITE_URL = "https://anneschuth.nl"  # for rewriting root-relative links in the PDF
DEFAULT_OUTPUT_DIR = "assets"  # local preview target; gitignored
PDF_NAME = "cv-anne-schuth.pdf"  # linked from cv.markdown and about.markdown
THUMB_NAME = "cv-thumbnail.png"  # linked from about.markdown
THUMB_WIDTH = 600  # px; the about page displays it small, this keeps it crisp on retina

# Inputs whose timestamps determine SOURCE_DATE_EPOCH when unset.
CV_INPUTS = [
    "cv.markdown",
    "_publications",
    "_talks",
    "_students",
    "_includes/cv",
    "activities.markdown",
    "assets/css/cv-print.scss",
    "_data/scholar_stats.yml",
]


def run_jekyll_build() -> None:
    if not shutil.which("bundle"):
        sys.exit("error: 'bundle' not found on PATH; install Ruby + Bundler first")
    print("==> bundle exec jekyll build", flush=True)
    subprocess.run(
        ["bundle", "exec", "jekyll", "build", "--trace"],
        cwd=ROOT,
        check=True,
    )


def ensure_source_date_epoch() -> None:
    """Pin SOURCE_DATE_EPOCH for reproducible PDFs.

    WeasyPrint uses this env var to set /CreationDate and /ModDate in the PDF;
    without it every run produces a different file, which makes two builds of
    the same commit impossible to compare.
    """
    if os.environ.get("SOURCE_DATE_EPOCH"):
        return
    try:
        result = subprocess.run(
            ["git", "log", "-1", "--format=%ct", "--", *CV_INPUTS],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        )
        ts = result.stdout.strip()
        if ts:
            os.environ["SOURCE_DATE_EPOCH"] = ts
            print(f"==> SOURCE_DATE_EPOCH={ts} (from git log of CV inputs)", flush=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        # Not in a git repo, or git missing: fall back to a fixed epoch so
        # the output is still deterministic across runs.
        os.environ["SOURCE_DATE_EPOCH"] = "1700000000"
        print("==> SOURCE_DATE_EPOCH=1700000000 (fallback)", flush=True)


def ensure_fontconfig() -> None:
    """Point fontconfig at the bundled Latin Modern fonts.

    WeasyPrint resolves font families through fontconfig, not the stylesheet's
    @font-face url(). Latin Modern is not installed on the GitHub runner (and
    may not be on a given Mac either), so we write a minimal fontconfig file
    that adds assets/fonts/ as a font directory and export FONTCONFIG_FILE.
    This makes "Latin Modern Roman"/"Latin Modern Sans" resolvable identically
    everywhere, with no system font install.
    """
    fonts_dir = ROOT / "assets" / "fonts"
    if not any(fonts_dir.glob("*.otf")):
        sys.exit(f"error: no .otf files in {fonts_dir}; cannot set up Latin Modern")
    cache_dir = ROOT / ".fontconfig-cache"
    cache_dir.mkdir(exist_ok=True)
    conf = ROOT / ".fonts.conf"
    conf.write_text(
        '<?xml version="1.0"?>\n'
        '<!DOCTYPE fontconfig SYSTEM "fonts.dtd">\n'
        "<fontconfig>\n"
        f"  <dir>{fonts_dir}</dir>\n"
        "  <dir>/System/Library/Fonts</dir>\n"
        "  <dir>/Library/Fonts</dir>\n"
        "  <dir>/usr/share/fonts</dir>\n"
        f"  <cachedir>{cache_dir}</cachedir>\n"
        "</fontconfig>\n",
        encoding="utf-8",
    )
    os.environ["FONTCONFIG_FILE"] = str(conf)
    print(f"==> FONTCONFIG_FILE={conf} (Latin Modern from {fonts_dir})", flush=True)


def render_pdf(output_pdf: Path) -> None:
    if not CV_HTML.exists():
        sys.exit(f"error: {CV_HTML} not found; did Jekyll build succeed?")
    if not PRINT_CSS.exists():
        sys.exit(f"error: {PRINT_CSS} not found; expected Jekyll to compile cv-print.scss")

    ensure_fontconfig()
    ensure_source_date_epoch()

    # WeasyPrint is imported lazily so `--help` works without it.
    from weasyprint import CSS, HTML  # type: ignore

    print(f"==> rendering {CV_HTML} -> {output_pdf}", flush=True)
    output_pdf.parent.mkdir(parents=True, exist_ok=True)

    # Internal links in the CV are root-relative (href="/projects/"). On the
    # live site that is correct, but in a standalone PDF WeasyPrint resolves
    # them against base_url, i.e. to a file:// path on the build machine, so
    # they are dead for anyone who opens the downloaded PDF. Rewrite them to
    # absolute production URLs. Local build assets (the bundled fonts and the
    # compiled stylesheet under /assets/) must stay relative so WeasyPrint can
    # still read them off disk, so those prefixes are left untouched.
    html = CV_HTML.read_text(encoding="utf-8")
    html = re.sub(
        r'(href|src)="/(?!/|assets/)',
        rf'\1="{SITE_URL}/',
        html,
    )

    HTML(string=html, base_url=str(SITE)).write_pdf(
        target=str(output_pdf),
        stylesheets=[CSS(filename=str(PRINT_CSS))],
    )
    size_kb = output_pdf.stat().st_size / 1024
    print(f"==> wrote {output_pdf} ({size_kb:.1f} KB)", flush=True)


def render_thumbnail(output_pdf: Path, output_thumb: Path) -> None:
    """Rasterize page 1 of the PDF to a PNG.

    The about page links this image to the full PDF; rendering both in the
    same run keeps the preview in sync with the CV.
    """
    if not output_pdf.exists():
        sys.exit(f"error: {output_pdf} not found; cannot render thumbnail")

    import pypdfium2 as pdfium  # type: ignore

    pdf = pdfium.PdfDocument(str(output_pdf))
    page = pdf[0]
    scale = THUMB_WIDTH / page.get_size()[0]
    image = page.render(scale=scale).to_pil().convert("RGB")
    image.save(str(output_thumb), optimize=True)
    page.close()
    pdf.close()
    size_kb = output_thumb.stat().st_size / 1024
    print(
        f"==> wrote {output_thumb} ({image.width}x{image.height}, {size_kb:.1f} KB)",
        flush=True,
    )


def main() -> None:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        "--no-build",
        action="store_true",
        help="skip jekyll build; assume _site/ is already up to date",
    )
    parser.add_argument(
        "--output-dir",
        default=DEFAULT_OUTPUT_DIR,
        help=(
            f"directory to write {PDF_NAME} and {THUMB_NAME} to, relative to the repo "
            "root (default: %(default)s; deploy.yml uses _site/assets)"
        ),
    )
    args = parser.parse_args()

    output_dir = Path(args.output_dir)
    if not output_dir.is_absolute():
        output_dir = ROOT / output_dir

    if not args.no_build:
        run_jekyll_build()
    render_pdf(output_dir / PDF_NAME)
    render_thumbnail(output_dir / PDF_NAME, output_dir / THUMB_NAME)


if __name__ == "__main__":
    main()
