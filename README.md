# Website of Anne Schuth

Deployed at <https://anneschuth.nl/>

The site is a Jekyll project. GitHub Actions builds it and deploys it to GitHub
Pages on every push to `main` (`.github/workflows/deploy.yml`).
Alongside it live a few Python tools: CV PDF generation, a Google Scholar
citation sync, link and frontmatter checkers, and the Wardley map renderers.

## Development

You need Ruby (version pinned in `.ruby-version`) and [`uv`](https://docs.astral.sh/uv/)
for Python. [`just`](https://github.com/casey/just) is optional but wraps the
common commands.

First-time setup installs the Ruby gems and the Python environment:

```sh
just setup        # or: bundle install && uv sync
```

Serve locally on <http://localhost:4000>:

```sh
just serve        # or: bundle exec jekyll serve
```

Python dependencies live in `pyproject.toml`, split into groups (`cv`,
`scholar`, `checks`, `viz`). `uv sync` installs everything; `uv.lock` pins exact
versions so local and CI match.

## Quality checks

Pre-commit runs the Jekyll build, internal link check, YAML frontmatter check,
`ruff`, and markdownlint. The same hooks run on CI for every push and pull
request, so a green local run means a green CI run:

```sh
just check        # or: uv run pre-commit run --all-files
```

Install the git hook so checks run automatically before each commit:

```sh
uv run pre-commit install
```

## Citation sync

Citation counts come from Google Scholar. `.github/workflows/scholar.yml`
refreshes them on the first day of every month and opens a pull request with
the diff; it never pushes to `main`. It runs `fetch_scholar_data.py
--citations-only`, which does a single request to Scholar and touches only
`_data/scholar_stats.yml` and the `citations` / `scholar_url` fields of
existing publications. Trigger it by hand with `gh workflow run scholar.yml`.

The full script also hunts for PDFs and creates entries for Scholar
publications that are missing locally. That mode is for local use, since its
output needs a look before it lands:

```sh
just scholar      # or: uv run python fetch_scholar_data.py
```

## CV PDF

The CV at `/cv/` is also served as `assets/cv-anne-schuth.pdf`, with a PNG
thumbnail on the about page. Neither file is in git. `deploy.yml` renders both
with WeasyPrint into the built site on every deployment, and `ci.yml` renders
them on every pull request as a smoke test (downloadable there as the
`cv-anne-schuth` artifact). To preview locally:

```sh
just cv           # or: uv run python generate_cv_pdf.py
```

This writes into `assets/`, where both files are gitignored.
