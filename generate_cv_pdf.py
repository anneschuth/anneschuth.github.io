#!/usr/bin/env python3
"""Render the Jekyll-built /cv/ page to assets/cv-anne-schuth.pdf via WeasyPrint.

The output is byte-deterministic: SOURCE_DATE_EPOCH is set to the timestamp of
the last git commit that touches CV inputs (overridable via the env var) so two
identical builds produce identical PDFs and the workflow only commits the PDF
back when the content actually changed.
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
OUTPUT_PDF = ROOT / "assets" / "cv-anne-schuth.pdf"
OUTPUT_THUMB = ROOT / "assets" / "cv-thumbnail.png"
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
    without it, every run produces a different file and the auto-commit
    workflow would commit on every push.
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
        # Not in a git repo, or git missing — fall back to a fixed epoch so
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


def render_pdf() -> None:
    if not CV_HTML.exists():
        sys.exit(f"error: {CV_HTML} not found; did Jekyll build succeed?")
    if not PRINT_CSS.exists():
        sys.exit(f"error: {PRINT_CSS} not found; expected Jekyll to compile cv-print.scss")

    ensure_fontconfig()
    ensure_source_date_epoch()

    # WeasyPrint is imported lazily so `--help` works without it.
    from weasyprint import CSS, HTML  # type: ignore

    print(f"==> rendering {CV_HTML} -> {OUTPUT_PDF}", flush=True)
    OUTPUT_PDF.parent.mkdir(parents=True, exist_ok=True)

    # Internal links in the CV are root-relative (href="/software/"). On the
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
        target=str(OUTPUT_PDF),
        stylesheets=[CSS(filename=str(PRINT_CSS))],
    )
    size_kb = OUTPUT_PDF.stat().st_size / 1024
    print(f"==> wrote {OUTPUT_PDF} ({size_kb:.1f} KB)", flush=True)


def render_thumbnail() -> None:
    """Rasterize page 1 of the PDF to assets/cv-thumbnail.png.

    The about page links this image to the full PDF; regenerating it here keeps
    the preview in sync with the CV instead of drifting like the old static one.
    """
    if not OUTPUT_PDF.exists():
        sys.exit(f"error: {OUTPUT_PDF} not found; cannot render thumbnail")

    import pypdfium2 as pdfium  # type: ignore

    pdf = pdfium.PdfDocument(str(OUTPUT_PDF))
    page = pdf[0]
    scale = THUMB_WIDTH / page.get_size()[0]
    image = page.render(scale=scale).to_pil().convert("RGB")
    image.save(str(OUTPUT_THUMB), optimize=True)
    page.close()
    pdf.close()
    size_kb = OUTPUT_THUMB.stat().st_size / 1024
    print(
        f"==> wrote {OUTPUT_THUMB} ({image.width}x{image.height}, {size_kb:.1f} KB)",
        flush=True,
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--no-build",
        action="store_true",
        help="skip jekyll build; assume _site/ is already up to date",
    )
    args = parser.parse_args()

    if not args.no_build:
        run_jekyll_build()
    render_pdf()
    render_thumbnail()


if __name__ == "__main__":
    main()
