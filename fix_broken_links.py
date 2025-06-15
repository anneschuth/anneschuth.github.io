#!/usr/bin/env python3
"""
Fix broken internal links found by link checker.
"""

import re
from pathlib import Path

# Mapping of old publication keys to new keys
PUBLICATION_KEY_MAPPING = {
    'schuth-lerot-2013': 'schuth2013lerot',
    'schuth-2015-extended': 'schuth2015extended',
    'schuth-2015-overview': 'schuth2015overview', 
    'schuth-2015-predicting': 'schuth2015predicting',
    'schuth-2015-probabilistic': 'schuth2015probabilistic',
    'schuth_2015_extended': 'schuth2015extended',
    'hofmann-2013-reusing': 'hofmann_2013_reusing',
    'chuklin-evaluating-2013': 'chuklin_evaluating_2013',
}

# Mapping of old talk keys to new keys  
TALK_KEY_MAPPING = {
    'automated-extraction-of-machine-executable-legisla-2025': 'automated-extraction-of-machine-executable-legislation-2025',
}

def fix_file_links(file_path):
    """Fix broken links in a single file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return False
    
    original_content = content
    
    # Fix publication links
    for old_key, new_key in PUBLICATION_KEY_MAPPING.items():
        # Fix various link formats
        content = content.replace(f'/publications/{old_key})', f'/publications/{new_key})')
        content = content.replace(f'/publications/{old_key}.html)', f'/publications/{new_key}.html)')
        content = content.replace(f'publication_url: {old_key}', f'publication_url: {new_key}')
        content = content.replace(f'/publications/{old_key}]', f'/publications/{new_key}]')
        content = content.replace(f'/publications/{old_key}.html]', f'/publications/{new_key}.html]')
    
    # Fix talk links
    for old_key, new_key in TALK_KEY_MAPPING.items():
        content = content.replace(f'/talks/{old_key})', f'/talks/{new_key})')
        content = content.replace(f'/talks/{old_key}.html)', f'/talks/{new_key}.html)')
        content = content.replace(f'/talks/{old_key}]', f'/talks/{new_key}]')
        content = content.replace(f'/talks/{old_key}.html]', f'/talks/{new_key}.html]')
    
    # Fix specific known issues
    # Remove WordPress-style image parameters
    content = re.sub(r'\?resize=\d+%2C\d+&ssl=1', '', content)
    
    # Save if changed
    if content != original_content:
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Fixed: {file_path}")
            return True
        except Exception as e:
            print(f"Error writing {file_path}: {e}")
            return False
    
    return False

def main():
    """Fix all broken links."""
    print("🔧 Fixing broken links...")
    
    base_path = Path("/Users/anneschuth/anneschuth.github.io")
    content_dirs = ['_publications', '_talks', '_posts']
    
    fixed_count = 0
    
    for content_dir in content_dirs:
        dir_path = base_path / content_dir
        if not dir_path.exists():
            continue
            
        for file_path in dir_path.glob("*.md"):
            if fix_file_links(file_path):
                fixed_count += 1
    
    print(f"✅ Fixed links in {fixed_count} files")

if __name__ == "__main__":
    main()