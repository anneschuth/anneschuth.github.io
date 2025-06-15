#!/usr/bin/env python3
"""
Link checker script for Jekyll site.
Checks for broken internal links before commits.
"""

import os
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

def find_internal_links(content):
    """Extract internal links from markdown content."""
    # Patterns for various link formats
    patterns = [
        r'\[([^\]]+)\]\((/[^)]+)\)',  # [text](/path)
        r'href="(/[^"]+)"',           # href="/path"
        r"href='(/[^']+)'",           # href='/path'
        r'slides_url:\s*(/\S+)',      # slides_url: /path
        r'pdf:\s*(/\S+)',             # pdf: /path
        r'poster_url:\s*(/\S+)',      # poster_url: /path
        r'video_url:\s*(/\S+)',       # video_url: /path (if local)
        r'publication_url:\s*(\S+)',  # publication_url: key
    ]

    links = []
    for pattern in patterns:
        matches = re.findall(pattern, content)
        for match in matches:
            if isinstance(match, tuple):
                link = match[1]  # Get the URL part
            else:
                link = match

            # Skip external URLs
            if link.startswith('http') or '://' in link:
                continue

            links.append(link)

    return links

def check_internal_link(link, base_path="/Users/anneschuth/anneschuth.github.io"):
    """Check if an internal link exists."""
    base = Path(base_path)

    # Handle different link types
    if link.startswith('/assets/'):
        # Asset link
        asset_path = base / link[1:]  # Remove leading /
        return asset_path.exists()

    elif link.startswith('/publications/'):
        # Publication link
        pub_key = link.replace('/publications/', '').replace('.html', '')
        pub_file = base / '_publications' / f'{pub_key}.md'
        return pub_file.exists()

    elif link.startswith('/talks/'):
        # Talk link
        talk_key = link.replace('/talks/', '').replace('.html', '')
        talk_file = base / '_talks' / f'{talk_key}.md'
        return talk_file.exists()

    elif link.startswith('/20'):
        # Post link (YYYY/MM/DD format)
        # These are handled by Jekyll's permalink structure
        # Extract the slug and check if post exists
        parts = link.strip('/').split('/')
        if len(parts) >= 4:
            year, month, day = parts[0], parts[1], parts[2]
            slug = parts[3].replace('.html', '')

            # Look for post file
            post_pattern = f"{year}-{month}-{day}-*.md"
            post_files = list((base / '_posts').glob(post_pattern))

            for post_file in post_files:
                if slug in post_file.stem:
                    return True
            return False

    elif not link.startswith('/') and not link.startswith('http'):
        # Relative publication/talk key reference
        # Check if it's a publication key
        pub_file = base / '_publications' / f'{link}.md'
        if pub_file.exists():
            return True

        # Check if it's a talk key
        talk_file = base / '_talks' / f'{link}.md'
        if talk_file.exists():
            return True

        return False

    # For other absolute paths, check if file exists
    if link.startswith('/'):
        file_path = base / link[1:]
        # Try with .html extension if not present
        if not file_path.exists() and not link.endswith('.html'):
            file_path = base / f"{link[1:]}.html"
        return file_path.exists()

    return True  # Assume external links are okay for now

def check_file_links(file_path):
    """Check all links in a single file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        return [], [f"Error reading {file_path}: {e}"]

    links = find_internal_links(content)
    broken_links = []

    for link in links:
        if not check_internal_link(link):
            broken_links.append(link)

    return links, broken_links

def main():
    """Main link checking function."""
    print("🔗 Jekyll Link Checker")
    print("=" * 50)

    base_path = Path("/Users/anneschuth/anneschuth.github.io")
    content_dirs = ['_publications', '_talks', '_posts']
    page_files = ['software.markdown', 'about.markdown', 'activities.markdown', 'press.markdown', 'publications.markdown', 'talks.markdown', 'teaching.markdown', 'thesis.markdown']

    total_files = 0
    total_links = 0
    total_broken = 0
    broken_by_file = {}

    for content_dir in content_dirs:
        dir_path = base_path / content_dir
        if not dir_path.exists():
            continue

        print(f"\n📁 Checking {content_dir}/")

        for file_path in dir_path.glob("*.md"):
            total_files += 1
            links, broken = check_file_links(file_path)
            total_links += len(links)

            if broken:
                total_broken += len(broken)
                relative_path = file_path.relative_to(base_path)
                broken_by_file[str(relative_path)] = broken
                print(f"  ❌ {relative_path}")
                for link in broken:
                    print(f"     🔗 {link}")
            else:
                relative_path = file_path.relative_to(base_path)
                print(f"  ✅ {relative_path} ({len(links)} links)")

    # Check page files
    print(f"\n📄 Checking page files")
    for page_file in page_files:
        file_path = base_path / page_file
        if file_path.exists():
            total_files += 1
            links, broken = check_file_links(file_path)
            total_links += len(links)

            if broken:
                total_broken += len(broken)
                relative_path = file_path.relative_to(base_path)
                broken_by_file[str(relative_path)] = broken
                print(f"  ❌ {relative_path}")
                for link in broken:
                    print(f"     🔗 {link}")
            else:
                relative_path = file_path.relative_to(base_path)
                print(f"  ✅ {relative_path} ({len(links)} links)")

    # Summary
    print("\n" + "=" * 50)
    print("📊 SUMMARY")
    print(f"Files checked: {total_files}")
    print(f"Links found: {total_links}")
    print(f"Broken links: {total_broken}")

    if broken_by_file:
        print(f"\n❌ Files with broken links: {len(broken_by_file)}")
        for file_path, broken_links in broken_by_file.items():
            print(f"  {file_path}: {len(broken_links)} broken")

        return 1  # Exit with error code
    else:
        print("\n✅ All links are working!")
        return 0

if __name__ == "__main__":
    sys.exit(main())
