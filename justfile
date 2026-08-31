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

# Render the CV PDF and thumbnail into assets/ for a local preview. Both files
# are gitignored; the ones on the live site are built by .github/workflows/deploy.yml.
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

# Sync citation counts from Google Scholar. Local only: Google answers GitHub
# runners with HTTP 403. Review the diff, then open a PR. Pass --citations-only
# to skip the PDF hunt and the creation of missing entries.
scholar *ARGS:
    uv run python fetch_scholar_data.py {{ARGS}}

# Regenerate the Wardley map image
wardley:
    uv run python wardley_map.py
