#!/usr/bin/env python3
"""
Script to fix asset naming conventions and update references.
"""

import os
import re
import shutil
from pathlib import Path

def analyze_asset_patterns():
    """Analyze current asset naming patterns."""
    assets_dir = Path("assets")
    patterns = {
        'date_prefixed': [],  # 20150809-SIGIR-multileave.pdf
        'author_topic': [],   # appliedml-anneschuth-streamingblendle.pdf
        'paper_title': [],    # chuklin-evaluating-2013.pdf
        'arxiv_id': [],       # 1907.00570.pdf
        'descriptive': [],    # helping-people-choose-2009.pdf
        'problematic': []     # Files with spaces, weird chars, etc.
    }
    
    for file_path in assets_dir.glob("*.pdf"):
        filename = file_path.name
        
        if re.match(r'^\d{8}-', filename):
            patterns['date_prefixed'].append(filename)
        elif re.match(r'^\d{4}\.\d{5}\.pdf$', filename):
            patterns['arxiv_id'].append(filename)
        elif 'anneschuth' in filename.lower():
            patterns['author_topic'].append(filename)
        elif re.search(r'\s|[A-Z]{2,}', filename):
            patterns['problematic'].append(filename)
        else:
            patterns['descriptive'].append(filename)
    
    return patterns

def propose_asset_fixes():
    """Propose standardized names for assets."""
    assets_dir = Path("assets")
    fixes = []
    
    for file_path in assets_dir.glob("*.pdf"):
        old_name = file_path.name
        new_name = old_name
        
        # Fix common issues
        # 1. Remove multiple spaces/underscores
        new_name = re.sub(r'[\s_]+', '-', new_name)
        
        # 2. Fix case issues in titles
        if ' ' in old_name:
            # Has spaces - needs fixing
            new_name = old_name.replace(' ', '-').lower()
            # Keep PDF extension uppercase if needed
            new_name = re.sub(r'\.pdf$', '.pdf', new_name, flags=re.IGNORECASE)
        
        # 3. Remove duplicate separators
        new_name = re.sub(r'-+', '-', new_name)
        
        # 4. Fix specific problematic names
        problem_fixes = {
            'Effective-Headlines-of-Newspaper-Articles-in-a-Digital-Environment.pdf': 
                'effective-headlines-newspaper-digital-environment.pdf',
            'Effective_Headlines_of_Newspaper_Articles_in_a_Digital_Environment.pdf':
                'effective-headlines-newspaper-digital-environment.pdf',
            'Effects-of-Position-Bias-on-Click-Based-Recommender-Evaluation-revised.pdf':
                'effects-position-bias-click-recommender-evaluation-revised.pdf',
            'Digital_sustainable_publication_of_legacy_parliament.pdf':
                'digital-sustainable-publication-legacy-parliament.pdf',
            'XML_Data_Integration_in_Action.pdf':
                'xml-data-integration-action.pdf'
        }
        
        if old_name in problem_fixes:
            new_name = problem_fixes[old_name]
        
        if new_name != old_name:
            new_path = assets_dir / new_name
            fixes.append((file_path, new_path, old_name, new_name))
    
    return fixes

def find_asset_references(filename):
    """Find all references to an asset file."""
    references = []
    search_dirs = ['_publications', '_talks', '_posts']
    
    for search_dir in search_dirs:
        for file_path in Path(search_dir).glob("*.md"):
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                if filename in content:
                    references.append(file_path)
            except:
                continue
    
    return references

def update_asset_references(old_name, new_name):
    """Update all references to a renamed asset."""
    updated_files = []
    search_dirs = ['_publications', '_talks', '_posts']
    
    for search_dir in search_dirs:
        for file_path in Path(search_dir).glob("*.md"):
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                if old_name in content:
                    new_content = content.replace(old_name, new_name)
                    
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    
                    updated_files.append(file_path)
            except Exception as e:
                print(f"Error updating {file_path}: {e}")
    
    return updated_files

def main():
    """Run asset cleanup."""
    print("=== ASSET CLEANUP SCRIPT ===\n")
    
    # Analyze current patterns
    patterns = analyze_asset_patterns()
    print("Current asset patterns:")
    for pattern_name, files in patterns.items():
        print(f"  {pattern_name}: {len(files)} files")
        if files and pattern_name == 'problematic':
            print(f"    Examples: {files[:3]}")
    
    # Get proposed fixes
    fixes = propose_asset_fixes()
    print(f"\nFound {len(fixes)} asset files that need fixing")
    
    if not fixes:
        print("No asset fixes needed!")
        return
    
    # Show proposed changes
    print("\n=== PROPOSED ASSET CHANGES ===")
    for old_path, new_path, old_name, new_name in fixes:
        print(f"{old_name}")
        print(f"  -> {new_name}")
        
        # Show what files reference this asset
        refs = find_asset_references(old_name)
        if refs:
            print(f"     Referenced in: {len(refs)} files")
        print()
    
    # Ask for confirmation
    response = input("Proceed with asset fixes? (y/N): ")
    if response.lower() != 'y':
        print("Aborted.")
        return
    
    # Apply fixes
    print("\n=== APPLYING ASSET FIXES ===")
    for old_path, new_path, old_name, new_name in fixes:
        try:
            # Rename the file
            shutil.move(str(old_path), str(new_path))
            print(f"Renamed: {old_name} -> {new_name}")
            
            # Update all references
            updated_files = update_asset_references(old_name, new_name)
            if updated_files:
                print(f"  Updated {len(updated_files)} files")
            
        except Exception as e:
            print(f"Error renaming {old_name}: {e}")
    
    print("\n=== ASSET CLEANUP COMPLETE ===")

if __name__ == "__main__":
    main()