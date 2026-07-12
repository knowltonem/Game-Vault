import json, os, re

dump_path = r'C:\Users\edwar\.local\share\opencode\tool-output\tool_f3d36d723001PS4NkgZB5yC5l1'
legacy_dir = r'C:\Users\edwar\Documents\games\board-game-vault\games\arkham-lcg\legacy'

with open(dump_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

player_types = ['investigator', 'asset', 'event', 'skill']

# Check all legacy files for coverage
files = [f for f in os.listdir(legacy_dir) if f.endswith('-Player-Cards.md')]
for fname in sorted(files):
    path = os.path.join(legacy_dir, fname)
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    packs_in_file = {}
    for i, line in enumerate(lines):
        s = line.strip()
        if s == '**Set**' and i+2 < len(lines):
            pc = lines[i+2].strip()
            if len(pc) <= 5 and pc != '```':
                packs_in_file[pc] = packs_in_file.get(pc, 0) + 1
    
    total = sum(packs_in_file.values())
    
    # Show pack names
    pack_names = {}
    for pc in packs_in_file:
        pn = next((c.get('pack_name') for c in data if c.get('pack_code') == pc), pc)
        pack_names[pc] = pn
    
    print(f'{fname}')
    print(f'  Total cards: {total}')
    print(f'  Packs:')
    for pc, cnt in sorted(packs_in_file.items()):
        print(f'    {pc} ({pack_names[pc]}): {cnt}')
    print()
