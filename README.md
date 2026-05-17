# Website of Anne Schuth

Deployed at <https://anneschuth.nl/>

The site is a Jekyll project, served by GitHub Pages natively from `main`.
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

Citation counts come from Google Scholar and are refreshed on demand, not on
every commit (the scrape hits the network and rate-limits):

```sh
just scholar      # or: uv run pre-commit run --hook-stage manual update-citations
```

The CV PDF at `assets/cv-anne-schuth.pdf` regenerates automatically via the
`cv.yml` workflow when CV inputs change. To rebuild it by hand:

```sh
just cv           # or: uv run python generate_cv_pdf.py
```
