# -*- coding: utf-8 -*-
"""
Localization Audit Script for HOI4 Mod
Checks if all localization keys are present in all language files.
"""

import os
import re
from pathlib import Path
from collections import defaultdict

# Languages in HOI4
LANGUAGES = {
    'english': ['plus_cs_events_l_english.yml', 'plus_cs_ideas_l_english.yml', 
                'plus_cs_decisions_l_english.yml', 'plus_cs_countries_cosmetic_l_english.yml'],
    'russian': ['plus_cs_l_russian.yml'],
    'french': ['plus_cs_l_french.yml'],
    'german': ['plus_cs_l_german.yml'],
    'spanish': ['plus_cs_l_spanish.yml'],
    'braz_por': ['plus_cs_l_braz_por.yml'],
    'polish': ['plus_cs_l_polish.yml'],
    'japanese': ['plus_cs_l_japanese.yml'],
    'simp_chinese': ['plus_cs_l_simp_chinese.yml']
}

LOC_DIR = Path(__file__).parent / 'localisation'


def extract_keys_from_file(filepath):
    """Extract all localization keys from a .yml file."""
    keys = set()
    try:
        with open(filepath, 'r', encoding='utf-8-sig') as f:
            content = f.read()
    except UnicodeDecodeError:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    
    # Match pattern: key:0 "value" or key: "value"
    # HOI4 uses format: key_name:0 "localized string"
    pattern = r'^\s*([a-zA-Z0-9_\.]+):\d*\s+"'
    for line in content.split('\n'):
        line = line.replace('\ufeff', '') # Handle potential BOMs in the middle
        match = re.match(pattern, line)
        if match:
            key = match.group(1)
            # Skip language header
            if not key.startswith('l_'):
                keys.add(key)
    return keys


def get_all_english_keys():
    """Get all keys from English localization files."""
    all_keys = set()
    for filename in LANGUAGES['english']:
        filepath = LOC_DIR / filename
        if filepath.exists():
            keys = extract_keys_from_file(filepath)
            all_keys.update(keys)
    return all_keys


def get_language_keys(lang):
    """Get all keys from a specific language's files."""
    all_keys = set()
    for filename in LANGUAGES.get(lang, []):
        filepath = LOC_DIR / filename
        if filepath.exists():
            keys = extract_keys_from_file(filepath)
            all_keys.update(keys)
    return all_keys


def find_used_keys_in_scripts():
    """Find all localization keys used in script files."""
    used_keys = set()
    script_dirs = [
        Path(__file__).parent / 'events',
        Path(__file__).parent / 'common' / 'decisions',
        Path(__file__).parent / 'common' / 'ideas',
        Path(__file__).parent / 'common' / 'scripted_effects',
        Path(__file__).parent / 'common' / 'on_actions',
        Path(__file__).parent / 'common' / 'dynamic_modifiers',
        Path(__file__).parent / 'common' / 'opinion_modifiers',
    ]
    
    # Patterns to find localization keys in scripts
    patterns = [
        r'title\s*=\s*([a-zA-Z0-9_\.]+)',
        r'desc\s*=\s*([a-zA-Z0-9_\.]+)',
        r'name\s*=\s*([a-zA-Z0-9_\.]+)',
        r'text\s*=\s*([a-zA-Z0-9_\.]+)',
        r'custom_tooltip\s*=\s*([a-zA-Z0-9_\.]+)',
        r'custom_effect_tooltip\s*=\s*([a-zA-Z0-9_\.]+)',
        r'localisation_key\s*=\s*"?([a-zA-Z0-9_\.]+)"?',
        r'icon\s*=\s*"?([a-zA-Z0-9_]+)"?',  # Ideas often use name as icon
    ]
    
    for script_dir in script_dirs:
        if not script_dir.exists():
            continue
        for filepath in script_dir.rglob('*.txt'):
            try:
                with open(filepath, 'r', encoding='utf-8-sig') as f:
                    content = f.read()
            except:
                continue
            
            for pattern in patterns:
                matches = re.findall(pattern, content)
                for match in matches:
                    if match and not match.startswith('{') and 'ROOT' not in match and 'FROM' not in match:
                        used_keys.add(match)
    
    return used_keys


def main():
    print("=" * 80)
    print("HOI4 MOD LOCALIZATION AUDIT")
    print("=" * 80)
    print()
    
    # Get English keys (master list)
    english_keys = get_all_english_keys()
    print(f"Total English keys found: {len(english_keys)}")
    print()
    
    # Check each language
    missing_report = {}
    extra_report = {}
    
    for lang in LANGUAGES:
        if lang == 'english':
            continue
        
        lang_keys = get_language_keys(lang)
        missing = english_keys - lang_keys
        extra = lang_keys - english_keys
        
        if missing or extra:
            missing_report[lang] = missing
            extra_report[lang] = extra
    
    # Print missing keys report
    print("=" * 80)
    print("MISSING KEYS BY LANGUAGE (keys in English but not in language)")
    print("=" * 80)
    
    for lang, missing in missing_report.items():
        if missing:
            print(f"\n--- {lang.upper()} ({len(missing)} missing) ---")
            for key in sorted(missing)[:50]:  # Limit output
                print(f"  - {key}")
            if len(missing) > 50:
                print(f"  ... and {len(missing) - 50} more")
    
    # Print extra keys report
    print()
    print("=" * 80)
    print("EXTRA KEYS BY LANGUAGE (keys in language but not in English)")
    print("=" * 80)
    
    for lang, extra in extra_report.items():
        if extra and len(extra) < 20:  # Only show if not too many (likely just different structure)
            print(f"\n--- {lang.upper()} ({len(extra)} extra) ---")
            for key in sorted(extra):
                print(f"  + {key}")
    
    # Summary
    print()
    print("=" * 80)
    print("SUMMARY")
    print("=" * 80)
    
    all_complete = True
    for lang in LANGUAGES:
        if lang == 'english':
            continue
        lang_keys = get_language_keys(lang)
        missing_count = len(english_keys - lang_keys)
        coverage = ((len(english_keys) - missing_count) / len(english_keys)) * 100 if english_keys else 100
        # FIXED: Removed unicode characters to prevent output encoding errors in Windows console
        status = "[OK] COMPLETE" if missing_count == 0 else f"[MISSING] {missing_count}"
        print(f"  {lang.upper():15} - {len(lang_keys):4} keys - {coverage:5.1f}% coverage - {status}")
        if missing_count > 0:
            all_complete = False
    
    if all_complete:
        print("\n[OK] All languages have complete localization!")
    else:
        print("\n[FAIL] Some languages are missing localization keys.")
    
    # Check for keys used in scripts but not in localization
    print()
    print("=" * 80)
    print("SCRIPT KEY ANALYSIS")
    print("=" * 80)
    
    script_keys = find_used_keys_in_scripts()
    
    # Only keep keys that look like mod keys
    relevant_prefixes = ('plus_cs', 'peace_', 'conditional_', 'white_peace', 'offer_', 'decision_category', 'decree_', 'stimulus_', 'shadow_', 'manpower_strain', 'officer_shortage', 'war_inflation', 'economic_retooling', 'rapid_', 'fight_', 'intervention_')
    
    missing_in_loc = set()
    
    for key in script_keys:
        if key in english_keys:
            continue
        
        # Check if it should be localized (based on prefix)
        if key.startswith(relevant_prefixes) or 'plus_cs' in key:
            missing_in_loc.add(key)
            
    if missing_in_loc:
        print(f"\nKeys used in scripts but missing from English localization ({len(missing_in_loc)}):")
        for key in sorted(missing_in_loc):
            print(f"  ! {key}")
    else:
        print("\n[OK] All relevant script keys have English localization!")


if __name__ == '__main__':
    main()
