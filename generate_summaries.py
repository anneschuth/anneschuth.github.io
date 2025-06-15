#!/usr/bin/env python3
"""
Generate actual summaries for talks using Claude Code Task tool.
"""

import os
import re
from pathlib import Path
import subprocess

def get_talks_with_slides():
    """Find talks that have slide PDFs available."""
    talks_with_slides = []
    
    for file_path in Path("_talks").glob("*.md"):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Look for slides_url
            slides_match = re.search(r'slides_url:\s*(/assets/[^\s]+\.pdf)', content)
            if slides_match:
                slides_path = slides_match.group(1)
                # Check if it's not commented out
                line_start = content.rfind('\n', 0, slides_match.start()) + 1
                line = content[line_start:slides_match.end()]
                
                if not line.strip().startswith('#'):
                    # Check if file exists
                    asset_path = Path(slides_path[1:])  # Remove leading /
                    if asset_path.exists():
                        title = extract_title_from_talk(content)
                        venue = extract_venue_from_talk(content)
                        talks_with_slides.append({
                            'talk_file': file_path,
                            'slides_path': asset_path,
                            'slides_url': slides_path,
                            'title': title,
                            'venue': venue
                        })
        except Exception as e:
            print(f"Error processing {file_path}: {e}")
            continue
    
    return talks_with_slides

def extract_title_from_talk(content):
    """Extract title from talk frontmatter."""
    title_match = re.search(r'title:\s*([^\n]+)', content)
    if title_match:
        return title_match.group(1).strip().strip('"\'')
    return "Unknown Title"

def extract_venue_from_talk(content):
    """Extract venue from talk frontmatter."""
    venue_match = re.search(r'venue:\s*([^\n]+)', content)
    if venue_match:
        return venue_match.group(1).strip().strip('"\'')
    return "Unknown Venue"

def extract_text_from_pdf(pdf_path):
    """Extract text from PDF using pdftotext."""
    try:
        # Try pdftotext first (better for slides)
        result = subprocess.run(['pdftotext', str(pdf_path), '-'], 
                              capture_output=True, text=True, timeout=30)
        if result.returncode == 0 and result.stdout.strip():
            return result.stdout
    except (subprocess.TimeoutExpired, FileNotFoundError):
        pass
    
    try:
        # Fallback to pdfplumber via python
        import pdfplumber
        text = ""
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages[:10]:  # Only first 10 pages for performance
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
        return text
    except ImportError:
        print("Neither pdftotext nor pdfplumber available. Install with: pip install pdfplumber")
        return None
    except Exception as e:
        print(f"Error extracting text from {pdf_path}: {e}")
        return None

def main():
    """Generate summaries for the first few talks."""
    print("📊 SUMMARY GENERATOR")
    print("=" * 50)
    
    # Get talks with slides
    talks_with_slides = get_talks_with_slides()
    print(f"Found {len(talks_with_slides)} talks with slide PDFs")
    
    if not talks_with_slides:
        print("No talks with slides found!")
        return
    
    # Process first 3 talks as examples
    for i, talk in enumerate(talks_with_slides[:3]):
        print(f"\n[{i+1}/3] Processing: {talk['title']}")
        print(f"Venue: {talk['venue']}")
        print(f"Slides: {talk['slides_path']}")
        
        # Extract text from PDF
        print("  📄 Extracting text from PDF...")
        text = extract_text_from_pdf(talk['slides_path'])
        if not text:
            print("  ❌ Could not extract text from PDF")
            continue
            
        print(f"  ✅ Extracted {len(text)} characters")
        
        # Clean up the text for Claude
        lines = text.split('\n')
        # Remove very short lines (likely headers/footers)
        lines = [line.strip() for line in lines if len(line.strip()) > 10]
        # Remove duplicates (common in slides)
        seen = set()
        unique_lines = []
        for line in lines:
            if line not in seen and len(line) > 20:
                seen.add(line)
                unique_lines.append(line)
        
        cleaned_text = '\n'.join(unique_lines[:50])  # Limit to first 50 unique lines
        
        if len(cleaned_text.strip()) < 200:
            print("  ❌ Insufficient content for analysis")
            continue
        
        # Create prompt for Claude
        prompt = f"""Please analyze this presentation content and create a concise 2-3 sentence summary for an academic website:

**Title**: {talk['title']}
**Venue**: {talk['venue']}

**Extracted Presentation Content**:
{cleaned_text[:2500]}

Create a summary that captures:
1. The main research topic/question being addressed
2. Key methodology, approach, or findings presented  
3. The academic/practical contribution or significance

Format as a single paragraph suitable for display on an academic website. Focus on substance over buzzwords."""
        
        print("\n" + "="*60)
        print(f"PROMPT FOR: {talk['title']}")
        print("="*60)
        print(prompt)
        print("="*60)
        print("\nNow I'll use the Task tool to generate the summary...")
        break  # Just show one example for now

if __name__ == "__main__":
    main()