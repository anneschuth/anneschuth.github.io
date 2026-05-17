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
    uv run python generate_cv_pdf.py

# Sync citation counts from Google Scholar
scholar:
    uv run pre-commit run --hook-stage manual update-citations

# Regenerate the Wardley map image
wardley:
    uv run python wardley_map.py
