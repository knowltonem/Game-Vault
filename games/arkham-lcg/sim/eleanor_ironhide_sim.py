import random

CHAOS_BAG_BASE = [1, 1, 0, 0, -1, -1, -2, -3, 'skull', 'skull', 'cultist', 'autofail', 'eldersign']

def draw_token(bless, curse):
    bag = CHAOS_BAG_BASE.copy() + ['bless']*bless + ['curse']*curse
    return random.choice(bag)

def resolve_token(token, bless, curse):
    if token == 'bless':
        inner = draw_token(max(0,bless-1), curse)
        mod, sp = resolve_token(inner, max(0,bless-1), curse)
        return (-999,'autofail') if mod==-999 else (mod+2, sp)
    if token == 'curse':
        inner = draw_token(bless, max(0,curse-1))
        mod, sp = resolve_token(inner, bless, max(0,curse-1))
        return (-999,'autofail') if mod==-999 else (mod-2, sp)
    if token == 'eldersign': return 1,'eldersign'
    if token == 'autofail': return -999,'autofail'
    if token in ('skull','cultist'): return -2, token
    return token, None

def skill_test(skill, diff, bless, curse, label=""):
    token = draw_token(bless, curse)
    mod, sp = resolve_token(token, bless, curse)
    if mod == -999:
        return False, -999, f"[{label}] {token}->AUTO-FAIL", sp
    eff = skill + mod
    margin = eff - diff
    res = f"[{label}] {token}({mod:+d}) {skill}{mod:+d}={eff} vs {diff} -> {'PASS' if margin>=0 else 'FAIL'} by {abs(margin)}"
    return margin>=0, margin, res, sp

LOCATIONS = [
    {'name':'Southside','shroud':2},{'name':'Downtown','shroud':3},
    {'name':'Easttown','shroud':2},{'name':'Merchant District','shroud':3},
    {'name':'Rivertown','shroud':2},{'name':'Miskatonic University','shroud':4},
    {'name':"St. Mary's Hospital",'shroud':3},{'name':'Woods','shroud':4},
]

CULTISTS = [
    {'name':'Swarm of Rats','hp':1,'fight':1,'evade':3,'dmg':1,'hor':0,'hunter':False},
    {'name':'Acolyte','hp':1,'fight':1,'evade':3,'dmg':1,'hor':1,'hunter':False},
    {'name':'Acolyte','hp':1,'fight':1,'evade':3,'dmg':1,'hor':1,'hunter':False},
    {'name':'Conglomeration','hp':3,'fight':3,'evade':4,'dmg':1,'hor':2,'hunter':True},
    {'name':'Wizard of Yog','hp':4,'fight':4,'evade':4,'dmg':2,'hor':1,'hunter':True},
    {'name':'Cultist Sentry','hp':2,'fight':2,'evade':3,'dmg':1,'hor':1,'hunter':False},
]

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

WEAKNESSES = {'Echoes of Rlyeh','Fog of Innsmouth','Church in Flames',
              'Hydra Hyde','Basic Weakness'}

IRONHIDE_DECK = (
    ['Kings Talon']*2+['Hound of the Deep']*2+['Luck of the Draw']*2+
    ['Father Thomas']*2+['Rlyeh Fury']*2+['Ill See You in Hell']*2+
    ['Cosmic Blast']*1+['On the Hunt']*1+['Antique Dealings']*2+
    ['Premonitions']*2+['Knowledge From the Deep']*2+['Ill Manage']*1+
    ['Aquinnah']*1+['Ward of Protection']*2+['Holy Water']*2+
    ['Overpower']*2+['Guts']*2
)
IRONHIDE_WEAKNESSES = ['Echoes of Rlyeh']

ELEANOR_DECK = (
    ['Take What You Need']*2+['Special Allowance']*2+
    ['Clarity of Mind']*2+['Military Tactics']*2+['Arcane Practice']*2+
    ['Triage']*2+['Patch Up']*2+['Fort Warren Chapel']*2+
    ['Shores of Innsmouth']*2+['Do No Harm']*2+
    ['The Codex Revealed']*2+['Innsmouth Lessons']*1+
    ['Private Parker']*1+['Father Rodriguez']*1+
    ['Ward of Protection EL']*2+['Focused Mind']*2+['The Undying Will']*1+
    ['Medical Bag']*1
)
ELEANOR_WEAKNESSES = ['Fog of Innsmouth']

def build_deck(cards, weaknesses):
    deck = cards.copy() + weaknesses.copy()
    random.shuffle(deck)
    return deck

def draw_opening_hand(deck, size=5):
    """No weaknesses in opening hand -- set aside, draw replacement, shuffle back."""
    hand = []; set_aside = []; deck_copy = deck.copy()
    while len(hand) < size and deck_copy:
        card = deck_copy.pop()
        if card in WEAKNESSES: set_aside.append(card)
        else: hand.append(card)
    deck_copy.extend(set_aside)
    random.shuffle(deck_copy)
    return hand, deck_copy

def el_heal_amount(el_dmg):
    """Eleanor healing scale: 0-2=1, 3-5=2, 6=3, 7=4"""
    if el_dmg >= 7: return 4
    if el_dmg >= 6: return 3
    if el_dmg >= 3: return 2
    return 1

def run_sim(sim_num):
    log = []
    def p(msg): log.append(msg)

    bless=0; curse=0; doom=0; doom_cap=11
    complete=False; failed=False; death_cause=''

    locs=[l.copy() for l in LOCATIONS]; random.shuffle(locs)
    cultists=[c.copy() for c in CULTISTS]; random.shuffle(cultists)
    cultists_found=0; cultists_needed=4
    ji_enemies=[]; el_enemies=[]

    enc_pool=ENCOUNTER_POOL.copy(); random.shuffle(enc_pool)
    def draw_enc():
        nonlocal enc_pool
        if not enc_pool: enc_pool=ENCOUNTER_POOL.copy(); random.shuffle(enc_pool)
        return enc_pool.pop()

    # ---- IRONHIDE SETUP ----
    # Permanents (Hollow Warden, Hydra Hyde) start in play before Round 1
    # Echoes of R'lyeh shuffled into deck -- cannot appear in opening hand
    ji_hp=9; ji_san=7; ji_res=5
    ji_wil=3; ji_int=2; ji_com=5; ji_agi=3
    ji_assets={'Hollow Warden':{'ammo':3},'Hydra Hyde':{}}
    echoes_active=False; echoes_round=random.randint(3,9)
    ji_raw_deck=build_deck(IRONHIDE_DECK, IRONHIDE_WEAKNESSES)
    ji_hand, ji_deck=draw_opening_hand(ji_raw_deck)
    # Mulligan: replace pure skill cards if no economy/assets in hand
    if not any(c in ji_hand for c in ['Antique Dealings','Holy Water','Hound of the Deep','Father Thomas']):
        discard=[c for c in ji_hand if c in ['Guts','Overpower','Premonitions']][:2]
        for c in discard: ji_hand.remove(c); ji_deck.append(c)
        random.shuffle(ji_deck)
        while len(ji_hand)<5 and ji_deck:
            card=ji_deck.pop()
            if card not in WEAKNESSES: ji_hand.append(card)
            else: ji_deck.insert(0,card)

    # ---- ELEANOR SETUP ----
    # Innsmouth Codex = Permanent, starts in play before Round 1
    # Fog of Innsmouth shuffled into deck -- cannot appear in opening hand
    el_hp=8; el_san=9; el_res=5
    el_wil=4; el_int=4; el_com=1; el_agi=4
    el_dmg=0; el_ability_used=False
    el_assets={'Innsmouth Codex':{}}
    fog_active=False; fog_round=random.randint(3,9)
    el_raw_deck=build_deck(ELEANOR_DECK, ELEANOR_WEAKNESSES)
    el_hand, el_deck=draw_opening_hand(el_raw_deck)
    # Mulligan: replace skill cards if no healing/economy in hand
    if not any(c in el_hand for c in ['Medical Bag','Triage','Special Allowance','Fort Warren Chapel','Clarity of Mind']):
        discard=[c for c in el_hand if c in ['Focused Mind','The Undying Will','Arcane Practice']][:2]
        for c in discard: el_hand.remove(c); el_deck.append(c)
        random.shuffle(el_deck)
        while len(el_hand)<5 and el_deck:
            card=el_deck.pop()
            if card not in WEAKNESSES: el_hand.append(card)
            else: el_deck.insert(0,card)

    def el_wil_stat():
        b=el_wil
        if 'Father Rodriguez' in el_assets: b+=1
        return b
    def el_int_stat():
        b=el_int
        if 'Innsmouth Codex' in el_assets: b+=1
        return b
    def ji_com_stat():
        b=ji_com
        if 'Hound of the Deep' in ji_assets: b+=1
        if 'Father Thomas' in ji_assets: b+=1
        return b

    def el_reactive_heal(src=''):
        nonlocal ji_hp,ji_san,el_hp,el_san,el_dmg,el_ability_used
        if el_ability_used: return
        el_ability_used=True
        heal=el_heal_amount(el_dmg)
        p(f"    [HEAL] Eleanor [rea] heal {heal} (dmg:{el_dmg}) ({src})")
        for _ in range(heal):
            if ji_san<7: ji_san=min(7,ji_san+1)
            elif ji_hp<9: ji_hp=min(9,ji_hp+1)
            elif el_san<9: el_san=min(9,el_san+1)
            elif el_dmg>0: el_hp=min(8,el_hp+1); el_dmg=max(0,el_dmg-1)
        p(f"    -> JI HP{ji_hp}/9 SAN{ji_san}/7 | EL HP{el_hp}/8 SAN{el_san}/9")

    def ji_take_dmg(amt):
        nonlocal ji_hp
        if 'Hydra Hyde' in ji_assets and amt>0: amt-=1; p(f"    [Hydra Hyde] -1 dmg")
        ji_hp-=amt; p(f"    Ironhide -{amt} dmg -> HP{ji_hp}/9")
    def ji_take_hor(amt):
        nonlocal ji_san
        if 'Hydra Hyde' in ji_assets and amt>0: amt-=1
        ji_san-=amt; p(f"    Ironhide -{amt} hor -> SAN{ji_san}/7")
        if echoes_active and amt>0: ji_san-=1; p(f"    [Echoes] +1 hor -> SAN{ji_san}/7")
    def el_take_dmg(amt):
        nonlocal el_hp,el_dmg
        el_hp-=amt; el_dmg+=amt
        p(f"    Eleanor -{amt} dmg -> HP{el_hp}/8 (dmg:{el_dmg})")
        if amt>0: el_reactive_heal('dmg')
    def el_take_hor(amt):
        nonlocal el_san
        el_san-=amt; p(f"    Eleanor -{amt} hor -> SAN{el_san}/9")
        if amt>0: el_reactive_heal('hor')

    def el_heal(target, amt, src=''):
        nonlocal ji_hp,ji_san,el_hp,el_san,el_dmg,bless
        if 'Fort Warren Chapel' in el_assets and amt>0:
            bless=min(10,bless+1); p(f"    [Chapel] bless:{bless}")
        if 'Private Parker' in el_assets and amt>0:
            if el_deck: el_hand.append(el_deck.pop()); p(f"    [Parker] draw")
        if target=='Ironhide': ji_hp=min(9,ji_hp+amt); p(f"    [Heal] {amt} -> Ironhide HP{ji_hp}")
        elif target=='Ironhide-hor': ji_san=min(7,ji_san+amt); p(f"    [Heal] {amt} -> Ironhide SAN{ji_san}")
        elif target=='Eleanor-dmg': el_hp=min(8,el_hp+amt); el_dmg=max(0,el_dmg-amt); p(f"    [Heal] {amt} -> Eleanor HP{el_hp}")
        elif target=='Eleanor-hor': el_san=min(9,el_san+amt); p(f"    [Heal] {amt} -> Eleanor SAN{el_san}")

    def check_sp(sp, who='Ironhide'):
        nonlocal bless,ji_res,ji_hp,ji_san,el_san,el_hp
        if sp=='bless':
            bless=max(0,bless-1)
            if ji_san<7: ji_san=min(7,ji_san+1); p(f"    [Bless] JI SAN{ji_san}")
            elif el_san<9: el_san=min(9,el_san+1); p(f"    [Bless] EL SAN{el_san}")
        if sp=='eldersign' and who=='Ironhide':
            if ji_deck: ji_hand.append(ji_deck.pop())
            ji_res+=1; p(f"  [Elder Sign JI] draw 1 + 1r={ji_res}r")
        elif sp=='eldersign' and who=='Eleanor':
            bless=min(10,bless+2); p(f"  [Elder Sign EL] +2 bless={bless}")
            h=min(2,7-ji_san); d=min(2,9-ji_hp)
            ji_san=min(7,ji_san+h); ji_hp=min(9,ji_hp+d)
            p(f"    Heals JI +{h}hor +{d}dmg -> HP{ji_hp} SAN{ji_san}")
            if ji_deck: ji_hand.append(ji_deck.pop())
            if el_deck: el_hand.append(el_deck.pop())

    def defeat_cultist(enemy, owner):
        nonlocal cultists_found,complete,ji_res
        lst=ji_enemies if owner=='ji' else el_enemies
        if enemy in lst: lst.remove(enemy)
        cultists_found+=1
        p(f"    [DEFEAT] {enemy['name']}! {cultists_found}/{cultists_needed}")
        if owner=='ji':
            for e in (ji_enemies+el_enemies)[:]:
                if e is not enemy:
                    e['hp']-=1; p(f"    [Cleave] {e['name']} HP{e['hp']}")
                    if e['hp']<=0:
                        o2='ji' if e in ji_enemies else 'el'
                        defeat_cultist(e,o2)
            ji_res+=1; p(f"    [+1r] ={ji_res}r")
            if echoes_active: ji_take_hor(1)
        if cultists_found>=cultists_needed: complete=True; p(f"  [WIN]")

    def resolve_treachery(card, target):
        if card not in TREACHERIES: return
        t=TREACHERIES[card]
        if target=='Ironhide' and 'Ward of Protection' in ji_hand:
            ji_hand.remove('Ward of Protection'); ji_take_hor(1); p(f"    [JI Ward] cancels!"); return
        if target=='Eleanor' and 'Ward of Protection EL' in el_hand:
            el_hand.remove('Ward of Protection EL'); el_take_hor(1); p(f"    [EL Ward] cancels!"); return
        if target=='Eleanor' and 'Do No Harm' in el_hand:
            el_hand.remove('Do No Harm'); p(f"    [Do No Harm] cancels! (free)"); return
        if t['type']=='wil':
            skill=ji_wil if target=='Ironhide' else el_wil_stat()
            success,margin,res,sp=skill_test(skill,t['diff'],bless,curse,f"{target} WIL")
            check_sp(sp,target); p(f"    {res}")
            if not success:
                if t.get('fail_hor'):
                    if target=='Ironhide': ji_take_hor(t['fail_hor'])
                    else: el_take_hor(t['fail_hor'])
        elif t['type']=='agi':
            skill=ji_agi if target=='Ironhide' else el_agi
            success,margin,res,sp=skill_test(skill,t['diff'],bless,curse,f"{target} AGI")
            check_sp(sp,target); p(f"    {res}")
            if not success:
                if t.get('fail_dmg'):
                    if target=='Ironhide': ji_take_dmg(t['fail_dmg'])
                    else: el_take_dmg(t['fail_dmg'])

    p("="*65)
    p(f"SIM {sim_num}: Ironhide + Eleanor Heart [RULES-CORRECTED v2]")
    p(f"Rules: Round 1=Investigation+Upkeep only. No Mythos/Enemy/Encounter.")
    p(f"Rules: No weakness in opening hand. Permanents in play at setup.")
    p(f"Rules: Asset play costs 1 action. Exhausted enemies dont attack.")
    p(f"Rules: 1 encounter card per investigator per Mythos (2 total).")
    p(f"Echoes:Rd{echoes_round} | Fog:Rd{fog_round}")
    p(f"Cultists: {[c['name'] for c in cultists]}")
    p(f"JI hand: {ji_hand}")
    p(f"EL hand: {el_hand}")
    p("="*65)

    for r in range(1,13):
        if complete or failed: break
        if ji_hp<=0: failed=True; death_cause='Ironhide HP'; break
        if ji_san<=0: failed=True; death_cause='Ironhide SAN'; break
        if el_hp<=0: failed=True; death_cause='Eleanor HP'; break
        if el_san<=0: failed=True; death_cause='Eleanor SAN'; break

        el_ability_used=False

        p(f"\n{'='*65}")
        p(f"ROUND {r} {'[SETUP ROUND]' if r==1 else ''}")
        p(f"Cultists:{cultists_found}/{cultists_needed} Doom:{doom}/{doom_cap} Bless:{bless}")
        p(f"JI: HP{ji_hp}/9 SAN{ji_san}/7 R:{ji_res} COM:{ji_com_stat()} | {[e['name'] for e in ji_enemies]}")
        p(f"EL: HP{el_hp}/8 SAN{el_san}/9 R:{el_res} WIL:{el_wil_stat()} INT:{el_int_stat()} dmg:{el_dmg} | {[e['name'] for e in el_enemies]}")

        if r==echoes_round and not echoes_active and r>1:
            echoes_active=True; ji_take_hor(2)
            p(f"  [ECHOES] drawn! JI SAN{ji_san}. Spend 4r to discard.")
        if r==fog_round and not fog_active and r>1:
            fog_active=True; el_take_hor(2)
            p(f"  [FOG] drawn! EL SAN{el_san}. +1dmg per enemy attack. Spend 3r to discard.")

        # ---- IRONHIDE TURN ----
        p(f"\n--- IRONHIDE TURN ---")
        actions=3

        for card in ji_hand[:]:
            if card=='Antique Dealings':
                ji_hand.remove(card); ji_res+=3; p(f"  [Fast] Antique Dealings -> {ji_res}r")

        for card in ['Hound of the Deep','Father Thomas','Holy Water']:
            costs={'Hound of the Deep':3,'Father Thomas':3,'Holy Water':2}
            if card in ji_hand and actions>0 and card not in ji_assets and ji_res>=costs[card]:
                ji_res-=costs[card]; ji_hand.remove(card)
                ji_assets[card]={'charges':4} if card=='Holy Water' else {}
                p(f"  [Play] {card} ({costs[card]}r, 1 act) COM:{ji_com_stat()}"); actions-=1

        for enemy in ji_enemies[:]:
            if actions<=0 or complete: break
            if enemy.get('exhausted'): continue
            com=ji_com_stat()+2
            p(f"  [Fight] {enemy['name']} HP:{enemy['hp']} COM:{com}")
            success,margin,res,sp=skill_test(com,enemy['fight'],bless,curse,"JI fight")
            check_sp(sp,'Ironhide'); p(f"    {res}")
            if success:
                dmg=3 if margin>=2 else 2
                if sp=='bless': dmg+=1
                enemy['hp']-=dmg; p(f"    {dmg}dmg -> HP{enemy['hp']}")
                if enemy['hp']<=0: defeat_cultist(enemy,'ji')
            actions-=1
            if complete: break

        if echoes_active and ji_res>=4 and actions>0:
            ji_res-=4; echoes_active=False
            p(f"  [Act] Discard Echoes (4r)"); actions-=1

        loc_idx=r
        while actions>0 and not complete:
            loc=locs[loc_idx%len(locs)]; loc_idx+=1
            p(f"  [Investigate] {loc['name']} (shroud:{loc['shroud']} INT:{ji_int})")
            success,margin,res,sp=skill_test(ji_int,loc['shroud'],bless,curse,"JI inv")
            check_sp(sp,'Ironhide'); p(f"    {res}")
            if success and cultists and random.random()<0.45:
                e=cultists.pop(0); ji_enemies.append(e); p(f"    [Find] {e['name']}!")
            elif success: p(f"    1 clue")
            actions-=1

        if complete: break

        # ---- ELEANOR TURN ----
        p(f"\n--- ELEANOR TURN ---")
        actions=3

        if fog_active and el_res>=3 and actions>0:
            el_res-=3; fog_active=False
            p(f"  [Act] Discard Fog (3r)"); actions-=1

        el_costs={'Medical Bag':2,'Triage':2,'Fort Warren Chapel':1,
                  'Innsmouth Lessons':2,'Private Parker':3,'Father Rodriguez':3}
        for card in ['Father Rodriguez','Private Parker','Fort Warren Chapel','Triage','Medical Bag','Innsmouth Lessons']:
            if card in el_hand and card not in el_assets and actions>0 and el_res>=el_costs.get(card,2):
                el_res-=el_costs[card]; el_hand.remove(card)
                if card=='Triage': el_assets[card]={'charges':5}
                else: el_assets[card]={}
                p(f"  [Play] {card} ({el_costs[card]}r, 1 act)"); actions-=1

        for card in ['Special Allowance']:
            if card in el_hand:
                el_hand.remove(card); el_res+=3; p(f"  [Fast] Special Allowance -> {el_res}r")

        for _ in range(el_hand.count('Clarity of Mind')):
            if 'Clarity of Mind' in el_hand and el_res>=1 and (ji_san<=4 or el_san<=5):
                el_hand.remove('Clarity of Mind'); el_res-=1
                if ji_san<=el_san: ji_san=min(7,ji_san+2); p(f"  [Fast] Clarity -> JI SAN{ji_san}")
                else: el_san=min(9,el_san+2); p(f"  [Fast] Clarity -> EL SAN{el_san}")

        for _ in range(el_hand.count('Shores of Innsmouth')):
            if 'Shores of Innsmouth' in el_hand:
                el_hand.remove('Shores of Innsmouth')
                el_take_hor(1); p(f"  [Fast] Shores of Innsmouth -> 2 clues!")

        if 'Military Tactics' in el_hand and len(el_hand)<=3:
            el_hand.remove('Military Tactics')
            for _ in range(3):
                if el_deck: el_hand.append(el_deck.pop())
            p(f"  [Fast] Military Tactics -> draw 3")

        if 'Patch Up' in el_hand and (ji_hp<=6 or ji_san<=4):
            el_hand.remove('Patch Up')
            el_heal('Ironhide',1,'Patch Up'); el_heal('Ironhide-hor',1,'Patch Up')

        if 'Medical Bag' in el_assets and actions>0:
            if ji_hp<=6 or ji_san<=4:
                if ji_san<=ji_hp: el_heal('Ironhide-hor',1,'Medical Bag')
                else: el_heal('Ironhide',1,'Medical Bag')
                actions-=1
            elif el_hp<=5 or el_san<=5:
                if el_dmg>0: el_heal('Eleanor-dmg',1,'Medical Bag')
                else: el_heal('Eleanor-hor',1,'Medical Bag')
                actions-=1

        if 'Triage' in el_assets and el_assets['Triage']['charges']>0 and actions>0:
            if ji_hp<=7 or ji_san<=5:
                el_assets['Triage']['charges']-=1
                if ji_san<=ji_hp: el_heal('Ironhide-hor',1,'Triage')
                else: el_heal('Ironhide',1,'Triage')
                actions-=1

        for enemy in el_enemies[:]:
            if actions<=0: break
            p(f"  [Evade] {enemy['name']} (AGI:{el_agi})")
            success,margin,res,sp=skill_test(el_agi,enemy['evade'],bless,curse,"EL evade")
            check_sp(sp,'Eleanor'); p(f"    {res}")
            if success:
                enemy['exhausted']=True
                ji_enemies.append(enemy); el_enemies.remove(enemy)
                p(f"    Evaded -> moved to Ironhide")
            actions-=1

        while actions>0 and not complete:
            loc=locs[(r+1)%len(locs)]; shroud=loc['shroud']
            p(f"  [Investigate] {loc['name']} (shroud:{shroud} INT:{el_int_stat()})")
            success,margin,res,sp=skill_test(el_int_stat(),shroud,bless,curse,"EL inv")
            check_sp(sp,'Eleanor'); p(f"    {res}")
            if success:
                if cultists and random.random()<0.35:
                    e=cultists.pop(0); ji_enemies.append(e); p(f"    [Find] {e['name']} -> Ironhide!")
                else:
                    p(f"    {'2' if 'Innsmouth Lessons' in el_assets else '1'} clue(s)")
                if 'Innsmouth Lessons' in el_assets: el_res+=1
            actions-=1

        if complete: break

        # ---- ENEMY PHASE (skip Round 1) ----
        if r==1:
            p(f"\n[ROUND 1: Enemy Phase skipped]")
        else:
            p(f"\n--- ENEMY PHASE ---")
            for enemy in ji_enemies[:]:
                if enemy.get('exhausted'):
                    enemy['exhausted']=False; p(f"  [Ready] {enemy['name']}")
                    continue
                p(f"  [Attack] {enemy['name']} -> Ironhide")
                ji_take_dmg(enemy['dmg'])
                if enemy.get('hor',0)>0: ji_take_hor(enemy['hor'])
            for enemy in el_enemies[:]:
                if enemy.get('exhausted'):
                    enemy['exhausted']=False; p(f"  [Ready] {enemy['name']}")
                    continue
                p(f"  [Attack] {enemy['name']} -> Eleanor")
                el_take_dmg(enemy['dmg'])
                if enemy.get('hor',0)>0: el_take_hor(enemy['hor'])
                if fog_active: el_take_dmg(1); p(f"    [Fog] +1 dmg")

        if ji_hp<=0 or ji_san<=0: failed=True; death_cause='Ironhide'; break
        if el_hp<=0 or el_san<=0: failed=True; death_cause='Eleanor'; break

        # ---- UPKEEP ----
        ji_res+=1; el_res+=1
        if ji_deck: ji_hand.append(ji_deck.pop())
        if el_deck: el_hand.append(el_deck.pop())
        while len(ji_hand)>8: ji_hand.pop(0)
        while len(el_hand)>8: el_hand.pop(0)
        p(f"\n--- UPKEEP --- JI:{ji_res}r({len(ji_hand)}cards) EL:{el_res}r({len(el_hand)}cards)")

        # ---- MYTHOS (skip Round 1) ----
        if r==1:
            p(f"[ROUND 1: Mythos Phase skipped]")
        else:
            doom+=1
            p(f"\n--- MYTHOS --- Doom:{doom}/{doom_cap} Bless:{bless}")
            if doom>=doom_cap: failed=True; death_cause='Doom'; p(f"  [DOOM]"); break
            if fog_active: el_take_hor(1)
            for target in ['Ironhide','Eleanor']:
                enc=draw_enc(); p(f"  [Encounter] {enc} -> {target}")
                resolve_treachery(enc,target)

    p(f"\n{'='*65}")
    p(f"RESULT: {'WIN' if complete else 'DEFEAT'}")
    p(f"Rounds:{r} | Doom:{doom}/11 | Bless:{bless}")
    p(f"Cultists:{cultists_found}/4")
    p(f"JI: HP{ji_hp}/9 SAN{ji_san}/7")
    p(f"EL: HP{el_hp}/8 SAN{el_san}/9 dmg:{el_dmg}")
    if not complete: p(f"Death: {death_cause}")
    return log, complete, r, doom, bless, el_dmg


if __name__ == '__main__':
    random.seed()
    results=[]
    for i in range(1,4):
        log,won,rounds,doom,bless,el_dmg=run_sim(i)
        for line in log: print(line)
        results.append({'won':won,'rounds':rounds,'doom':doom,'bless':bless,'el_dmg':el_dmg})
        print()

    print("="*65)
    print(f"SUMMARY: {sum(1 for r in results if r['won'])}/3 victories")
    for i,r in enumerate(results,1):
        status='WIN' if r['won'] else 'DEFEAT'
        print(f"  Sim {i}: {status} Round {r['rounds']} Doom {r['doom']}/11 Bless {r['bless']} EL_dmg:{r['el_dmg']}")
