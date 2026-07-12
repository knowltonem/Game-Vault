import json, re, os

dump_path = r'C:\Users\edwar\.local\share\opencode\tool-output\tool_f3d36d723001PS4NkgZB5yC5l1'
legacy_dir = r'C:\Users\edwar\Documents\games\board-game-vault\games\arkham-lcg\legacy'

with open(dump_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

player_types = ['investigator', 'asset', 'event', 'skill']

standalone_packs = [
    'blbe', 'btb', 'enc', 'aon', 'bad', 'rod',
    'hoth', 'tftbw', 'bob', 'dre', 'otr', 'ptr',
    'rop', 'hfa', 'pap', 'aof', 'tdg', 'ltr', 'rtr'
]

cards = [c for c in data if c.get('pack_code') in standalone_packs and c.get('type_code') in player_types]

# Sort by pack order, then position
pack_order = {p: i for i, p in enumerate(standalone_packs)}
cards.sort(key=lambda c: (pack_order.get(c.get('pack_code'), 99), c.get('position', 999)))

def safe_str(val):
    if val is None or val == '' or val == 'None':
        return '\u2014'
    return str(val)

def fmt_traits(card):
    t = card.get('real_traits') or card.get('traits') or ''
    t = re.sub(r'<[^>]+>', '', t)
    t = t.strip().strip('.').strip()
    return t if t else '\u2014'

def fmt_icons(card):
    icons = []
    for sk, label in [('skill_willpower','wil'),('skill_intellect','int'),('skill_combat','com'),('skill_agility','agi'),('skill_wild','wild')]:
        v = card.get(sk, 0) or 0
        if v:
            icons.append(f'{v} \u00d7 <{label}>')
    return ', '.join(icons) if icons else '\u2014'

def fmt_rules(card):
    text = card.get('real_text') or card.get('text') or ''
    text = re.sub(r'<[^>]+>', '', text)
    return text if text.strip() else '\u2014'

def fmt_slot(card):
    s = card.get('real_slot') or card.get('slot') or ''
    if not s or s == 'None':
        return '\u2014'
    return s.replace('Hand x2', 'Two Hands')

def fmt_subtype(card):
    st = card.get('subtype_name') or ''
    return st if st else '\u2014'

def fmt_flavor(card):
    f = card.get('flavor') or ''
    f = re.sub(r'<[^>]+>', '', f)
    return f if f.strip() else '\u2014'

lines = []
lines.append('# Player Cards \u2014 Standalone Scenarios')
lines.append('')
lines.append('Cards in this file are from the ArkhamDB API dump and formatted for Strange Eons.')
lines.append('')
lines.append('---')

for card in cards:
    code = card.get('code', '?????')
    name = card.get('real_name') or card.get('name') or '???'
    subtype = card.get('subname') or ''
    qty = ''
    if card.get('quantity', 1) > 1 and card.get('type_code') != 'investigator':
        qty = f' (\u00d7{card["quantity"]})'
    subtitle_part = f' \u2014 {subtype}' if subtype else ''

    lines.append(f'### {code} \u2014 {name}{subtitle_part}{qty}')
    lines.append('')

    fields = [
        ('Card Number', code),
        ('Set', card.get('pack_code', '???')),
        ('Name', name),
        ('Subtitle', subtype if subtype else '\u2014'),
        ('Type', card.get('type_name', '???')),
        ('Subtype', fmt_subtype(card)),
        ('Class', card.get('faction_name', '???').lower()),
        ('Level', str(card.get('xp', 0))),
        ('Unique', 'Yes' if card.get('is_unique') else 'No'),
        ('Cost', str(card.get('cost', '')) if card.get('cost') is not None else '\u2014'),
        ('Slot', fmt_slot(card)),
        ('Traits', fmt_traits(card)),
    ]
    if card.get('type_code') == 'investigator' or card.get('health') is not None or card.get('sanity') is not None:
        fields.append(('HP Soak', str(card.get('health', '')) if card.get('health') is not None else '\u2014'))
        fields.append(('SAN Soak', str(card.get('sanity', '')) if card.get('sanity') is not None else '\u2014'))
    fields.append(('Icons', fmt_icons(card)))
    fields.append(('Rules Text', fmt_rules(card)))
    fields.append(('Flavor', fmt_flavor(card)))
    fields.append(('Copyright', 'RYP-NW \u00a9 2026'))

    for label, value in fields:
        lines.append(f'**{label}**')
        lines.append('```')
        lines.append(value)
        lines.append('```')

    lines.append('---')

outpath = os.path.join(legacy_dir, 'Standalone-Player-Cards.md')
with open(outpath, 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))
print(f'Written {len(cards)} cards to {outpath}')
