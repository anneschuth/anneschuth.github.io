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

Citation counts come from Google Scholar and are refreshed by hand. Google
answers GitHub-hosted runners with HTTP 403, so there is deliberately no
scheduled workflow for this. Run the sync locally, check the diff, open a PR:

```sh
just scholar      # or: uv run python fetch_scholar_data.py
```

Add `--citations-only` to limit it to a single request and to citation counts;
without it the script also hunts for PDFs and creates entries for publications
that are missing locally.

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
