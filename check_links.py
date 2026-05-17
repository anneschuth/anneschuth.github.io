#!/usr/bin/env python3
"""
Link checker for the Jekyll site.

Resolves every internal link against the built site in _site/ rather than
guessing from source files. _site/ is ground truth: if a URL renders to a
file there, the link works. This makes the checker correct about pages that
only exist via `permalink:` front-matter (/cv/, /publications/, /talks/, ...)
and about #fragment anchors, which the old source-guessing logic flagged as
false positives.

Run `jekyll build` before this (the pre-commit config does) so _site/ is
fresh.
"""

import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlparse

REPO = Path(__file__).resolve().parent
SITE = REPO / "_site"

LINK_PATTERNS = [
    r'\[([^\]]+)\]\((/[^)]+)\)',  # [text](/path)
    r'href="(/[^"]+)"',           # href="/path"
    r"href='(/[^']+)'",           # href='/path'
    r'slides_url:\s*(/\S+)',      # slides_url: /path
    r'pdf:\s*(/\S+)',             # pdf: /path
    r'poster_url:\s*(/\S+)',      # poster_url: /path
    r'video_url:\s*(/\S+)',       # video_url: /path
]


def find_internal_links(content):
    """Extract root-relative internal links from markdown/HTML content."""
    active = "\n".join(
        line for line in content.split("\n") if not line.strip().startswith("#")
    )

    links = []
    for pattern in LINK_PATTERNS:
        for match in re.findall(pattern, active):
            link = match[1] if isinstance(match, tuple) else match
            if link.startswith("http") or "://" in link:
                continue
            if link.startswith("/"):
                links.append(link)
    return links


def _resolved_file(path_part):
    """Map a URL path to the file Jekyll would serve for it, or None."""
    path_part = unquote(path_part)
    rel = path_part.lstrip("/")

    if rel == "":
        candidate = SITE / "index.html"
        return candidate if candidate.exists() else None

    direct = SITE / rel
    if direct.is_file():
        return direct

    # Pretty URL: /cv/ -> _site/cv/index.html
    as_index = SITE / rel.rstrip("/") / "index.html"
    if as_index.is_file():
        return as_index

    # Permalink without trailing slash or extension: /cv -> _site/cv/index.html
    as_html = SITE / f"{rel}.html"
    if as_html.is_file():
        return as_html

    return None


def check_internal_link(link):
    """True if the link resolves in the built site, fragments included."""
    parsed = urlparse(link)
    target = _resolved_file(parsed.path)
    if target is None:
        return False

    if not parsed.fragment:
        return True

    # Verify the #anchor exists as an id/name in the target page.
    try:
        html = target.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return False
    frag = re.escape(unquote(parsed.fragment))
    return bool(
        re.search(rf'\bid="{frag}"', html) or re.search(rf'\bname="{frag}"', html)
    )


def check_file_links(file_path):
    try:
        content = Path(file_path).read_text(encoding="utf-8")
    except OSError as e:
        return [], [f"Error reading {file_path}: {e}"]

    links = find_internal_links(content)
    broken = [link for link in links if not check_internal_link(link)]
    return links, broken


def main():
    print("🔗 Jekyll Link Checker")
    print("=" * 50)

    if not SITE.exists():
        print(f"\n❌ {SITE} not found. Run `bundle exec jekyll build` first.")
        return 1

    content_dirs = ["_publications", "_talks", "_posts", "_software"]
    page_files = [
        "software.markdown", "about.markdown", "activities.markdown",
        "press.markdown", "publications.markdown", "talks.markdown",
        "teaching.markdown", "thesis.markdown", "cv.markdown",
    ]

    total_files = total_links = total_broken = 0
    broken_by_file = {}

    def report(file_path, links, broken):
        nonlocal total_broken
        rel = Path(file_path).relative_to(REPO)
        if broken:
            total_broken += len(broken)
            broken_by_file[str(rel)] = broken
            print(f"  ❌ {rel}")
            for link in broken:
                print(f"     🔗 {link}")
        else:
            print(f"  ✅ {rel} ({len(links)} links)")

    for content_dir in content_dirs:
        dir_path = REPO / content_dir
        if not dir_path.exists():
            continue
        print(f"\n📁 Checking {content_dir}/")
        for file_path in sorted(dir_path.glob("*.md")):
            total_files += 1
            links, broken = check_file_links(file_path)
            total_links += len(links)
            report(file_path, links, broken)

    print("\n📄 Checking page files")
    for page_file in page_files:
        file_path = REPO / page_file
        if not file_path.exists():
            continue
        total_files += 1
        links, broken = check_file_links(file_path)
        total_links += len(links)
        report(file_path, links, broken)

    print("\n" + "=" * 50)
    print("📊 SUMMARY")
    print(f"Files checked: {total_files}")
    print(f"Links found: {total_links}")
    print(f"Broken links: {total_broken}")

    if broken_by_file:
        print(f"\n❌ Files with broken links: {len(broken_by_file)}")
        for file_path, broken_links in broken_by_file.items():
            print(f"  {file_path}: {len(broken_links)} broken")
        return 1

    print("\n✅ All links are working!")
    return 0


if __name__ == "__main__":
    sys.exit(main())
