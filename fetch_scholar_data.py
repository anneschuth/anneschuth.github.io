#!/usr/bin/env python3
"""
Fetch citation data from Google Scholar profile and update publications.
"""

import requests
import re
import time
import random
from pathlib import Path
from urllib.parse import quote, urljoin
from bs4 import BeautifulSoup

def fetch_scholar_profile(user_id="Y3ahb_wAAAAJ"):
    """Fetch all publications and profile stats from Google Scholar profile."""
    base_url = "https://scholar.google.com/citations"
    url = f"{base_url}?user={user_id}&hl=en&cstart=0&pagesize=100"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    try:
        response = requests.get(url, headers=headers, timeout=15)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, 'html.parser')
        publications = []

        # Extract profile statistics
        profile_stats = {}

        # Find citation stats table
        stats_table = soup.find('table', {'id': 'gsc_rsb_st'})
        if stats_table:
            rows = stats_table.find_all('tr')
            for row in rows:
                cells = row.find_all('td')
                if len(cells) >= 2:
                    label = cells[0].get_text().strip()
                    value = cells[1].get_text().strip()

                    if 'Citations' in label and 'All' in value:
                        # Extract total citations (first number)
                        try:
                            profile_stats['total_citations'] = int(value.split()[0])
                        except (ValueError, IndexError):
                            pass
                    elif 'h-index' in label and 'All' in value:
                        # Extract h-index (first number)
                        try:
                            profile_stats['h_index'] = int(value.split()[0])
                        except (ValueError, IndexError):
                            pass

        # Alternative method: look for citation metrics in different structure
        if 'total_citations' not in profile_stats or 'h_index' not in profile_stats:
            # Try finding citation metrics in the sidebar
            citation_elements = soup.find_all('td', class_='gsc_rsb_std')
            if len(citation_elements) >= 2:
                try:
                    if 'total_citations' not in profile_stats:
                        profile_stats['total_citations'] = int(citation_elements[0].get_text().strip())
                    if 'h_index' not in profile_stats:
                        profile_stats['h_index'] = int(citation_elements[2].get_text().strip())
                except (ValueError, IndexError):
                    pass

        # Find all publication rows
        rows = soup.find_all('tr', class_='gsc_a_tr')

        for row in rows:
            # Extract title and link
            title_cell = row.find('a', class_='gsc_a_at')
            if not title_cell:
                continue

            title = title_cell.get_text().strip()
            scholar_link = urljoin(base_url, title_cell.get('href', ''))

            # Extract citation count
            cite_cell = row.find('a', class_='gsc_a_ac')
            citations = 0
            if cite_cell and cite_cell.get_text().strip():
                try:
                    citations = int(cite_cell.get_text().strip())
                except ValueError:
                    citations = 0

            # Extract year
            year_cell = row.find('span', class_='gsc_a_h')
            year = year_cell.get_text().strip() if year_cell else ""

            publications.append({
                'title': title,
                'citations': citations,
                'year': year,
                'scholar_url': scholar_link
            })

        return publications, profile_stats

    except Exception as e:
        print(f"Error fetching Scholar profile: {e}")
        return [], {}

def normalize_title(title):
    """Normalize title for comparison."""
    # Remove punctuation, convert to lowercase, remove extra whitespace
    normalized = re.sub(r'[^\w\s]', ' ', title.lower())
    normalized = ' '.join(normalized.split())
    return normalized

def find_best_match(pub_title, scholar_publications):
    """Find the best matching publication from Scholar data."""
    pub_normalized = normalize_title(pub_title)

    best_match = None
    best_score = 0

    for scholar_pub in scholar_publications:
        scholar_normalized = normalize_title(scholar_pub['title'])

        # Calculate similarity score (simple word overlap)
        pub_words = set(pub_normalized.split())
        scholar_words = set(scholar_normalized.split())

        if len(pub_words) == 0 or len(scholar_words) == 0:
            continue

        intersection = pub_words.intersection(scholar_words)
        union = pub_words.union(scholar_words)

        score = len(intersection) / len(union) if union else 0

        # Boost score if titles are very similar in length
        if abs(len(pub_words) - len(scholar_words)) <= 2:
            score += 0.1

        if score > best_score and score > 0.5:  # Minimum threshold
            best_score = score
            best_match = scholar_pub

    return best_match, best_score

def update_publication_with_scholar_data(file_path, scholar_data):
    """Update publication file with Scholar citation and URL data."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        lines = content.split('\n')
        new_lines = []
        frontmatter_started = False
        frontmatter_ended = False
        citations_updated = False
        scholar_url_updated = False

        for line in lines:
            if line.strip() == '---':
                if not frontmatter_started:
                    frontmatter_started = True
                elif not frontmatter_ended:
                    frontmatter_ended = True

            if frontmatter_started and not frontmatter_ended:
                # We're in the frontmatter
                if line.startswith('citations:'):
                    new_lines.append(f'citations: {scholar_data["citations"]}')
                    citations_updated = True
                elif line.startswith('scholar_url:'):
                    new_lines.append(f'scholar_url: "{scholar_data["scholar_url"]}"')
                    scholar_url_updated = True
                elif line.startswith('title:') and not citations_updated:
                    new_lines.append(line)
                    new_lines.append(f'citations: {scholar_data["citations"]}')
                    if not scholar_url_updated:
                        new_lines.append(f'scholar_url: "{scholar_data["scholar_url"]}"')
                        scholar_url_updated = True
                    citations_updated = True
                else:
                    new_lines.append(line)
            else:
                new_lines.append(line)

        # Write updated content
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(new_lines))

        return True

    except Exception as e:
        print(f"Error updating {file_path}: {e}")
        return False

def save_profile_stats(stats):
    """Save profile statistics to a data file."""
    try:
        stats_file = Path("_data/scholar_stats.yml")
        stats_file.parent.mkdir(exist_ok=True)

        with open(stats_file, 'w', encoding='utf-8') as f:
            f.write("# Google Scholar Profile Statistics\n")
            f.write("# Auto-generated by fetch_scholar_data.py\n")
            f.write(f"total_citations: {stats.get('total_citations', 0)}\n")
            f.write(f"h_index: {stats.get('h_index', 0)}\n")
            f.write(f"last_updated: \"{time.strftime('%Y-%m-%d %H:%M:%S')}\"\n")

        return True

    except Exception as e:
        print(f"Error saving profile stats: {e}")
        return False

def main():
    """Main function."""
    print("🎓 GOOGLE SCHOLAR DATA FETCHER")
    print("=" * 50)

    # Fetch Scholar profile data
    print("📡 Fetching Google Scholar profile...")
    scholar_pubs, profile_stats = fetch_scholar_profile()

    if not scholar_pubs:
        print("❌ Failed to fetch Scholar data")
        return 1

    print(f"✅ Found {len(scholar_pubs)} publications on Google Scholar")

    # Display and save profile statistics
    if profile_stats:
        total_cites = profile_stats.get('total_citations', 'Unknown')
        h_index = profile_stats.get('h_index', 'Unknown')
        print(f"📊 Profile Stats: {total_cites} total citations, h-index: {h_index}")

        if save_profile_stats(profile_stats):
            print("✅ Profile statistics saved to _data/scholar_stats.yml")
    else:
        print("⚠️  Could not extract profile statistics")

    # Process local publications
    publications_dir = Path("_publications")
    if not publications_dir.exists():
        print("❌ _publications directory not found!")
        return 1

    publication_files = list(publications_dir.glob("*.md"))
    print(f"📚 Processing {len(publication_files)} local publications")

    updated_count = 0
    matched_count = 0

    for i, pub_file in enumerate(publication_files):
        print(f"\n[{i+1}/{len(publication_files)}] {pub_file.name}")

        # Extract title from local file
        try:
            with open(pub_file, 'r', encoding='utf-8') as f:
                content = f.read()

            title_match = re.search(r'^title:\s*["\']?([^"\'\n]+)["\']?', content, re.MULTILINE)
            if not title_match:
                print("  ⏭️  No title found")
                continue

            local_title = title_match.group(1).strip()
            print(f"  📄 {local_title[:60]}{'...' if len(local_title) > 60 else ''}")

        except Exception as e:
            print(f"  ❌ Error reading file: {e}")
            continue

        # Find matching Scholar publication
        match, score = find_best_match(local_title, scholar_pubs)

        if match:
            print(f"  ✅ Matched (score: {score:.2f}): {match['title'][:50]}...")
            print(f"  📊 Citations: {match['citations']}")

            # Update the file
            if update_publication_with_scholar_data(pub_file, match):
                print(f"  ✅ Updated file with Scholar data")
                updated_count += 1
            else:
                print(f"  ❌ Failed to update file")

            matched_count += 1
        else:
            print("  ⚠️  No good match found")

    print(f"\n🎉 COMPLETED")
    print(f"Matched: {matched_count}/{len(publication_files)}")
    print(f"Updated: {updated_count}")

    return 0

if __name__ == "__main__":
    exit(main())
