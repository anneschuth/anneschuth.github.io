#!/usr/bin/env python3
"""
Comprehensive fix for ALL naming inconsistencies.
Makes everything 100% consistent.
"""

import os
import re
import shutil
from pathlib import Path

# PHASE 1: Fix remaining publication naming
PUBLICATION_RENAMES = {
    'hofmann_2013_reusing.md': 'hofmann2013reusing.md',
    'hofmann_reusing_2013_dir.md': 'hofmann2013reusingdir.md',
    'overview_inex_2012.md': 'overview2012inex.md',
    'chuklin_evaluating_2013.md': 'chuklin2013evaluating.md',
}

# PHASE 2: Fix key inconsistencies
KEY_FIXES = {
    'hofmann2014sigweb.md': 'hofmann2014sigweb'  # Fix the key to match filename
}

# PHASE 3: Link reference updates
LINK_MAPPING = {
    # Old -> New publication keys
    'hofmann_2013_reusing': 'hofmann2013reusing',
    'hofmann_reusing_2013_dir': 'hofmann2013reusingdir', 
    'overview_inex_2012': 'overview2012inex',
    'chuklin_evaluating_2013': 'chuklin2013evaluating',
    'hofmann-2013-reusing': 'hofmann2013reusing',
    'chuklin-evaluating-2013': 'chuklin2013evaluating',
    'schuth-2015-overview': 'schuth2015overview',
}

def fix_publication_filenames():
    """Rename publication files to consistent format."""
    fixes = []
    
    for old_name, new_name in PUBLICATION_RENAMES.items():
        old_path = Path("_publications") / old_name
        new_path = Path("_publications") / new_name
        
        if old_path.exists():
            # Rename file
            shutil.move(str(old_path), str(new_path))
            print(f"Renamed: {old_name} -> {new_name}")
            fixes.append((old_name, new_name))
            
            # Update key field in the file
            old_key = old_name.replace('.md', '')
            new_key = new_name.replace('.md', '')
            
            with open(new_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Update key field
            content = re.sub(r'key:\s*' + re.escape(old_key), f'key: {new_key}', content)
            
            # Add redirect
            if 'redirect_from:' not in content:
                # Find end of frontmatter and add redirect
                parts = content.split('---', 2)
                if len(parts) >= 3:
                    frontmatter = parts[1]
                    body = parts[2]
                    frontmatter += f"\nredirect_from: /publications/{old_key}.html\n"
                    content = f"---{frontmatter}---{body}"
            
            with open(new_path, 'w', encoding='utf-8') as f:
                f.write(content)
    
    return fixes

def fix_key_inconsistencies():
    """Fix key fields that don't match filenames."""
    fixes = []
    
    for filename, correct_key in KEY_FIXES.items():
        file_path = Path("_publications") / filename
        
        if file_path.exists():
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Replace the key field
            content = re.sub(r'key:\s*[^\n]+', f'key: {correct_key}', content)
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f"Fixed key in: {filename}")
            fixes.append(filename)
    
    return fixes

def update_all_references():
    """Update all references to use new naming."""
    updated_files = []
    
    # Search all content directories
    for content_dir in ['_publications', '_talks', '_posts']:
        dir_path = Path(content_dir)
        if not dir_path.exists():
            continue
            
        for file_path in dir_path.glob("*.md"):
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                original_content = content
                
                # Update all link mappings
                for old_ref, new_ref in LINK_MAPPING.items():
                    # Various link formats
                    content = content.replace(f'/publications/{old_ref})', f'/publications/{new_ref})')
                    content = content.replace(f'/publications/{old_ref}.html)', f'/publications/{new_ref}.html)')
                    content = content.replace(f'publication_url: {old_ref}', f'publication_url: {new_ref}')
                    content = content.replace(f'/publications/{old_ref}]', f'/publications/{new_ref}]')
                    content = content.replace(f'/publications/{old_ref}.html]', f'/publications/{new_ref}.html]')
                
                if content != original_content:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(content)
                    updated_files.append(str(file_path))
                    print(f"Updated references in: {file_path}")
                    
            except Exception as e:
                print(f"Error updating {file_path}: {e}")
    
    return updated_files

def check_remaining_issues():
    """Check what issues remain after fixes."""
    print("\n🔍 CHECKING REMAINING ISSUES...")
    
    # Check for remaining underscore files
    underscore_files = []
    for file_path in Path("_publications").glob("*.md"):
        if '_' in file_path.stem and not file_path.stem.startswith('overview'):
            underscore_files.append(file_path.name)
    
    if underscore_files:
        print(f"❌ Still have {len(underscore_files)} underscore files:")
        for f in underscore_files:
            print(f"   • {f}")
    else:
        print("✅ No underscore files remaining")
    
    # Check key consistency
    key_issues = []
    for file_path in Path("_publications").glob("*.md"):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            key_match = re.search(r'key:\s*([^\n]+)', content)
            if key_match:
                key = key_match.group(1).strip()
                filename = file_path.stem
                
                if key != filename:
                    key_issues.append(f"{filename} -> key: {key}")
        except:
            continue
    
    if key_issues:
        print(f"❌ Still have {len(key_issues)} key mismatches:")
        for issue in key_issues:
            print(f"   • {issue}")
    else:
        print("✅ All keys match filenames")

def main():
    """Run comprehensive naming fixes."""
    print("🔧 COMPREHENSIVE NAMING FIX")
    print("=" * 50)
    
    print("\n📚 Phase 1: Fix publication filenames...")
    pub_fixes = fix_publication_filenames()
    print(f"Fixed {len(pub_fixes)} publication files")
    
    print("\n🔑 Phase 2: Fix key inconsistencies...")
    key_fixes = fix_key_inconsistencies()
    print(f"Fixed {len(key_fixes)} key fields")
    
    print("\n🔗 Phase 3: Update all references...")
    ref_updates = update_all_references()
    print(f"Updated references in {len(ref_updates)} files")
    
    print("\n🔍 Phase 4: Check remaining issues...")
    check_remaining_issues()
    
    print("\n✅ COMPREHENSIVE FIX COMPLETE!")
    print("Run the link checker to verify 100% success rate.")

if __name__ == "__main__":
    main()