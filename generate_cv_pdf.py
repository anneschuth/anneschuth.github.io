#!/usr/bin/env python3
"""Render the Jekyll-built /cv/ page to assets/cv-anne-schuth.pdf via WeasyPrint."""
from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SITE = ROOT / "_site"
CV_HTML = SITE / "cv" / "index.html"
PRINT_CSS = SITE / "assets" / "css" / "cv-print.css"
OUTPUT_PDF = ROOT / "assets" / "cv-anne-schuth.pdf"


def run_jekyll_build() -> None:
    if not shutil.which("bundle"):
        sys.exit("error: 'bundle' not found on PATH; install Ruby + Bundler first")
    print("==> bundle exec jekyll build", flush=True)
    subprocess.run(
        ["bundle", "exec", "jekyll", "build", "--trace"],
        cwd=ROOT,
        check=True,
    )


def render_pdf() -> None:
    if not CV_HTML.exists():
        sys.exit(f"error: {CV_HTML} not found; did Jekyll build succeed?")
    if not PRINT_CSS.exists():
        sys.exit(f"error: {PRINT_CSS} not found; expected Jekyll to compile cv-print.scss")

    # WeasyPrint is imported lazily so `--help` and `--no-build` work without it.
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
