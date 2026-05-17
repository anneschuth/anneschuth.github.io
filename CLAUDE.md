# Working on this project

## Always branch and PR

Every change to this repo goes on a feature branch and lands via a pull
request. Never commit directly to `main`, even for a one-line fix. The flow is:
create a branch, make the change, push, open a PR with `gh pr create`. Do this
without being asked each time.

## CV PDF generation

`just cv` regenerates `assets/cv-anne-schuth.pdf` and the thumbnail from
`/cv/`. On macOS, WeasyPrint needs the Homebrew pango/gobject libraries on the
dyld path, so run it as:

```bash
DYLD_FALLBACK_LIBRARY_PATH=/opt/homebrew/lib uv run python generate_cv_pdf.py
```

Source of truth is `cv.markdown` plus the includes under `_includes/cv/`.
Print styling lives in `assets/css/cv-print.scss` (WeasyPrint loads it
directly, not via Jekyll). In the rendered CV, the organization is a sans-serif
accent-blue `h4`; the role is a serif bold run in the entry paragraph just
below it. Keep that contrast intact when touching the print stylesheet.
