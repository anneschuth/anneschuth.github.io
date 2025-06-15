#!/usr/bin/env python3
"""
Script to standardize shield/badge naming conventions.
"""

import os
import re
from pathlib import Path

def analyze_shield_patterns():
    """Analyze current shield patterns."""
    patterns = {
        'publications': {},
        'talks': {}
    }
    
    # Analyze publications
    for file_path in Path("_publications").glob("*.md"):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            shield_match = re.search(r'shield:\s*(.+)', content)
            if shield_match:
                shield = shield_match.group(1).strip()
                if shield in patterns['publications']:
                    patterns['publications'][shield] += 1
                else:
                    patterns['publications'][shield] = 1
        except:
            continue
    
    # Analyze talks
    for file_path in Path("_talks").glob("*.md"):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            shield_match = re.search(r'shield:\s*(.+)', content)
            if shield_match:
                shield = shield_match.group(1).strip()
                if shield in patterns['talks']:
                    patterns['talks'][shield] += 1
                else:
                    patterns['talks'][shield] = 1
        except:
            continue
    
    return patterns

def create_shield_mapping():
    """Create standardized shield mapping."""
    
    # Standard venue types and colors
    venue_mapping = {
        # Conferences - blue
        'SIGIR': 'conference-SIGIR-blue',
        'CIKM': 'conference-CIKM-blue', 
        'WSDM': 'conference-WSDM-blue',
        'ECIR': 'conference-ECIR-blue',
        'CLEF': 'conference-CLEF-blue',
        'TREC': 'conference-TREC-blue',
        
        # Workshops - green
        'workshop': 'workshop-green',
        
        # Journals - purple
        'journal': 'journal-purple',
        'TOIS': 'journal-TOIS-purple',
        
        # Talks - different colors by type
        'conference-talk': 'talk-conference-orange',
        'invited-talk': 'talk-invited-green',
        'internal-talk': 'talk-internal-gray',
        'tutorial': 'talk-tutorial-blue',
        
        # Thesis
        'phdthesis': 'thesis-phd-red',
        'masterthesis': 'thesis-masters-orange'
    }
    
    # Current shield -> standardized shield mapping
    shield_fixes = {}
    
    # Based on current patterns, create mappings
    patterns = analyze_shield_patterns()
    
    for shield in patterns['publications']:
        if 'SIGIR' in shield:
            shield_fixes[shield] = 'conference-SIGIR-blue'
        elif 'CIKM' in shield:
            shield_fixes[shield] = 'conference-CIKM-blue'
        elif 'WSDM' in shield:
            shield_fixes[shield] = 'conference-WSDM-blue'
        elif 'ECIR' in shield:
            shield_fixes[shield] = 'conference-ECIR-blue'
        elif 'CLEF' in shield:
            shield_fixes[shield] = 'conference-CLEF-blue'
        elif 'workshop' in shield.lower():
            # Extract venue name if possible
            if 'CIKM' in shield:
                shield_fixes[shield] = 'workshop-CIKM-green'
            else:
                shield_fixes[shield] = 'workshop-green'
        elif 'journal' in shield.lower() or 'TOIS' in shield:
            shield_fixes[shield] = 'journal-purple'
        elif 'phdthesis' in shield:
            shield_fixes[shield] = 'thesis-phd-red'
    
    for shield in patterns['talks']:
        if 'conference' in shield.lower():
            shield_fixes[shield] = 'talk-conference-orange'
        elif 'internal' in shield.lower():
            shield_fixes[shield] = 'talk-internal-gray'
        elif 'lightblue' in shield:
            shield_fixes[shield] = 'talk-invited-green'
        elif shield == 'talk':
            shield_fixes[shield] = 'talk-conference-orange'  # Default
    
    return shield_fixes

def apply_shield_fixes(shield_mapping):
    """Apply shield fixes to all content."""
    fixed_files = []
    
    # Fix publications
    for file_path in Path("_publications").glob("*.md"):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            updated_content = content
            for old_shield, new_shield in shield_mapping.items():
                if f'shield: {old_shield}' in content:
                    updated_content = updated_content.replace(
                        f'shield: {old_shield}', 
                        f'shield: {new_shield}'
                    )
            
            if updated_content != content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(updated_content)
                fixed_files.append(file_path)
                
        except Exception as e:
            print(f"Error fixing {file_path}: {e}")
    
    # Fix talks
    for file_path in Path("_talks").glob("*.md"):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            updated_content = content
            for old_shield, new_shield in shield_mapping.items():
                if f'shield: {old_shield}' in content:
                    updated_content = updated_content.replace(
                        f'shield: {old_shield}', 
                        f'shield: {new_shield}'
                    )
            
            if updated_content != content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(updated_content)
                fixed_files.append(file_path)
                
        except Exception as e:
            print(f"Error fixing {file_path}: {e}")
    
    return fixed_files

def main():
    """Run shield standardization."""
    print("=== SHIELD STANDARDIZATION SCRIPT ===\n")
    
    # Analyze current patterns
    patterns = analyze_shield_patterns()
    
    print("Current shield patterns:")
    print("\nPublications:")
    for shield, count in sorted(patterns['publications'].items()):
        print(f"  {shield}: {count} files")
    
    print("\nTalks:")
    for shield, count in sorted(patterns['talks'].items()):
        print(f"  {shield}: {count} files")
    
    # Create mapping
    shield_mapping = create_shield_mapping()
    
    print(f"\n=== PROPOSED SHIELD CHANGES ===")
    for old_shield, new_shield in shield_mapping.items():
        if old_shield != new_shield:
            print(f"{old_shield}")
            print(f"  -> {new_shield}")
    
    if not shield_mapping:
        print("No shield fixes needed!")
        return
    
    # Ask for confirmation
    response = input("\nProceed with shield standardization? (y/N): ")
    if response.lower() != 'y':
        print("Aborted.")
        return
    
    # Apply fixes
    print("\n=== APPLYING SHIELD FIXES ===")
    fixed_files = apply_shield_fixes(shield_mapping)
    
    print(f"Updated shields in {len(fixed_files)} files")
    for file_path in fixed_files:
        print(f"  {file_path}")
    
    print("\n=== SHIELD STANDARDIZATION COMPLETE ===")

if __name__ == "__main__":
    main()