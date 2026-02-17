import os
import re
from pathlib import Path

DECISIONS_DIR = Path("common/decisions")
LOC_FILE = Path("localisation/plus_cs_decisions_l_english.yml")

def get_loc_keys():
    keys = set()
    if not LOC_FILE.exists():
        return keys
    try:
        with open(LOC_FILE, 'r', encoding='utf-8-sig') as f:
            content = f.read()
    except UnicodeDecodeError:
         with open(LOC_FILE, 'r', encoding='utf-8') as f:
            content = f.read()
            
    for line in content.splitlines():
        line = line.strip()
        if ':' in line and not line.startswith('#'):
            key = line.split(':')[0].strip()
            keys.add(key)
    return keys

def find_categories():
    categories = set()
    # Scan main decisions folder
    for fpath in DECISIONS_DIR.glob("*.txt"):
        with open(fpath, 'r', encoding='utf-8-sig', errors='ignore') as f:
            content = f.read()
            # Match top-level keys: key = { ... }
            # We assume proper formatting where top-level keys are at start of line or minimal indent
            # But strict regex: ^\s*(\w+)\s*=\s*\{
            matches = re.finditer(r'^\s*(\w+)\s*=\s*\{', content, re.MULTILINE)
            for m in matches:
                cat = m.group(1)
                # Filter out standard keywords that might look like categories if file structure is loose
                if cat not in ['add_namespace', 'decision_category_crisis_management', 'decision_category_economic_stimulus']:
                    categories.add(cat)
                    
    # Scan categories folder if exists
    cat_dir = DECISIONS_DIR / "categories"
    if cat_dir.exists():
         for fpath in cat_dir.glob("*.txt"):
            with open(fpath, 'r', encoding='utf-8-sig', errors='ignore') as f:
                content = f.read()
                matches = re.finditer(r'^\s*(\w+)\s*=\s*\{', content, re.MULTILINE)
                for m in matches:
                    categories.add(m.group(1))
                    
    return categories

def main():
    loc_keys = get_loc_keys()
    categories = find_categories()
    
    print(f"Found {len(categories)} potential categories.")
    missing = []
    
    # Standard ignoring list (effects, known blocks) - adjust as needed
    ignore_list = [
        'if', 'limit', 'else', 'effect', 'modifier', 'ai_will_do', 
        'complete_effect', 'available', 'allowed', 'visible', 'target_trigger', 
        'fire_only_once', 'cost', 'days_remove', 'days_re_enable', 'cancel_trigger',
        'remove_effect', 'timeout_effect'
    ]
    
    for cat in categories:
        if cat in ignore_list:
            continue
        if cat not in loc_keys:
            missing.append(cat)
            
    if missing:
        print("Missing localization for:")
        for m in missing:
            print(f"- {m}")
    else:
        print("All categories appear to be localized.")

if __name__ == "__main__":
    main()
