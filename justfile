# Task runner for anneschuth.nl. Run `just` to list recipes.

# One-time setup: Ruby gems + Python env
setup:
    bundle install
    uv sync

# Serve the site locally with live reload
serve:
    bundle exec jekyll serve

# Build the site once
build:
    bundle exec jekyll build --trace

# Run all pre-commit checks (same as CI)
check:
    uv run pre-commit run --all-files

# Regenerate the CV PDF and thumbnail
cv:
    #!/usr/bin/env bash
    set -euo pipefail
    # WeasyPrint needs pango/gobject on the dyld path. On macOS those live
    # under the Homebrew prefix and are not searched by default; on Linux/CI
    # they sit in standard paths, so this is a no-op there.
    if [[ "$OSTYPE" == darwin* ]] && command -v brew >/dev/null 2>&1; then
        export DYLD_FALLBACK_LIBRARY_PATH="$(brew --prefix)/lib${DYLD_FALLBACK_LIBRARY_PATH:+:$DYLD_FALLBACK_LIBRARY_PATH}"
    fi
    uv run python generate_cv_pdf.py

# Sync citation counts from Google Scholar
scholar:
    uv run pre-commit run --hook-stage manual update-citations

# Regenerate the Wardley map image
wardley:
    uv run python wardley_map.py
