#!/usr/bin/env python3
"""
Script to systematically fix filename inconsistencies across the Jekyll site.
"""

import os
import re
import shutil
from pathlib import Path

def fix_talk_filenames():
    """Fix talk filename issues: double dashes and truncated words."""
    talks_dir = Path("_talks")
    fixes = []
    
    # Common truncation fixes - be more careful with boundaries
    def fix_truncations(filename):
        """Fix truncated words in filename"""
        # Only fix if it's clearly truncated (ends with word)
        if 'learni-' in filename or filename.endswith('learni.md'):
            filename = filename.replace('learni', 'learning')
        if 'evaluatio-' in filename or filename.endswith('evaluatio.md'):
            filename = filename.replace('evaluatio', 'evaluation')
        if 'recommende-' in filename or filename.endswith('recommende.md'):
            filename = filename.replace('recommende', 'recommender')
        if 'transpar-' in filename or filename.endswith('transpar.md'):
            filename = filename.replace('transpar', 'transparency')
        return filename
    
    for file_path in talks_dir.glob("*.md"):
        old_name = file_path.name
        new_name = old_name
        
        # Fix double dashes
        new_name = re.sub(r'--(\d{4})', r'-\1', new_name)
        
        # Fix truncated words
        new_name = fix_truncations(new_name)
        
        if new_name != old_name:
            new_path = talks_dir / new_name
            fixes.append((file_path, new_path, old_name, new_name))
    
    return fixes

def fix_publication_filenames():
    """Standardize publication filenames to lastname+year format."""
    pubs_dir = Path("_publications")
    fixes = []
    
    for file_path in pubs_dir.glob("*.md"):
        old_name = file_path.name
        new_name = old_name
        
        # Convert underscore format to consistent format
        # schuth_2015_extended.md -> schuth2015extended.md
        if '_' in old_name and not old_name.startswith('overview_'):
            # Extract components
            parts = old_name.replace('.md', '').split('_')
            if len(parts) >= 2 and parts[1].isdigit():
                # lastname_year_keyword -> lastnameYEARkeyword
                new_name = ''.join(parts) + '.md'
        
        if new_name != old_name:
            new_path = pubs_dir / new_name
            fixes.append((file_path, new_path, old_name, new_name))
    
    return fixes

def fix_asset_names():
    """Standardize asset naming conventions."""
    assets_dir = Path("assets")
    fixes = []
    
    for file_path in assets_dir.glob("*.pdf"):
        old_name = file_path.name
        new_name = old_name
        
        # Normalize spacing and capitalization issues
        # Remove multiple spaces, normalize case
        new_name = re.sub(r'\s+', '-', new_name)
        new_name = re.sub(r'[_\s]+', '-', new_name)
        
        # Fix common issues like double extensions
        new_name = new_name.replace('..', '.')
        
        if new_name != old_name:
            new_path = assets_dir / new_name
            fixes.append((file_path, new_path, old_name, new_name))
    
    return fixes

def update_references(old_filename, new_filename, content_dirs):
    """Update references to renamed files in all content."""
    old_base = old_filename.replace('.md', '')
    new_base = new_filename.replace('.md', '')
    
    for content_dir in content_dirs:
        for file_path in Path(content_dir).glob("*.md"):
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Update various reference patterns
                updated = content
                updated = updated.replace(f'/{old_base})', f'/{new_base})')
                updated = updated.replace(f'/{old_base}.html)', f'/{new_base}.html)')
                updated = updated.replace(f'publication_url: {old_base}', f'publication_url: {new_base}')
                
                if updated != content:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(updated)
                    print(f"Updated references in {file_path}")
                        
            except Exception as e:
                print(f"Error updating {file_path}: {e}")

def add_redirects(old_filename, new_filename, content_type):
    """Add Jekyll redirects to renamed files."""
    if content_type == 'talks':
        old_url = f"/talks/{old_filename.replace('.md', '.html')}"
    elif content_type == 'publications':
        old_url = f"/publications/{old_filename.replace('.md', '.html')}"
    else:
        return
    
    new_file_path = Path(f"_{content_type}") / new_filename
    
    try:
        with open(new_file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Add redirect_from to frontmatter
        if 'redirect_from:' not in content:
            # Find end of frontmatter
            parts = content.split('---', 2)
            if len(parts) >= 3:
                frontmatter = parts[1]
                body = parts[2]
                
                # Add redirect
                frontmatter += f"\nredirect_from: {old_url}\n"
                
                new_content = f"---{frontmatter}---{body}"
                
                with open(new_file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                
                print(f"Added redirect {old_url} -> {new_file_path}")
    
    except Exception as e:
        print(f"Error adding redirect to {new_file_path}: {e}")

def main():
    """Run all fixes."""
    print("=== FILENAME CLEANUP SCRIPT ===\n")
    
    # Get all proposed fixes
    talk_fixes = fix_talk_filenames()
    pub_fixes = fix_publication_filenames()
    asset_fixes = fix_asset_names()
    
    print(f"Found {len(talk_fixes)} talk files to fix")
    print(f"Found {len(pub_fixes)} publication files to fix") 
    print(f"Found {len(asset_fixes)} asset files to fix")
    
    # Show proposed changes
    print("\n=== PROPOSED TALK CHANGES ===")
    for old_path, new_path, old_name, new_name in talk_fixes:
        print(f"{old_name} -> {new_name}")
    
    print("\n=== PROPOSED PUBLICATION CHANGES ===")
    for old_path, new_path, old_name, new_name in pub_fixes:
        print(f"{old_name} -> {new_name}")
    
    print("\n=== PROPOSED ASSET CHANGES ===")
    for old_path, new_path, old_name, new_name in asset_fixes[:10]:  # Show first 10
        print(f"{old_name} -> {new_name}")
    if len(asset_fixes) > 10:
        print(f"... and {len(asset_fixes) - 10} more")
    
    # Auto-proceed for script execution
    print("\nProceeding with fixes...")
    
    if len(talk_fixes) == 0 and len(pub_fixes) == 0:
        print("No fixes needed!")
        return
    
    # Apply talk fixes
    print("\n=== APPLYING TALK FIXES ===")
    for old_path, new_path, old_name, new_name in talk_fixes:
        try:
            shutil.move(str(old_path), str(new_path))
            print(f"Renamed: {old_name} -> {new_name}")
            
            # Update references
            update_references(old_name, new_name, ['_talks', '_publications', '_posts'])
            
            # Add redirect
            add_redirects(old_name, new_name, 'talks')
            
        except Exception as e:
            print(f"Error renaming {old_name}: {e}")
    
    # Apply publication fixes
    print("\n=== APPLYING PUBLICATION FIXES ===")
    for old_path, new_path, old_name, new_name in pub_fixes:
        try:
            shutil.move(str(old_path), str(new_path))
            print(f"Renamed: {old_name} -> {new_name}")
            
            # Update references
            update_references(old_name, new_name, ['_talks', '_publications', '_posts'])
            
            # Add redirect
            add_redirects(old_name, new_name, 'publications')
            
        except Exception as e:
            print(f"Error renaming {old_name}: {e}")
    
    print("\n=== CLEANUP COMPLETE ===")
    print("Note: Asset fixes require manual review - run asset cleanup separately")

if __name__ == "__main__":
    main()