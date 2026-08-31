# Working on this project

## Always branch and PR

Every change to this repo goes on a feature branch and lands via a pull
request. Never commit directly to `main`, even for a one-line fix. The flow is:
create a branch, make the change, push, open a PR with `gh pr create`. Do this
without being asked each time.

## Deployment: GitHub Actions builds and deploys the site

GitHub Pages is configured to deploy from GitHub Actions, not from the `main`
branch. `.github/workflows/deploy.yml` runs on every push to `main`: it builds
the site with `JEKYLL_ENV=production`, renders the CV PDF into the build
output, and deploys `_site/`. Nothing else deploys. The build needs no GitHub
API access: `_config.yml` pins `repository` and `baseurl: ""`, because
jekyll-github-metadata (part of the `github-pages` gem) otherwise rewrites
`baseurl` in production and guesses wrong without a token. `deploy.yml` checks
the canonical URL of the built homepage after every build; keep that check.

`main` is protected with the required status check `quality`, which is the job
id in `.github/workflows/ci.yml`. No workflow token can satisfy that check, so
a workflow that commits or pushes to `main` will always be rejected. Do not add
one. Do not rename the `quality` job either; that blocks every merge.

## Citation counts: a manual Scholar sync, on purpose

Citation counts on `/publications/` and the CV come from Google Scholar via
`fetch_scholar_data.py`. Run `just scholar` locally, look at the diff, open a
PR. `just scholar --citations-only` limits it to one request and to the
`citations`/`scholar_url` fields plus `_data/scholar_stats.yml`; without the
flag the script also hunts for PDFs and creates entries for publications that
are missing locally, which needs a look before it lands.

There is no scheduled workflow for this, and one on GitHub-hosted runners
cannot work: Scholar answers those IP ranges with HTTP 403 (verified on
2026-08-31). Do not add a scheduled Scholar sync unless the data source changes
to an API that allows it, such as OpenAlex or Semantic Scholar; in that case
also reword the "According to Google Scholar" sentences on `/publications/`
and in `cv.markdown`.

## CV PDF: a build artifact, never a committed file

`assets/cv-anne-schuth.pdf` and `assets/cv-thumbnail.png` are not in git and
are listed in `.gitignore`. Both are rendered from the built `/cv/` page by
`generate_cv_pdf.py` (WeasyPrint, pypdfium2 for the thumbnail). Three callers,
one script:

- `deploy.yml` renders them into `_site/assets/`, so they ship with every
  deployment. This is the only copy that reaches the live site.
- `ci.yml` renders them on every pull request and uploads them as the
  `cv-anne-schuth` artifact. A PR that breaks the render fails the required
  `quality` check, before merge.
- `just cv` renders them into `assets/` for a local preview.

What this means in practice:

- Changing the CV is editing `cv.markdown` (or its inputs) and opening a PR.
  There is no regeneration step to remember; the deploy does it.
- Never `git add` the PDF or the thumbnail, and never write a workflow that
  commits them back. That was the previous design; it failed on every push to
  `main` for months because of the branch protection above.
- `check_links.py` treats links to these two files as valid without looking in
  `_site/`, because a local build does not contain them. The deploy workflow
  fails if either file is missing from `_site/assets/`.
- The CI steps that render the PDF (system libraries, script flags) live in
  `.github/actions/render-cv-pdf/action.yml`. Change them there, once.

`just cv` sets `DYLD_FALLBACK_LIBRARY_PATH` to the Homebrew prefix on macOS
(WeasyPrint needs pango/gobject there; on Linux/CI it is a no-op), so `just cv`
works as-is. Do not reintroduce a manual env-var prefix in docs or commands; if
the dyld path is wrong, fix the `cv` recipe in the justfile.

Source of truth is `cv.markdown` plus the includes under `_includes/cv/`.
Print styling lives in `assets/css/cv-print.scss` (WeasyPrint loads it
directly, not via Jekyll). In the rendered CV, the organization is a sans-serif
accent-blue `h4`; the role is a serif bold run in the entry paragraph just
below it. Keep that contrast intact when touching the print stylesheet.
