"""
Arkham Horror LCG — Verbose Display Simulator
Eleanor Heart + Ironhide vs Midnight Masks

Full round-by-round display format:
- Setup Phase: card draws shown numbered, weaknesses flagged
- Each round: actions numbered, tokens shown, results clear
- Upkeep: card draws shown
- Mythos: encounter cards and results shown

Rules applied:
- Round 1: Investigation + Upkeep only (no Mythos, no Enemy, no encounters)
- No weakness in opening hand (set aside, replaced, shuffled back)
- Permanents in play at setup
- Asset plays cost 1 action
- Exhausted enemies skip attack, ready in Upkeep
- 1 encounter card per investigator per Mythos (2 total)
- Hand size limit: 8
"""
import random

CHAOS_BAG_BASE = [1,1,0,0,-1,-1,-2,-3,'skull','skull','cultist','autofail','eldersign']
WEAKNESSES = {'Echoes of Rlyeh','Fog of Innsmouth','Church in Flames','Basic Weakness'}

ENCOUNTER_POOL = (
    ['Rotting Remains']*3+['Frozen in Fear']*2+['Grasping Hands']*3+
    ['Dissonant Voices']*2+['Obscuring Fog']*2+['Mysterious Chanting']*2+
    ['On Wings of Darkness']*1+['Unholy Pact']*1
)
TREACHERIES = {
    'Rotting Remains':     {'type':'wil','diff':4,'fail_hor':2},
    'Frozen in Fear':      {'type':'wil','diff':4,'fail_hor':1},
    'Grasping Hands':      {'type':'agi','diff':3,'fail_dmg':2},
    'Dissonant Voices':    {'type':'wil','diff':3,'fail_hor':1},
    'Obscuring Fog':       {'type':'agi','diff':2,'fail_dmg':1},
    'Mysterious Chanting': {'type':'wil','diff':3,'fail_hor':1},
    'On Wings of Darkness':{'type':'agi','diff':4,'fail_dmg':2},
    'Unholy Pact':         {'type':'wil','diff':5,'fail_hor':3},
}
CULTISTS = [
    {'name':'Swarm of Rats','hp':1,'fight':1,'evade':3,'dmg':1,'hor':0,'hunter':False},
    {'name':'Acolyte','hp':1,'fight':1,'evade':3,'dmg':1,'hor':1,'hunter':False},
    {'name':'Acolyte','hp':1,'fight':1,'evade':3,'dmg':1,'hor':1,'hunter':False},
    {'name':'Conglomeration','hp':3,'fight':3,'evade':4,'dmg':1,'hor':2,'hunter':True},
    {'name':'Wizard of Yog','hp':4,'fight':4,'evade':4,'dmg':2,'hor':1,'hunter':True},
    {'name':'Cultist Sentry','hp':2,'fight':2,'evade':3,'dmg':1,'hor':1,'hunter':False},
]
LOCATIONS = [
    {'name':'Southside','shroud':2},{'name':'Downtown','shroud':3},
    {'name':'Easttown','shroud':2},{'name':'Merchant District','shroud':3},
    {'name':'Rivertown','shroud':2},{'name':'Miskatonic University','shroud':4},
    {'name':"St. Mary's Hospital",'shroud':3},{'name':'Woods','shroud':4},
]

IRONHIDE_DECK = (
    ['Kings Talon']*2+['Hound of the Deep']*2+['Luck of the Draw']*2+
    ['Father Thomas']*2+['Rlyeh Fury']*2+['Ill See You in Hell']*2+
    ['Cosmic Blast']*1+['On the Hunt']*1+['Antique Dealings']*2+
    ['Premonitions']*2+['Knowledge From the Deep']*2+['Ill Manage']*1+
    ['Aquinnah']*1+['Ward of Protection']*2+['Holy Water']*2+
    ['Overpower']*2+['Guts']*2
)
IRONHIDE_WEAK=['Echoes of Rlyeh']

ELEANOR_DECK = (
    ['Take What You Need']*2+['Special Allowance']*2+['Clarity of Mind']*2+
    ['Military Tactics']*2+['Arcane Practice']*2+['Triage']*2+['Patch Up']*2+
    ['Fort Warren Chapel']*2+['Shores of Innsmouth']*2+['Do No Harm']*2+
    ['The Codex Revealed']*2+['Innsmouth Lessons']*1+['Private Parker']*1+
    ['Father Rodriguez']*1+['Ward of Protection EL']*2+['Focused Mind']*2+
    ['The Undying Will']*1+['Medical Bag']*1
)
ELEANOR_WEAK=['Fog of Innsmouth']

def draw_token(bless,curse):
    return random.choice(CHAOS_BAG_BASE+['bless']*bless+['curse']*curse)

def resolve_token(token,bless,curse):
    if token=='bless':
        inner=draw_token(max(0,bless-1),curse)
        mod,sp=resolve_token(inner,max(0,bless-1),curse)
        return (-999,'autofail') if mod==-999 else (mod+2,sp)
    if token=='curse':
        inner=draw_token(bless,max(0,curse-1))
        mod,sp=resolve_token(inner,bless,max(0,curse-1))
        return (-999,'autofail') if mod==-999 else (mod-2,sp)
    if token=='eldersign': return 1,'eldersign'
    if token=='autofail': return -999,'autofail'
    if token in ('skull','cultist'): return -2,token
    return token,None

def skill_test(skill,diff,bless,curse,label=""):
    token=draw_token(bless,curse)
    mod,sp=resolve_token(token,bless,curse)
    if mod==-999: return False,-999,token,'autofail',sp
    eff=skill+mod; margin=eff-diff
    return margin>=0,margin,token,f"{skill}{mod:+d}={eff} vs {diff} ({'PASS' if margin>=0 else 'FAIL'} by {abs(margin)})",sp

def build_deck(cards,weaknesses=[]):
    d=cards.copy()+list(weaknesses); random.shuffle(d); return d

def draw_opening_hand(deck,size=5):
    """No weaknesses in opening hand -- set aside, replaced, shuffled back."""
    hand=[]; aside=[]; d=deck.copy()
    while len(hand)<size and d:
        c=d.pop()
        if c in WEAKNESSES: aside.append(c)
        else: hand.append(c)
    d.extend(aside); random.shuffle(d)
    return hand,d

def el_scale(dmg):
    """Eleanor healing scale: 0-2=1, 3-5=2, 6=3, 7=4"""
    if dmg>=7: return 4
    if dmg>=6: return 3
    if dmg>=3: return 2
    return 1

def print_hand(hand, label="Hand"):
    print(f"  {label}:")
    for i,c in enumerate(hand,1):
        print(f"    Card {i}: {c}")

def print_separator(char='-', width=60):
    print(char*width)

def print_stats(name, hp, hp_max, san, san_max, res, extra=""):
    print(f"  {name}: HP {hp}/{hp_max} | SAN {san}/{san_max} | Resources: {res}{extra}")
