import os

loc_dir = r"C:\Users\Machenike\PyCharmMiscProject\hoi4\HOI4+War Fatigue Surrender\localisation"

english_tooltips = """
 plus_cs_demand_not_core_tt:0 "Target must control at least one of our Core or Claimed states."
 plus_cs_demand_not_at_war_tt:0 "Requires both nations to be at peace, without internal civil wars."
 plus_cs_demand_not_faction_tt:0 "Target cannot be our subject, overlord, or faction member."
 plus_cs_demand_no_recent_tt:0 "We have not sent a territory demand to them recently."
 plus_cs_demand_full_annexation_tt:0 "Target must have at least one state that is §RNOT§! our core. (We cannot annex their entire country peacefully)."
"""

files_to_update = [
    "plus_cs_l_braz_por.yml",
    "plus_cs_l_french.yml",
    "plus_cs_l_german.yml",
    "plus_cs_l_japanese.yml",
    "plus_cs_l_polish.yml",
    "plus_cs_l_simp_chinese.yml",
    "plus_cs_l_spanish.yml",
]

for filename in files_to_update:
    filepath = os.path.join(loc_dir, filename)
    with open(filepath, 'a', encoding='utf-8-sig') as f:
        f.write("\n # --- Missing Action Tooltips (Fallback to English) ---")
        f.write(english_tooltips)
        
print("Successfully appended missing tooltips to all 7 language files.")
