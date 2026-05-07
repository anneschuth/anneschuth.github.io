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
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SITE = ROOT / "_site"
CV_HTML = SITE / "cv" / "index.html"
PRINT_CSS = SITE / "assets" / "css" / "cv-print.css"
OUTPUT_PDF = ROOT / "assets" / "cv-anne-schuth.pdf"

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


def render_pdf() -> None:
    if not CV_HTML.exists():
        sys.exit(f"error: {CV_HTML} not found; did Jekyll build succeed?")
    if not PRINT_CSS.exists():
        sys.exit(f"error: {PRINT_CSS} not found; expected Jekyll to compile cv-print.scss")

    ensure_source_date_epoch()

    # WeasyPrint is imported lazily so `--help` works without it.
    from weasyprint import CSS, HTML  # type: ignore

    print(f"==> rendering {CV_HTML} -> {OUTPUT_PDF}", flush=True)
    OUTPUT_PDF.parent.mkdir(parents=True, exist_ok=True)
    HTML(filename=str(CV_HTML), base_url=str(SITE)).write_pdf(
        target=str(OUTPUT_PDF),
        stylesheets=[CSS(filename=str(PRINT_CSS))],
    )
    size_kb = OUTPUT_PDF.stat().st_size / 1024
    print(f"==> wrote {OUTPUT_PDF} ({size_kb:.1f} KB)", flush=True)


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


if __name__ == "__main__":
    main()
