#!/usr/bin/env python3
"""
Check YAML frontmatter in Jekyll content files.
"""

import yaml
import sys
from pathlib import Path

def check_yaml_frontmatter(file_path):
    """Check if YAML frontmatter is valid."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        if content.startswith('---'):
            parts = content.split('---', 2)
            if len(parts) >= 2:
                yaml.safe_load(parts[1])
    except Exception as e:
        print(f'YAML error in {file_path}: {e}')
        return False
    return True

def main():
    """Check YAML in all content files."""
    errors = 0
    for content_dir in ['_publications', '_talks', '_posts']:
        dir_path = Path(content_dir)
        if dir_path.exists():
            for file_path in dir_path.glob('*.md'):
                if not check_yaml_frontmatter(file_path):
                    errors += 1

    sys.exit(1 if errors > 0 else 0)

if __name__ == "__main__":
    main()
