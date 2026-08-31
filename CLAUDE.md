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
output, and deploys `_site/`. Nothing else deploys.

`main` is protected with the required status check `quality`, which is the job
id in `.github/workflows/ci.yml`. No workflow token can satisfy that check, so
a workflow that commits or pushes to `main` will always be rejected. Do not add
one. Do not rename the `quality` job either; that blocks every merge.

## Citation counts: a monthly Scholar sync that opens a PR

`.github/workflows/scholar.yml` runs `fetch_scholar_data.py --citations-only`
on the first of every month (and on `gh workflow run scholar.yml`), commits the
result to the branch `scholar-sync`, opens or updates a pull request, and then
dispatches `ci.yml` on that branch. The dispatch is there because a push made
with `GITHUB_TOKEN` does not trigger `pull_request` workflows, and without a run
of `quality` the PR could never be merged. The sync never pushes to `main`.

In that mode the script does one request to Scholar and only refreshes
`_data/scholar_stats.yml` plus the `citations` and `scholar_url` fields of
existing publications. It does not create publication files or download PDFs;
new publications are added by hand, in a PR. A run fails loudly when Scholar
blocks the runner (no publications parsed), so if no sync PR has shown up for a
while, look at the Actions tab rather than assuming the counts are current.
`just scholar` runs the full script locally, including the PDF hunt and the
creation of entries for publications missing locally.

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
