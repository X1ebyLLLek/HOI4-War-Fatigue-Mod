import os
import re

loc_dir = r"C:\Users\Machenike\PyCharmMiscProject\hoi4\HOI4+War Fatigue Surrender\localisation"

english_keys = {}

# Read all english files
for filename in os.listdir(loc_dir):
    if filename.endswith("l_english.yml"):
        filepath = os.path.join(loc_dir, filename)
        with open(filepath, 'r', encoding='utf-8-sig') as f:
            for line in f:
                match = re.search(r'^\s*([a-zA-Z0-9_\-\.]+):\d*\s*"(.*)"', line)
                if match:
                    key = match.group(1).strip()
                    val = match.group(2)
                    english_keys[key] = val

print(f"Total English keys found: {len(english_keys)}")

# For each other file
for filename in os.listdir(loc_dir):
    if filename.endswith(".yml") and "english" not in filename:
        filepath = os.path.join(loc_dir, filename)
        target_keys = set()
        with open(filepath, 'r', encoding='utf-8-sig') as f:
            for line in f:
                match = re.search(r'^\s*([a-zA-Z0-9_\-\.]+):\d*\s*".*"', line)
                if match:
                    target_keys.add(match.group(1).strip())
        
        missing = []
        for e_key in english_keys:
            if e_key not in target_keys:
                missing.append(e_key)
        
        if missing:
            print(f"--- {filename} is missing {len(missing)} keys ---")
            for m in missing:
                print(f"  {m}")
        else:
            print(f"--- {filename} is fully updated ---")
