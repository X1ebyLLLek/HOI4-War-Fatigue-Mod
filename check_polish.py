import os

filepath = r'localisation/plus_cs_l_polish.yml'
with open(filepath, 'rb') as f:
    text = f.read().decode('utf-8-sig')

lines = text.split('\n')
out_lines = []
for i, line in enumerate(lines):
    # check quotes count
    if line.strip() and not line.strip().startswith('#'):
        parts = line.split('0 ', 1)
        if len(parts) > 1:
            val = parts[1].strip()
            # If quotes inside aren't escaped or there are extra quotes
            if val.count('"') > 2:
                out_lines.append(f"Line {i+1} has >2 quotes: {repr(line.strip())}")
            if not val.startswith('"') or not val.endswith('"'):
                out_lines.append(f"Line {i+1} mismatched quotes: {repr(line.strip())}")

with open('check_polish_out.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(out_lines))
