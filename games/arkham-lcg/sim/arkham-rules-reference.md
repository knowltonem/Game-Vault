# Arkham Horror LCG — Simulator Rules Reference
## Source: Official FFG Rules Reference (arkham606.com), updated May 2026

---

## ROUND STRUCTURE

### Phase 1 — Investigation
Each investigator takes a turn. 3 actions each.

### Phase 2 — Enemy
1. Hunter enemies move
2. Ready engaged enemies attack

### Phase 3 — Upkeep
1. Each investigator gains 1 resource
2. Each investigator draws 1 card
3. All exhausted cards ready
4. Discard down to hand size (8)

### Phase 4 — Mythos
1. Place 1 doom on agenda
2. Check doom threshold
3. Each investigator draws 1 encounter card

---

## ACTIONS

| Action | Cost | Rule |
|---|---|---|
| Fight | 1 act | COM test vs enemy Fight value. Success: 1 dmg. Fail: no dmg |
| Investigate | 1 act | INT test vs location Shroud. Success: discover 1 clue |
| Evade | 1 act | AGI test vs enemy Evade value. Success: enemy exhausts + disengages |
| Move | 1 act | Move to connecting location |
| Draw | 1 act | Draw 1 card |
| Resource | 1 act | Gain 1 resource |
| Play | 1 act | Play 1 card from hand (pay cost). Fast cards: no action |
| Activate | 1 act per [act] | Trigger [act] ability on card in play |
| Engage | 1 act | Move enemy at your location into your threat area |

---

## ATTACKS OF OPPORTUNITY

Triggered when: investigator engaged with 1+ ready enemies takes an action other than Fight, Evade, Parley, or Resign.

Each engaged ready enemy attacks immediately (before the action resolves).
Fast abilities [fre] do NOT provoke AoO.

---

## ENEMY ENGAGEMENT

- Ready unengaged enemy at investigator's location IMMEDIATELY engages
- Exhausted enemies do not engage
- Aloof enemies never auto-engage
- Engaged enemies move WITH investigator when investigator moves
- Hunter enemies (unengaged) move toward nearest investigator in Enemy Phase

---

## SKILL TEST STEPS

1. Determine skill + difficulty
2. Commit skill cards (icons add to skill value)
3. Reveal 1 chaos token
4. Apply token modifier/effect
5. Total = skill + modifier vs difficulty
6. Pass if total >= difficulty
7. Apply results

### Chaos Bag (Standard difficulty, Midnight Masks)
+1, +1, 0, 0, -1, -1, -2, -3, skull(-2), skull(-2), cultist(-2), autofail, eldersign

### Token Rules
| Token | Effect |
|---|---|
| numeric | Apply as modifier |
| skull / cultist | -2 (scenario specific) |
| autofail | Automatic failure |
| eldersign | Investigator's elder sign effect |
| bless | +2, reveal another token, remove bless from bag |
| curse | -2, reveal another token, remove curse from bag |

---

## DAMAGE AND HORROR

### Two Steps:
1. Assign — may route to eligible assets (assets with health/sanity)
2. Apply — tokens placed simultaneously

### Defeat:
- Investigator: dmg >= HP or hor >= SAN → eliminated
- Enemy: dmg >= HP → defeated, discard pile
- Asset: dmg >= HP or hor >= SAN → defeated, owner's discard

---

## ENEMY PHASE DETAIL

### Step 1 — Hunter Movement
- Each ready UNENGAGED hunter enemy moves 1 location toward nearest investigator
- Does not move if already at investigator's location
- Exhausted hunters do not move

### Step 2 — Enemy Attacks
- Each READY ENGAGED enemy attacks its investigator
- Deals damage + horror simultaneously
- Enemy does NOT exhaust after attacking
- Exhausted enemies do NOT attack

---

## UPKEEP PHASE DETAIL

1. Gain 1 resource
2. Draw 1 card
3. ALL exhausted cards ready (assets, enemies, locations)
4. Discard to hand size (8)

---

## ASSET SLOTS

| Slot | Max |
|---|---|
| Hand | 2 |
| Arcane | 2 |
| Accessory | 1 |
| Body | 1 |
| Ally | 1 |

Slotless assets (Permanent, or no slot listed): no limit.

---

## KEYWORDS

### Hunter
Moves toward nearest investigator during Enemy Phase. Only when unengaged and ready.

### Aloof
Does not auto-engage. Must use Engage action. Cannot be attacked while unengaged.

### Retaliate
After investigator attacks this enemy: enemy immediately attacks back.

### Alert
After investigator FAILS evade against this enemy: enemy attacks (without exhausting).

### Elusive
After this enemy attacks or is attacked: disengages, moves to connecting location (no investigators if possible), exhausts.

### Fast
No action cost. Does not provoke AoO.

### Permanent
Enters play at game start. Not from hand. Does not count toward deck size.

---

## EXHAUST / READY TABLE

| State | Attacks? | Moves (Hunter)? | Engages? |
|---|---|---|---|
| Ready + Engaged | YES | N/A | Already engaged |
| Ready + Unengaged | NO | YES (Hunter) | YES if at investigator location |
| Exhausted + Engaged | NO | NO | Remains engaged |
| Exhausted + Unengaged | NO | NO | NO |

---

## HAND SIZE

Default: 8 cards.
Checked at end of Upkeep Phase. Discard to 8 if over.
No limit during a round.

---

## DECK EMPTY RULE

If deck is empty and must draw:
1. Shuffle discard pile into deck
2. Draw card
3. Take 1 horror

---

## DOOM

- 1 doom added to agenda each Mythos Phase
- Doom on other cards (enemies, locations) counts toward total
- Agenda advances when total doom >= threshold
- When agenda advances: remove ALL doom from ALL cards in play

---

## CLUES

- Placed on location when first revealed (shroud value per investigator)
- Discovered by successful Investigate or card ability
- Held on investigator card until spent
- Spent as group to advance Act deck

---

## INVESTIGATOR ELIMINATION

1. Remove controlled cards from play
2. Drop clues at last location
3. Return resources to pool
4. Enemies disengage and stay at last location
5. Discard threat area cards
6. If last investigator: scenario ends (defeat)

---

## FAST [fre] AND REACTION [rea]

### [fre] Free triggered ability
- Any player window
- No action cost
- No AoO

### [rea] Reaction
- "When X": before X resolves
- "After X": immediately after X resolves
- Triggers once per triggering condition

---

## SKILL CARDS

- Committed at ST.2 (before token reveal)
- Icons add to skill value for that test
- Placed in discard after test resolves
- "If successful" / "If you fail" effects trigger based on result

---

## MIDNIGHT MASKS SCENARIO RULES

- Win condition: defeat 4 cultist enemies
- Doom threshold: 11
- Encounter deck: horror-heavy (Unholy Pact, Rotting Remains, Frozen in Fear, Grasping Hands)
- 2 encounter cards per Mythos phase (1 per investigator)
- Standard chaos bag (as above)
- Skull/Cultist = -2 on Standard difficulty

---

## KNOWN SIM BUGS TO FIX

| Bug | Correct Rule |
|---|---|
| Asset plays don't cost actions | WRONG — costs 1 action unless Fast |
| Exhausted assets usable | WRONG — cannot use [act] or exhaust abilities |
| Fast cards provoke AoO | WRONG — Fast never provokes AoO |
| Auto-evade = successful test | WRONG — not a skill test at all |
| Draw to hand size in upkeep | WRONG — draw exactly 1, then discard to 8 |
| Doom removed every round | WRONG — only when agenda advances |
| Assets ready in Enemy Phase | WRONG — ready in Upkeep |
| Exhausted enemy attacks | WRONG — exhausted enemies never attack |
| Hunter moves while engaged | WRONG — hunter only moves when unengaged |
| 1 encounter card total | WRONG — 1 per investigator (2 for 2-player) |
