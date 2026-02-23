import os
import re

loc_dir = "localisation"
eng_file = os.path.join(loc_dir, "plus_cs_events_l_english.yml")
target_files = [
    "plus_cs_l_french.yml", "plus_cs_l_german.yml", "plus_cs_l_spanish.yml", 
    "plus_cs_l_braz_por.yml", "plus_cs_l_polish.yml", "plus_cs_l_japanese.yml", 
    "plus_cs_l_simp_chinese.yml"
]

missing_keys = [
    "plus_cs.250.t", "plus_cs.250.d", "plus_cs.250.a", "plus_cs.250.b", "plus_cs.250.c", "plus_cs.250.d",
    "plus_cs_internal.14.t", "plus_cs_internal.14.d", "plus_cs_internal.14.a",
    "plus_cs_internal.15.t", "plus_cs_internal.15.d", "plus_cs_internal.15.a"
]

# Read english translations
translations = {}
with open(eng_file, "r", encoding="utf-8-sig") as f:
    for line in f:
        for key in missing_keys:
            if line.strip().startswith(key + ":0"):
                translations[key] = line

# Append to all target languages
for filename in target_files:
    filepath = os.path.join(loc_dir, filename)
    if os.path.exists(filepath):
        with open(filepath, "a", encoding="utf-8-sig") as f:
            f.write("\n")
            for key in missing_keys:
                if key in translations:
                    f.write(translations[key])
        print(f"Appended keys to {filename}")
