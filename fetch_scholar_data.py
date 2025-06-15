#!/usr/bin/env python3
"""
Fetch citation data from Google Scholar profile and update publications.
"""

import requests
import re
import time
import random
import os
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
                    # Add missing fields at the end of frontmatter if not found
                    if not citations_updated:
                        new_lines.append(f'citations: {scholar_data["citations"]}')
                    if not scholar_url_updated:
                        new_lines.append(f'scholar_url: "{scholar_data["scholar_url"]}"')

            if frontmatter_started and not frontmatter_ended:
                # We're in the frontmatter
                if line.startswith('citations:'):
                    new_lines.append(f'citations: {scholar_data["citations"]}')
                    citations_updated = True
                elif line.startswith('scholar_url:'):
                    new_lines.append(f'scholar_url: "{scholar_data["scholar_url"]}"')
                    scholar_url_updated = True
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

def fetch_publication_details(scholar_url):
    """Fetch detailed publication information from individual Scholar page."""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        response = requests.get(scholar_url, headers=headers, timeout=15)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')
        details = {}
        
        # Extract title (for better accuracy)
        title_elem = soup.find('a', class_='gsc_oci_title_link')
        if title_elem:
            details['title'] = title_elem.get_text().strip()
        
        # Extract details from the metadata table
        field_rows = soup.find_all('div', class_='gs_scl')
        
        for row in field_rows:
            field_name = row.find('div', class_='gsc_oci_field')
            field_value = row.find('div', class_='gsc_oci_value')
            
            if field_name and field_value:
                field_text = field_name.get_text().strip().lower()
                value_text = field_value.get_text().strip()
                
                if 'authors' in field_text:
                    # Clean up author names
                    authors = value_text.replace('Authors', '').strip()
                    if authors:
                        details['authors'] = authors
                
                elif 'publication date' in field_text or 'year' in field_text:
                    year_match = re.search(r'\d{4}', value_text)
                    if year_match:
                        details['year'] = year_match.group()
                
                elif any(venue_word in field_text for venue_word in ['journal', 'conference', 'book', 'venue', 'published']):
                    # Clean up venue information
                    venue = value_text.strip()
                    
                    # Remove common prefixes and clean up venue
                    venue = re.sub(r'^(Proceedings of the|Proceedings of|In |Journal of )', '', venue, flags=re.IGNORECASE)
                    
                    # Handle truncated venue names that have "..." or weird concatenations
                    if '...' in venue or len(venue.split()) > 15:
                        # Try to extract just the main venue name
                        venue_parts = venue.split(',')[0].split('.')[0].strip()
                        if len(venue_parts) < 100:  # Reasonable length
                            venue = venue_parts
                    
                    # Clean up common formatting issues
                    venue = re.sub(r'\s+', ' ', venue)  # Multiple spaces
                    venue = venue.replace('\n', ' ').strip()
                    
                    if venue and len(venue) > 3 and len(venue) < 200:  # Reasonable length
                        details['venue'] = venue
        
        # Look for PDF link - try multiple strategies
        pdf_url = None
        
        # Strategy 1: Look for direct PDF links
        pdf_links = soup.find_all('a', href=True)
        for link in pdf_links:
            href = link.get('href', '')
            link_text = link.get_text().strip().lower()
            
            # Check if it's a PDF link
            if (href.endswith('.pdf') or 'pdf' in href.lower()) and 'scholar' not in href:
                pdf_url = href
                break
            
            # Check if link text suggests PDF
            if any(pdf_word in link_text for pdf_word in ['pdf', 'download']):
                pdf_url = href
                break
        
        # Strategy 2: Look in the sidebar for PDF
        if not pdf_url:
            sidebar_links = soup.find_all('div', class_='gsc_oci_merged_snippet')
            for div in sidebar_links:
                links = div.find_all('a', href=True)
                for link in links:
                    href = link.get('href', '')
                    if href.endswith('.pdf') and 'scholar' not in href:
                        pdf_url = href
                        break
        
        if pdf_url:
            details['pdf_url'] = pdf_url
        
        return details
        
    except Exception as e:
        print(f"Error fetching publication details: {e}")
        return {}

def download_pdf(pdf_url, filename):
    """Download PDF file to assets folder."""
    try:
        assets_dir = Path("assets")
        assets_dir.mkdir(exist_ok=True)
        
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        response = requests.get(pdf_url, headers=headers, timeout=30)
        response.raise_for_status()
        
        # Check if it's actually a PDF
        if response.headers.get('content-type', '').startswith('application/pdf'):
            file_path = assets_dir / filename
            with open(file_path, 'wb') as f:
                f.write(response.content)
            return str(file_path)
        
        return None
        
    except Exception as e:
        print(f"Error downloading PDF: {e}")
        return None

def generate_publication_key(title, year, author=None):
    """Generate a unique key for a publication."""
    # Extract first author's last name if available
    first_author = "unknown"
    if author:
        # Handle "Lastname, Firstname" or "Firstname Lastname" formats
        author_parts = author.split(',')[0].strip()  # Get first author
        if ' ' in author_parts:
            # Assume "Firstname Lastname" format
            first_author = author_parts.split()[-1].lower()
        else:
            first_author = author_parts.lower()
    
    # Clean up first word of title
    title_words = re.sub(r'[^\w\s]', '', title.lower()).split()
    first_title_word = title_words[0] if title_words else "untitled"
    
    # Create key: firstauthor + year + firstword
    key = f"{first_author}{year}{first_title_word}"
    
    # Remove any remaining non-alphanumeric characters
    key = re.sub(r'[^\w]', '', key)
    
    return key

def create_publication_file(scholar_pub, details=None):
    """Create a new publication markdown file."""
    try:
        # Use improved title if available from details
        title = details.get('title', scholar_pub['title']) if details else scholar_pub['title']
        year = details.get('year', scholar_pub['year']) if details else scholar_pub['year']
        
        # Generate key
        author = details.get('authors') if details else None
        pub_key = generate_publication_key(title, year, author)
        
        # Generate filename from key
        filename = f"{pub_key}.md"
        
        # Ensure unique filename
        pub_file = Path("_publications") / filename
        counter = 1
        while pub_file.exists():
            filename = f"{pub_key}{counter}.md"
            pub_file = Path("_publications") / filename
            counter += 1
        
        # Create frontmatter with proper ordering
        frontmatter = {}
        
        # Add author first if available
        if details and 'authors' in details:
            frontmatter['author'] = details['authors']
        
        # Add venue/booktitle
        if details and 'venue' in details:
            frontmatter['booktitle'] = details['venue']
        
        # Add date (quoted string)
        frontmatter['date'] = f"{year}-01-01"
        
        # Add key
        frontmatter['key'] = pub_key
        
        # Add layout
        frontmatter['layout'] = 'publication'
        
        # Try to download PDF
        if details and 'pdf_url' in details:
            pdf_filename = f"{pub_key}.pdf"
            print(f"    📥 Attempting to download PDF...")
            pdf_path = download_pdf(details['pdf_url'], pdf_filename)
            if pdf_path:
                frontmatter['pdf'] = f"/assets/{pdf_filename}"
                print(f"    ✅ Downloaded PDF")
            else:
                print(f"    ⚠️  Could not download PDF")
        
        # Add title
        frontmatter['title'] = title
        
        # Add citations and scholar_url
        frontmatter['citations'] = scholar_pub['citations']
        frontmatter['scholar_url'] = scholar_pub['scholar_url']
        
        # Add type and year
        frontmatter['type'] = 'inproceedings'  # Default type
        frontmatter['year'] = year
        
        # Write file with proper YAML formatting
        with open(pub_file, 'w', encoding='utf-8') as f:
            f.write("---\n")
            for key, value in frontmatter.items():
                if isinstance(value, str):
                    # Handle strings that need quoting
                    if '"' in value or "'" in value or ':' in value or '\n' in value:
                        # Escape quotes and use double quotes
                        escaped_value = value.replace('"', '\\"')
                        f.write(f'{key}: "{escaped_value}"\n')
                    else:
                        # Simple strings can be quoted or unquoted
                        f.write(f'{key}: "{value}"\n')
                else:
                    # Numbers, booleans, etc.
                    f.write(f'{key}: {value}\n')
            f.write("---\n\n")
            
            # Add meaningful content based on publication type and venue
            if details and 'venue' in details:
                venue = details['venue']
                if any(workshop_word in venue.lower() for workshop_word in ['workshop', 'demo', 'poster']):
                    content_type = "workshop paper"
                elif any(conf_word in venue.lower() for conf_word in ['conference', 'proceedings', 'symposium']):
                    content_type = "conference paper"
                elif any(journal_word in venue.lower() for journal_word in ['journal', 'transactions', 'letters']):
                    content_type = "journal article"
                else:
                    content_type = "publication"
                
                f.write(f"This {content_type} was presented at {venue} in {year}. ")
            else:
                f.write(f"This publication was published in {year}. ")
            
            # Add information about citations if significant
            if scholar_pub['citations'] > 0:
                f.write(f"It has received {scholar_pub['citations']} citation{'s' if scholar_pub['citations'] != 1 else ''} according to Google Scholar.")
            else:
                f.write("The full text and additional details are available through the links above.")
        
        return pub_file
        
    except Exception as e:
        print(f"Error creating publication file: {e}")
        return None

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
    pdf_downloaded_count = 0
    local_titles = []

    # First pass: update existing publications
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
            local_titles.append(local_title)
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

            # Check if this publication needs a PDF
            try:
                with open(pub_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Check if it already has a PDF
                if 'pdf:' not in content:
                    print(f"  📄 No PDF found, searching for one...")
                    
                    # Fetch detailed page to look for PDF
                    details = fetch_publication_details(match['scholar_url'])
                    if details and 'pdf_url' in details:
                        # Generate filename from publication key or title
                        key_match = re.search(r'^key:\s*(\w+)', content, re.MULTILINE)
                        if key_match:
                            pdf_filename = f"{key_match.group(1)}.pdf"
                        else:
                            # Fallback to safe title
                            safe_title = re.sub(r'[^\w\s-]', '', local_title.lower())
                            safe_title = re.sub(r'[-\s]+', '-', safe_title)[:30]
                            pdf_filename = f"{safe_title}.pdf"
                        
                        print(f"    📥 Attempting to download PDF...")
                        pdf_path = download_pdf(details['pdf_url'], pdf_filename)
                        if pdf_path:
                            # Add PDF to frontmatter
                            lines = content.split('\n')
                            new_lines = []
                            frontmatter_started = False
                            frontmatter_ended = False
                            pdf_added = False
                            
                            for line in lines:
                                if line.strip() == '---':
                                    if not frontmatter_started:
                                        # Opening frontmatter
                                        frontmatter_started = True
                                        new_lines.append(line)
                                    elif not frontmatter_ended:
                                        # Closing frontmatter - add PDF before it
                                        if not pdf_added:
                                            new_lines.append(f'pdf: "/assets/{pdf_filename}"')
                                            pdf_added = True
                                        frontmatter_ended = True
                                        new_lines.append(line)
                                    else:
                                        new_lines.append(line)
                                else:
                                    new_lines.append(line)
                            
                            # Write updated content
                            with open(pub_file, 'w', encoding='utf-8') as f:
                                f.write('\n'.join(new_lines))
                            
                            print(f"    ✅ Downloaded and added PDF")
                            pdf_downloaded_count += 1
                        else:
                            print(f"    ⚠️  Could not download PDF")
                    else:
                        print(f"    ⚠️  No PDF URL found")
                    
                    # Be nice to Google Scholar
                    time.sleep(random.uniform(1, 3))
            
            except Exception as e:
                print(f"  ❌ Error checking for PDF: {e}")

            matched_count += 1
        else:
            print("  ⚠️  No good match found")

    # Second pass: find missing publications and create them
    print(f"\n🔍 FINDING MISSING PUBLICATIONS")
    missing_pubs = []
    
    for scholar_pub in scholar_pubs:
        # Check if this Scholar publication exists locally
        found = False
        
        # Strategy 1: Check against local titles using bidirectional matching
        for local_title in local_titles:
            # Check both directions for better matching
            _, score1 = find_best_match(local_title, [scholar_pub])
            _, score2 = find_best_match(scholar_pub['title'], [{'title': local_title}])
            
            max_score = max(score1, score2) if score1 or score2 else 0
            
            if max_score > 0.5:  # Same threshold as matching
                found = True
                break
        
        # Strategy 2: Check for very similar short titles (only for very short titles)
        if not found:
            scholar_title_words = set(re.sub(r'[^\w\s]', '', scholar_pub['title'].lower()).split())
            
            # Only apply this check for very short titles (2 words or less)
            if len(scholar_title_words) <= 2:
                for local_title in local_titles:
                    local_title_words = set(re.sub(r'[^\w\s]', '', local_title.lower()).split())
                    
                    # For very short titles, require exact match or near-exact match
                    if len(scholar_title_words.intersection(local_title_words)) == len(scholar_title_words):
                        found = True
                        print(f"  🔍 Short title duplicate detected: '{scholar_pub['title']}' matches '{local_title}'")
                        break
        
        if not found:
            missing_pubs.append(scholar_pub)

    if missing_pubs:
        print(f"📚 Found {len(missing_pubs)} missing publications")
        
        created_count = 0
        for i, scholar_pub in enumerate(missing_pubs[:10]):  # Limit to 10 new publications
            print(f"\n[{i+1}/{min(len(missing_pubs), 10)}] Creating: {scholar_pub['title'][:60]}...")
            
            # Fetch additional details
            print("  🔍 Fetching publication details...")
            details = fetch_publication_details(scholar_pub['scholar_url'])
            
            # Create the publication file
            pub_file = create_publication_file(scholar_pub, details)
            if pub_file:
                print(f"  ✅ Created {pub_file.name}")
                created_count += 1
            else:
                print(f"  ❌ Failed to create publication file")
            
            # Be nice to Google Scholar
            time.sleep(random.uniform(2, 5))
        
        if len(missing_pubs) > 10:
            print(f"\n⚠️  Only created first 10 of {len(missing_pubs)} missing publications")
            print("Run the script again to create more.")
        
        print(f"📝 Created {created_count} new publication files")
    else:
        print("✅ All publications are already present locally")

    print(f"\n🎉 COMPLETED")
    print(f"Matched: {matched_count}/{len(publication_files)}")
    print(f"Updated: {updated_count}")
    if pdf_downloaded_count > 0:
        print(f"PDFs downloaded: {pdf_downloaded_count}")
    if missing_pubs:
        print(f"Created: {created_count} new publications")

    return 0

if __name__ == "__main__":
    exit(main())
