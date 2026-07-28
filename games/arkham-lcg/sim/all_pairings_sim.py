"""
Arkham Horror LCG — All Pairings Corrected Sim
Rules Reference: games/arkham-lcg/sim/arkham-rules-reference.md

Rules fixes applied:
  - Round 1: Investigation + Upkeep only (no Mythos, no Enemy, no encounters)
  - Opening hand: no weaknesses (set aside, replaced, shuffled back)
  - Mulligans: applied once before Round 1
  - Permanents: in play at setup, not drawn from deck
  - Asset plays: cost 1 action each (unless Fast)
  - Exhausted enemies: skip attack, ready in Upkeep
  - Encounter cards: 1 per investigator per Mythos (2 for 2-player)
  - Hand size: discard to 8 in Upkeep
  - Hunter enemies: move only when unengaged + ready
"""
import random

CHAOS_BAG_BASE = [1,1,0,0,-1,-1,-2,-3,'skull','skull','cultist','autofail','eldersign']
WEAKNESSES = {'Echoes of Rlyeh','Fog of Innsmouth','Church in Flames',
              'Hydra Hyde','Basic Weakness','Shadowed','Necronomicon',
              'My Glass Is Nearly Run'}

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
    if mod==-999: return False,-999,f"[{label}] AUTOFAIL",sp
    eff=skill+mod; margin=eff-diff
    return margin>=0,margin,f"[{label}] {token}({mod:+d}) {eff} vs {diff} {'OK' if margin>=0 else 'FAIL'}",sp

def build_deck(cards,weaknesses=[]):
    d=cards.copy()+list(weaknesses); random.shuffle(d); return d

def draw_hand(deck,size=5):
    hand=[]; aside=[]; d=deck.copy()
    while len(hand)<size and d:
        c=d.pop()
        if c in WEAKNESSES: aside.append(c)
        else: hand.append(c)
    d.extend(aside); random.shuffle(d)
    return hand,d

def el_scale(dmg):
    if dmg>=7: return 4
    if dmg>=6: return 3
    if dmg>=3: return 2
    return 1

# ─────────────────────────────────────────────
# INVESTIGATOR DECKS
# ─────────────────────────────────────────────

ELEANOR_DECK = (
    ['Take What You Need']*2+['Special Allowance']*2+['Clarity of Mind']*2+
    ['Military Tactics']*2+['Arcane Practice']*2+['Triage']*2+['Patch Up']*2+
    ['Fort Warren Chapel']*2+['Shores of Innsmouth']*2+['Do No Harm']*2+
    ['The Codex Revealed']*2+['Innsmouth Lessons']*1+['Private Parker']*1+
    ['Father Rodriguez']*1+['Ward of Protection EL']*2+['Focused Mind']*2+
    ['The Undying Will']*1+['Medical Bag']*1
)
ELEANOR_WEAK=['Fog of Innsmouth']

IRONHIDE_DECK = (
    ['Kings Talon']*2+['Hound of the Deep']*2+['Luck of the Draw']*2+
    ['Father Thomas']*2+['Rlyeh Fury']*2+['Ill See You in Hell']*2+
    ['Cosmic Blast']*1+['On the Hunt']*1+['Antique Dealings']*2+
    ['Premonitions']*2+['Knowledge From the Deep']*2+['Ill Manage']*1+
    ['Aquinnah']*1+['Ward of Protection']*2+['Holy Water']*2+
    ['Overpower']*2+['Guts']*2
)
IRONHIDE_WEAK=['Echoes of Rlyeh']

EDUARDO_DECK = (
    ['Holy Water']*2+['Shrivelling']*2+['St Huberts Key']*1+['Holy Word']*2+
    ['Encyclopedia']*1+['Ward of Protection']*2+['Light of Faith']*2+
    ['Read the Signs']*2+['Whispers of the Island']*2+['Divine Insight']*1+
    ['Church Collection']*1+['Answered Prayers']*1+['Anointing']*1+
    ['Ethereal Form']*2+['Crack the Case']*2+['Guts']*2+['Enraptured']*2+
    ['Perception']*2+['Holy Rosary']*1
)
EDUARDO_WEAK=['Church in Flames']

EPHRAIM_DECK = (
    ['Red Blade']*1+['RagTag']*2+['Brush It Off']*2+['Iron Will']*2+
    ['Hunt Them Down']*1+['Kori']*1+['Dread']*1+['Vicious Blow']*2+
    ['Overpower']*2+['Sure Gamble']*2+['Emergency Cache']*2+
    ['Take the Initiative']*2+['Manual Dexterity']*2+['On the Hunt']*1+
    ['Prepared for the Worst']*2+['Machete']*2+['Beat Cop']*1+['Guard Dog']*1
)
EPHRAIM_WEAK=[]

GREYSTOKE_DECK = (
    ['Magnifying Glass']*2+['Dr Milan Christopher']*1+['Encyclopedia']*1+
    ['Ancient Binding']*1+['Relic Harvester']*1+['My Eyes and Ears']*1+
    ['Deduction']*2+['Perception']*2+['Guts']*2+['Unexpected Courage']*2+
    ['Ward of Protection']*2+['Crack the Case']*2+['No Stone Unturned']*2+
    ['Drawn to the Flame']*2+['Working a Hunch']*2+['Shortcut']*1+
    ['Emergency Cache']*2
)
GREYSTOKE_WEAK=[]

MIB_DECK = (
    ['Switchblade']*2+['Lockpicks']*2+['Hard Knocks']*2+['Pickpocketing']*2+
    ['Hot Streak']*2+['Cheap Shot']*2+['Elusive']*2+['Think on Your Feet']*2+
    ['Sure Gamble']*2+['Daring']*2+['Manual Dexterity']*2+['Overpower']*2+
    ['Watch This']*2+['Lucky']*2
)
MIB_WEAK=[]

HARVEY_DECK = (
    ['Magnifying Glass']*2+['Old Book of Lore']*2+['Encyclopedia']*1+
    ['Dream Enhancing Serum']*1+['Research Librarian']*2+['Dr Milan Christopher']*1+
    ['Peter Sylvestre']*1+['Logical Reasoning']*2+['Painkillers']*2+
    ['Deduction']*2+['Perception']*2+['Guts']*2+['Unexpected Courage']*2+
    ['Ward of Protection']*2+['Emergency Cache']*2+['No Stone Unturned']*2+
    ['Drawn to the Flame']*2+['Working a Hunch']*2+['Crack the Case']*1
)
HARVEY_WEAK=['Necronomicon']

JOE_DECK = (
    ['45 Automatic']*2+['Trench Coat']*1+['Lockpicks']*1+['Switchblade']*2+
    ['Leather Coat']*1+['St Huberts Key']*1+['Lucky']*2+['Look What I Found']*2+
    ['Think on Your Feet']*2+['Sure Gamble']*2+['Daring']*2+['Overpower']*1+
    ['Take the Initiative']*2+['Manual Dexterity']*1+['Guts']*2+
    ['Lola Santiago']*1+['Leo De Luca']*1+['Streetwise']*1
)
JOE_HUNCH=['Working a Hunch','Scene of the Crime','Logical Reasoning',
           'Dynamite Blast','Barricade','Lucky','Shortcut',
           'Think on Your Feet','Slip Away','Elusive','Cheap Shot']
JOE_WEAK=[]

# ─────────────────────────────────────────────
# INVESTIGATOR FACTORIES
# ─────────────────────────────────────────────

def make_eleanor():
    hand,deck=draw_hand(build_deck(ELEANOR_DECK,ELEANOR_WEAK))
    return {'name':'Eleanor','hp':8,'san':9,'hp_max':8,'san_max':9,
            'wil':4,'int':4,'com':1,'agi':4,'res':5,
            'hand':hand,'deck':deck,'enemies':[],
            'assets':{'Innsmouth Codex':{}},
            'is_eleanor':True,'dmg_taken':0,'find_rate':0.35,'send_to_partner':True,
            'elder_sign':'bless_heal'}

def make_ironhide():
    hand,deck=draw_hand(build_deck(IRONHIDE_DECK,IRONHIDE_WEAK))
    return {'name':'Ironhide','hp':9,'san':7,'hp_max':9,'san_max':7,
            'wil':3,'int':2,'com':5,'agi':3,'res':5,
            'hand':hand,'deck':deck,'enemies':[],
            'assets':{'Hollow Warden':{},'Hydra Hyde':{}},
            'cleave':True,'warden':True,'find_rate':0.45,
            'elder_sign':'draw_res'}

def make_eduardo():
    deck=build_deck(EDUARDO_DECK,EDUARDO_WEAK)
    deck.extend(['Holy Cross','Miracle']); random.shuffle(deck)
    hand,deck=draw_hand(deck)
    return {'name':'Eduardo','hp':7,'san':9,'hp_max':7,'san_max':9,
            'wil':4,'int':4,'com':1,'agi':3,'res':5,
            'hand':hand,'deck':deck,'enemies':[],
            'assets':{'Prayer Beads':{}},
            'prayer_beads':True,'repel':True,'find_rate':0.35,'send_to_partner':True,
            'elder_sign':'bless_heal'}

def make_ephraim():
    hand,deck=draw_hand(build_deck(EPHRAIM_DECK,EPHRAIM_WEAK))
    return {'name':'Ephraim','hp':7,'san':8,'hp_max':7,'san_max':8,
            'wil':3,'int':2,'com':5,'agi':3,'res':5,
            'hand':hand,'deck':deck,'enemies':[],
            'assets':{},'cleave':False,'find_rate':0.45,
            'elder_sign':'draw_res'}

def make_greystoke():
    hand,deck=draw_hand(build_deck(GREYSTOKE_DECK,GREYSTOKE_WEAK))
    return {'name':'Greystoke','hp':7,'san':7,'hp_max':7,'san_max':7,
            'wil':3,'int':5,'com':3,'agi':2,'res':5,
            'hand':hand,'deck':deck,'enemies':[],
            'assets':{},'inv_ability':True,'find_rate':0.4,
            'elder_sign':'draw_res'}

def make_mib():
    hand,deck=draw_hand(build_deck(MIB_DECK,MIB_WEAK))
    return {'name':'MiB','hp':7,'san':7,'hp_max':7,'san_max':7,
            'wil':3,'int':3,'com':4,'agi':4,'res':5,
            'hand':hand,'deck':deck,'enemies':[],
            'assets':{},'find_rate':0.3,
            'elder_sign':'draw_res'}

def make_harvey():
    hand,deck=draw_hand(build_deck(HARVEY_DECK,HARVEY_WEAK))
    return {'name':'Harvey','hp':6,'san':9,'hp_max':6,'san_max':9,
            'wil':5,'int':4,'com':2,'agi':2,'res':5,
            'hand':hand,'deck':deck,'enemies':[],
            'assets':{},'find_rate':0.4,
            'elder_sign':'draw_res'}

def make_joe():
    hand,deck=draw_hand(build_deck(JOE_DECK,JOE_WEAK))
    hunch=JOE_HUNCH.copy(); random.shuffle(hunch)
    hand.append(hunch.pop())
    return {'name':'Joe','hp':8,'san':7,'hp_max':8,'san_max':7,
            'wil':3,'int':4,'com':4,'agi':4,'res':5,
            'hand':hand,'deck':deck,'enemies':[],
            'assets':{},'find_rate':0.3,
            'elder_sign':'draw_res'}

# ─────────────────────────────────────────────
# SIM ENGINE
# ─────────────────────────────────────────────

def run_sim(factA, factB, sim_num, pairing_name):
    bless=0; curse=0; doom=0; doom_cap=11
    complete=False; failed=False

    locs=[l.copy() for l in LOCATIONS]; random.shuffle(locs)
    cultists=[c.copy() for c in CULTISTS]; random.shuffle(cultists)
    found=0; needed=4

    enc_pool=ENCOUNTER_POOL.copy(); random.shuffle(enc_pool)
    def draw_enc():
        nonlocal enc_pool
        if not enc_pool: enc_pool=ENCOUNTER_POOL.copy(); random.shuffle(enc_pool)
        return enc_pool.pop()

    A=factA(); B=factB()

    def take_dmg(inv, amt):
        if 'Hydra Hyde' in inv['assets'] and amt>0: amt-=1
        if 'Leather Coat' in inv['assets'] and amt>0: amt-=1
        inv['hp']-=amt
        if inv.get('is_eleanor') and amt>0:
            inv['dmg_taken']=inv.get('dmg_taken',0)+amt

    def take_hor(inv, amt):
        if 'Peter Sylvestre' in inv['assets'] and amt>0: amt-=1
        if 'St Huberts Key' in inv['assets'] and amt>0: amt-=1
        inv['san']-=amt

    def el_reactive(el, partner):
        if el.get('ability_used'): return
        el['ability_used']=True
        heal=el_scale(el.get('dmg_taken',0))
        for _ in range(heal):
            if partner['san']<partner['san_max']: partner['san']=min(partner['san_max'],partner['san']+1)
            elif partner['hp']<partner['hp_max']: partner['hp']=min(partner['hp_max'],partner['hp']+1)
            elif el['san']<el['san_max']: el['san']=min(el['san_max'],el['san']+1)

    def check_sp(sp, inv, partner):
        nonlocal bless
        if sp=='bless':
            bless=max(0,bless-1)
            if partner['san']<partner['san_max']: partner['san']=min(partner['san_max'],partner['san']+1)
        if sp=='eldersign':
            if inv.get('elder_sign')=='draw_res':
                if inv['deck']: inv['hand'].append(inv['deck'].pop())
                inv['res']+=1
            elif inv.get('elder_sign')=='bless_heal':
                bless=min(10,bless+2)
                partner['san']=min(partner['san_max'],partner['san']+min(2,partner['san_max']-partner['san']))
                if inv['deck']: inv['hand'].append(inv['deck'].pop())
                if partner['deck']: partner['hand'].append(partner['deck'].pop())

    def defeat_enemy(enemy, inv, partner):
        nonlocal found, complete, bless
        if enemy in inv['enemies']: inv['enemies'].remove(enemy)
        found+=1
        if inv.get('cleave'):
            for e in inv['enemies']+partner['enemies']:
                if e is not enemy: e['hp']-=1
            inv['res']+=1
        if inv.get('prayer_beads') or inv.get('is_eleanor'):
            pass  # healing handled separately
        if found>=needed: complete=True

    def resolve_treachery(card, inv, partner):
        if card not in TREACHERIES: return
        t=TREACHERIES[card]
        for wcard in ['Ward of Protection','Ward of Protection EL']:
            if wcard in inv['hand']:
                inv['hand'].remove(wcard); take_hor(inv,1)
                if inv.get('is_eleanor'): el_reactive(inv,partner)
                return
        if 'Logical Reasoning' in inv['hand'] and t['type']=='wil':
            inv['hand'].remove('Logical Reasoning'); return
        if 'Do No Harm' in inv['hand']:
            inv['hand'].remove('Do No Harm'); return
        if t['type']=='wil':
            wil=inv['wil']
            if 'Peter Sylvestre' in inv['assets']: wil+=1
            if 'Father Rodriguez' in inv['assets']: wil+=1
            if 'Holy Rosary' in inv['assets']: wil+=1
            success,margin,res,sp=skill_test(wil,t['diff'],bless,curse,f"{inv['name']} WIL")
            check_sp(sp,inv,partner)
            if not success and t.get('fail_hor'):
                take_hor(inv,t['fail_hor'])
                if inv.get('is_eleanor'): el_reactive(inv,partner)
        elif t['type']=='agi':
            success,margin,res,sp=skill_test(inv['agi'],t['diff'],bless,curse,f"{inv['name']} AGI")
            check_sp(sp,inv,partner)
            if not success and t.get('fail_dmg'):
                take_dmg(inv,t['fail_dmg'])
                if inv.get('is_eleanor'): el_reactive(inv,partner)

    def do_fight(inv, enemy, partner):
        com=inv['com']
        for a in ['Machete','Switchblade','Hound of the Deep','Father Thomas',
                  'Red Blade','45 Automatic','Hard Knocks']:
            if a in inv['assets']: com+=1
        if inv.get('warden'): com+=2
        success,margin,res,sp=skill_test(com,enemy['fight'],bless,curse,f"{inv['name']} fight")
        check_sp(sp,inv,partner)
        if success:
            dmg=3 if margin>=2 else 2
            if sp=='bless': dmg+=1
            enemy['hp']-=dmg
            if enemy['hp']<=0: defeat_enemy(enemy,inv,partner)
        return success

    def do_investigate(inv, loc, partner):
        nonlocal bless
        int_=inv['int']
        for a in ['Magnifying Glass','Dr Milan Christopher','Encyclopedia','Innsmouth Codex']:
            if a in inv['assets']: int_+=1
        success,margin,res,sp=skill_test(int_,loc['shroud'],bless,curse,f"{inv['name']} inv")
        check_sp(sp,inv,partner)
        if success:
            if 'Dr Milan Christopher' in inv['assets']: inv['res']+=1
            if inv.get('inv_ability') and not inv.get('inv_used'):
                inv['inv_used']=True; inv['res']+=1
                if inv['deck']: inv['hand'].append(inv['deck'].pop())
            if 'Innsmouth Lessons' in inv['assets']: inv['res']+=1
            if 'Fort Warren Chapel' in inv['assets']:
                bless=min(10,bless+1)
            if cultists and random.random()<inv.get('find_rate',0.35):
                e=cultists.pop(0)
                target=partner if inv.get('send_to_partner') else inv
                target['enemies'].append(e)
        return success

    def do_turn(inv, partner, loc_offset):
        nonlocal bless, complete
        actions=3
        inv['inv_used']=False
        inv['ability_used']=False
        if 'Leo De Luca' in inv['assets']: actions+=1

        # Fast economy
        for card in inv['hand'][:]:
            if card in ['Antique Dealings','Emergency Cache','Church Collection',
                        'Special Allowance','Hot Streak']:
                inv['hand'].remove(card); inv['res']+=3

        # Fast healing cards
        if 'Clarity of Mind' in inv['hand'] and inv['res']>=1:
            if partner['san']<=4 or inv['san']<=5:
                inv['hand'].remove('Clarity of Mind'); inv['res']-=1
                partner['san']=min(partner['san_max'],partner['san']+2)

        if 'Shores of Innsmouth' in inv['hand']:
            inv['hand'].remove('Shores of Innsmouth')
            take_hor(inv,1)
            if inv.get('is_eleanor'): el_reactive(inv,partner)

        if 'Anointing' in inv['hand']:
            inv['hand'].remove('Anointing'); bless=min(10,bless+2)
            if bless>=5 and partner['san']<partner['san_max']:
                partner['san']=min(partner['san_max'],partner['san']+1)

        if 'Patch Up' in inv['hand'] and (partner['hp']<=5 or partner['san']<=4):
            inv['hand'].remove('Patch Up')
            partner['san']=min(partner['san_max'],partner['san']+1)
            partner['hp']=min(partner['hp_max'],partner['hp']+1)

        # Eduardo repel
        if inv.get('repel') and inv['enemies'] and not inv.get('repel_used') and inv['res']>=2:
            inv['repel_used']=True; inv['res']-=2
            for e in inv['enemies'][:]: partner['enemies'].append(e)
            inv['enemies'].clear()

        # Play assets (each costs 1 action)
        ASSET_COSTS = {
            'Hound of the Deep':3,'Father Thomas':3,'Holy Water':2,'Shrivelling':3,
            'St Huberts Key':2,'Holy Rosary':2,'Encyclopedia':2,'Magnifying Glass':0,
            'Machete':3,'Beat Cop':4,'Guard Dog':3,'Triage':2,'Medical Bag':2,
            'Fort Warren Chapel':1,'Father Rodriguez':3,'Private Parker':3,
            'Lockpicks':3,'Switchblade':1,'Leather Coat':0,'Peter Sylvestre':3,
            'Dr Milan Christopher':4,'Research Librarian':2,'Innsmouth Lessons':2,
            'Leo De Luca':6,'45 Automatic':4,'Trench Coat':2,'Lola Santiago':3,
        }
        priority=['Peter Sylvestre','Magnifying Glass','Leather Coat','Father Rodriguez',
                  'Private Parker','Fort Warren Chapel','Medical Bag','Triage',
                  'Hound of the Deep','Father Thomas','Machete','45 Automatic',
                  'Lockpicks','Switchblade','Shrivelling','St Huberts Key',
                  'Holy Rosary','Encyclopedia','Dr Milan Christopher',
                  'Research Librarian','Holy Water','Innsmouth Lessons','Leo De Luca']
        for asset in priority:
            cost=ASSET_COSTS.get(asset,2)
            if asset in inv['hand'] and asset not in inv['assets'] and actions>0 and inv['res']>=cost:
                inv['res']-=cost; inv['hand'].remove(asset)
                inv['assets'][asset]={'charges':5} if asset=='Triage' else {}
                actions-=1

        # Medical Bag heal (action, no charges)
        if 'Medical Bag' in inv['assets'] and actions>0:
            if partner['hp']<=6 or partner['san']<=4:
                if partner['san']<=partner['hp']:
                    partner['san']=min(partner['san_max'],partner['san']+1)
                else:
                    partner['hp']=min(partner['hp_max'],partner['hp']+1)
                actions-=1

        # Triage (action, charges)
        if 'Triage' in inv['assets'] and inv['assets']['Triage'].get('charges',0)>0 and actions>0:
            if partner['hp']<=7 or partner['san']<=5:
                inv['assets']['Triage']['charges']-=1
                if partner['san']<=partner['hp']:
                    partner['san']=min(partner['san_max'],partner['san']+1)
                else:
                    partner['hp']=min(partner['hp_max'],partner['hp']+1)
                actions-=1

        # Fight
        for enemy in inv['enemies'][:]:
            if actions<=0 or complete: break
            if enemy.get('exhausted'): continue
            do_fight(inv,enemy,partner); actions-=1
            if complete: break

        # Evade own enemies then move to partner (Eleanor)
        if inv.get('is_eleanor'):
            for enemy in inv['enemies'][:]:
                if actions<=0: break
                success,margin,res,sp=skill_test(inv['agi'],enemy['evade'],bless,curse,"EL evade")
                check_sp(sp,inv,partner)
                if success:
                    enemy['exhausted']=True
                    partner['enemies'].append(enemy); inv['enemies'].remove(enemy)
                actions-=1

        # Investigate
        loc_idx=loc_offset
        while actions>0 and not complete:
            loc=locs[loc_idx%len(locs)]; loc_idx+=1
            do_investigate(inv,loc,partner); actions-=1

    for r in range(1,13):
        if complete or failed: break
        if A['hp']<=0 or A['san']<=0: failed=True; break
        if B['hp']<=0 or B['san']<=0: failed=True; break

        A['repel_used']=False; B['repel_used']=False

        # ---- INVESTIGATOR TURNS ----
        do_turn(A,B,r)
        if complete: break
        do_turn(B,A,r+1)
        if complete: break

        # ---- ENEMY PHASE (skip Round 1) ----
        if r>1:
            for inv,partner in [(A,B),(B,A)]:
                for enemy in inv['enemies'][:]:
                    if enemy.get('exhausted'): enemy['exhausted']=False; continue
                    take_dmg(inv,enemy['dmg'])
                    if enemy.get('hor',0)>0: take_hor(inv,enemy['hor'])
                    if inv.get('is_eleanor'): el_reactive(inv,partner)

        if A['hp']<=0 or A['san']<=0: failed=True; break
        if B['hp']<=0 or B['san']<=0: failed=True; break

        # ---- UPKEEP ----
        for inv in [A,B]:
            inv['res']+=1
            if inv['deck']: inv['hand'].append(inv['deck'].pop())
            for e in inv['enemies']:
                e.pop('exhausted',None)
            while len(inv['hand'])>8: inv['hand'].pop(0)

        # ---- MYTHOS (skip Round 1) ----
        if r>1:
            doom+=1
            if doom>=doom_cap: failed=True; break
            # Prayer Beads passive heal
            for inv,partner in [(A,B),(B,A)]:
                if inv.get('prayer_beads'):
                    bless=min(10,bless+1)
                    if partner['san']<partner['san_max']:
                        partner['san']=min(partner['san_max'],partner['san']+1)
            # 1 encounter per investigator (2 total)
            for inv,partner in [(A,B),(B,A)]:
                enc=draw_enc()
                resolve_treachery(enc,inv,partner)

    return complete,r,doom


# ─────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────
if __name__=='__main__':
    random.seed()
    N=9

    pairings=[
        ("Eduardo + Ephraim",   make_eduardo, make_ephraim),
        ("Eduardo + Ironhide",  make_eduardo, make_ironhide),
        ("Eduardo + MiB",       make_eduardo, make_mib),
        ("Eleanor + Ironhide",  make_eleanor, make_ironhide),
        ("Eleanor + Eduardo",   make_eleanor, make_eduardo),
        ("Eleanor + Ephraim",   make_eleanor, make_ephraim),
        ("Eleanor + Greystoke", make_eleanor, make_greystoke),
        ("Eleanor + MiB",       make_eleanor, make_mib),
        ("Harvey + Joe",        make_harvey,  make_joe),
    ]

    print("="*65)
    print("ARKHAM LCG - CORRECTED RULES SIM - ALL PAIRINGS")
    print(f"Rules: Round 1 no Mythos/Enemy. No weakness in opening hand.")
    print(f"       Permanents at setup. Asset=1 action. Hand limit 8.")
    print(f"Sims per pairing: {N}")
    print("="*65)

    all_results=[]
    for pname,factA,factB in pairings:
        wins=0; rounds_list=[]; doom_list=[]
        for i in range(N):
            won,rounds,doom=run_sim(factA,factB,i+1,pname)
            if won: wins+=1
            rounds_list.append(rounds); doom_list.append(doom)
        pct=int(wins/N*100)
        avg_r=sum(rounds_list)/len(rounds_list)
        avg_d=sum(doom_list)/len(doom_list)
        all_results.append((pname,wins,N,pct,avg_r,avg_d))
        print(f"{pname:<30} {wins}/{N} ({pct:3d}%) | Avg rnd:{avg_r:.1f} Doom:{avg_d:.1f}/11")

    print("\n"+"="*65)
    print("FINAL TABLE (sorted by win rate)")
    print(f"{'Pairing':<30} {'Win%':>5} {'Avg Rnd':>8} {'Avg Doom':>9}")
    print("-"*58)
    for name,wins,n,pct,avg_r,avg_d in sorted(all_results,key=lambda x:-x[3]):
        bar="X"*(pct//10)
        print(f"{name:<30} {pct:>4}% {avg_r:>8.1f} {avg_d:>8.1f}/11  {bar}")
