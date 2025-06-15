#!/usr/bin/env python3
"""
Complete analysis of naming inconsistencies across the site.
"""

from pathlib import Path
import re

def analyze_publication_naming():
    """Analyze publication filename patterns."""
    pubs_dir = Path("_publications")
    patterns = {
        'underscore_year': [],      # schuth_2015_overview
        'year_attached': [],        # schuth2015overview  
        'dash_year': [],           # schuth-2015-overview
        'mixed': [],               # other patterns
    }
    
    for file_path in pubs_dir.glob("*.md"):
        name = file_path.stem
        
        if re.match(r'^\w+_\d{4}_\w+', name):
            patterns['underscore_year'].append(name)
        elif re.match(r'^\w+\d{4}\w+', name):
            patterns['year_attached'].append(name)
        elif re.match(r'^\w+-\d{4}-\w+', name):
            patterns['dash_year'].append(name)
        else:
            patterns['mixed'].append(name)
    
    return patterns

def analyze_talk_naming():
    """Analyze talk filename patterns."""
    talks_dir = Path("_talks")
    patterns = {
        'long_descriptive': [],     # multileave-gradient-descent-for-fast-online-learning-2015
        'short_descriptive': [],    # ai-validation-team-2024
        'issues': []               # problematic names
    }
    
    for file_path in talks_dir.glob("*.md"):
        name = file_path.stem
        
        if len(name) > 60:
            patterns['long_descriptive'].append(name)
        elif any(word in name for word in ['learni-', 'evaluatio-', 'recommende-']):
            patterns['issues'].append(name)
        else:
            patterns['short_descriptive'].append(name)
    
    return patterns

def find_key_inconsistencies():
    """Find key field inconsistencies."""
    inconsistencies = []
    
    # Check publications
    for file_path in Path("_publications").glob("*.md"):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            key_match = re.search(r'key:\s*([^\n]+)', content)
            if key_match:
                key = key_match.group(1).strip()
                filename = file_path.stem
                
                # Key should match filename
                if key != filename:
                    inconsistencies.append({
                        'file': str(file_path),
                        'filename': filename,
                        'key': key,
                        'type': 'publication'
                    })
        except:
            continue
    
    # Check talks
    for file_path in Path("_talks").glob("*.md"):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            key_match = re.search(r'key:\s*([^\n]+)', content)
            if key_match:
                key = key_match.group(1).strip()
                filename = file_path.stem
                
                if key != filename:
                    inconsistencies.append({
                        'file': str(file_path),
                        'filename': filename,
                        'key': key,
                        'type': 'talk'
                    })
        except:
            continue
    
    return inconsistencies

def main():
    """Run complete naming analysis."""
    print("📊 COMPLETE NAMING ANALYSIS")
    print("=" * 50)
    
    # Publication patterns
    pub_patterns = analyze_publication_naming()
    print("\n📚 PUBLICATION NAMING PATTERNS:")
    for pattern, files in pub_patterns.items():
        print(f"  {pattern}: {len(files)} files")
        if files and len(files) < 10:  # Show examples for smaller groups
            for f in files[:3]:
                print(f"    • {f}")
    
    # Talk patterns  
    talk_patterns = analyze_talk_naming()
    print("\n🎤 TALK NAMING PATTERNS:")
    for pattern, files in talk_patterns.items():
        print(f"  {pattern}: {len(files)} files")
        if files and pattern == 'issues':
            for f in files:
                print(f"    • {f}")
    
    # Key inconsistencies
    key_issues = find_key_inconsistencies()
    print(f"\n🔑 KEY FIELD INCONSISTENCIES: {len(key_issues)}")
    for issue in key_issues:
        print(f"  {issue['file']}")
        print(f"    filename: {issue['filename']}")
        print(f"    key:      {issue['key']}")
    
    # Recommendations
    print("\n💡 RECOMMENDATIONS:")
    print("1. PUBLICATIONS: Standardize to 'lastname+year+keyword' format")
    print("   Examples: schuth2015overview, hofmann2013reusing")
    print("2. TALKS: Keep descriptive names but fix truncations")
    print("3. KEYS: Must always match filename exactly")
    print("4. Target: 100% working links, 0 inconsistencies")

if __name__ == "__main__":
    main()