# R'lyeh Expansion — AI Handoff Document

## READ THIS FIRST

This document exists so any AI assistant can pick up this project without losing context.
The primary AI is Claude (Anthropic). Secondary AIs are OpenCode and BigPickle.
When Claude's usage is paused, read this file and continue seamlessly.

---

## Project Summary

Custom Arkham Horror LCG expansion called **The R'lyeh Expansion**.
Five custom investigator packs plus one shared upgrade pack.
Physical cards printed via Strange Eons software.
Repository: `C:\Users\edwar\Documents\games\board-game-vault` → GitHub: `knowltonem/Game-Vault`

---

## Repository Structure

```
games/arkham-lcg/investigators/custom-1/
├── HANDOFF.md                          ← YOU ARE HERE
├── card-reference.md                   ← Verified ArkhamDB card text
├── index.md                            ← Project index
├── Jonathan Ironhide/                  ← COMPLETE ✅ printed
├── Alistair Greystoke/                 ← COMPLETE ✅ printed
├── Agnes Crane/                        ← COMPLETE ✅ printed
├── Abel Redcloud/                      ← COMPLETE ✅ printed
├── Nora Warwick/                       ← IN PROGRESS 🔧
└── Upgrade Pack/                       ← DESIGNED ✅ not yet built in Strange Eons
```

---

## Standing Rules — NEVER VIOLATE

### Naming Conventions
| File Type | Convention | Example |
|---|---|---|
| Folders | `###-Card-Name` | `006-The-Warwick-Incendiary` |
| EON files (signature) | `Warwick-Sig-[Type]-[Name].eon` | `Warwick-Sig-Asset-The-Warwick-Collection.eon` |
| EON files (deck) | `Warwick-[Type]-[Name].eon` | `Warwick-Event-Desert-Trick.eon` |
| PNG exports | `RYP-NW-###-[Name]-Front.png` | `RYP-NW-006-The-Warwick-Incendiary-Front.png` |

### Print Standards
- Always check card-reference.md before printing any official card
- Export PNGs at 300 DPI minimum
- Always export Front AND Back for each card
- Git commit after every session with descriptive message

### Git Workflow
```
git -C "C:\Users\edwar\Documents\games\board-game-vault" add -A
git -C "C:\Users\edwar\Documents\games\board-game-vault" commit -m "Description"
git -C "C:\Users\edwar\Documents\games\board-game-vault" push
```

---

## Pack Codes

| Investigator | Pack Code |
|---|---|
| Jonathan Ironhide | RYP-JI |
| Alistair Greystoke | RYP-AG |
| Agnes Crane | RYP-AC |
| Abel Redcloud | RYP-AR |
| Nora Warwick | RYP-NW |
| Upgrade Pack | RYP-UP |

---

## Completed Investigators — Do Not Modify

### Jonathan Ironhide (RYP-JI) ✅ PRINTED
Guardian. Will 3 / Int 2 / Com 5 / Agi 3. Health 9 / Sanity 7.
Curse payoff fighter. Hollow Warden signature weapon.

### Alistair Greystoke (RYP-AG) ✅ PRINTED
Seeker. Will 3 / Int 5 / Com 3 / Agi 2. Health 7 / Sanity 7.
Ally swarm investigator. Summoner's Deck signature.

### Agnes Crane (RYP-AC) ✅ PRINTED
Survivor. Will 4 / Int 3 / Com 3 / Agi 3. Health 6 / Sanity 9.
Horror prevention specialist. Night-Gaunt + Pale Child allies.

### Abel Redcloud (RYP-AR) ✅ PRINTED
Guardian. Will 4 / Int 2 / Com 4 / Agi 3. Health 8 / Sanity 7.
Bless generator. Sacred Spear + Spirit Coyote.

---

## Nora Warwick — Current Status 🔧

### What Is Done
- Investigator card — fully designed and locked
- All signature cards — fully designed and locked
- All pack cards — fully designed and locked
- 35-card deck — fully designed and locked
- All card data in: `Nora Warwick/Nora-Warwick-Card-Data.md`
- Folders created for all pack cards (001-006)

### What Is NOT Done
- Strange Eons .eon files — NONE built yet
- Art — not yet generated
- PNG exports — none yet
- Full Strange Eons-ready card blocks — in progress

### Immediate Next Task
Write full Strange Eons-ready card blocks for every Nora Warwick pack card.
Then build .eon files in Strange Eons.
Then generate art prompts.
Then export PNGs.

---

## Nora Warwick — Investigator Card

| Field | Value |
|---|---|
| Name | Professor Nora Warwick |
| Subtitle | The Warwick Endowment |
| Class | Rogue |
| Traits | Academic. Archaeologist. Blessed. |
| Willpower | 3 |
| Intellect | 5 |
| Combat | 3 |
| Agility | 2 |
| Health | 7 |
| Sanity | 8 |
| Ability | Once per round: Spend 1 resource to add 1 bless token to the chaos bag. |
| Elder Sign | +1. If you succeed, gain resources equal to the shroud value of your location. |
| Deckbuilding | Rogue 0-5, Seeker 0-2, Guardian 0-2, Mystic 0-1, Neutral 0-5 |
| Requirements | The Warwick Collection ×1, The Book of the Dead ×1, The Family Debt ×1, 1 random basic weakness |
| Pack Code | RYP-NW |
| Flavor | "The Warwick name has opened every tomb, every archive, and every door that mattered. What I've found has cosmic implications." |
| EON file | `Warwick-Sig-Investigator.eon` |
| PNG front | `RYP-NW-001-Nora-Warwick-Front.png` |
| PNG back | `RYP-NW-001-Nora-Warwick-Back.png` |

---

## Nora Warwick — All Pack Cards (Strange Eons Ready)

---

### 002 — The Warwick Collection

| Field | Value |
|---|---|
| EON file | `Warwick-Sig-Asset-The-Warwick-Collection.eon` |
| PNG front | `RYP-NW-002-The-Warwick-Collection-Front.png` |
| PNG back | `RYP-NW-002-The-Warwick-Collection-Back.png` |
| Class | Rogue |
| Level | Signature |
| Cost | 0 |
| Slot | Accessory |
| Traits | Item. Relic. Blessed. |
| HP soak | — |
| SAN soak | 2 |
| Unique | Yes |
| Icons | 1 × `<int>` + 1 × `<wil>` |

Rules text:
```
Nora Warwick deck only. Unique.
You get +1 <int> while The Warwick Collection is in play.
<fre> At the start of your turn: Gain 1 resource.
<act> Spend 4 resources: Discover 1 clue at your location.
<fre> After you successfully investigate: You may move 1 clue
from your location to any connecting location.
```
Flavor: `"The curator at the British Museum was quite upset, until he saw the cheque."`

---

### 003 — The Family Debt

| Field | Value |
|---|---|
| EON file | `Warwick-Sig-Treachery-The-Family-Debt.eon` |
| PNG front | `RYP-NW-003-The-Family-Debt-Front.png` |
| PNG back | `RYP-NW-003-The-Family-Debt-Back.png` |
| Class | Rogue |
| Level | Signature |
| Type | Treachery — Weakness |
| Traits | Flaw. Burden. |
| Unique | Yes |
| Icons | — |

Rules text:
```
Nora Warwick deck only.
Revelation — Immediately spend resources equal to half the
current agenda's doom threshold (rounded up, minimum 3).
If you cannot pay the full amount: For each resource you
cannot pay, take 1 horror or 1 damage (your choice).
<act> Spend 5 resources: Discard The Family Debt.
```
Flavor: `"The telegram arrived at the worst possible moment. They always do."`

---

### 004 — The Book of the Dead

| Field | Value |
|---|---|
| EON file | `Warwick-Sig-Asset-The-Book-of-the-Dead.eon` |
| PNG front | `RYP-NW-004-The-Book-of-the-Dead-Front.png` |
| PNG back | `RYP-NW-004-The-Book-of-the-Dead-Back.png` |
| Class | Rogue |
| Level | Signature |
| Cost | 1 |
| Slot | Arcane |
| Traits | Item. Tome. Relic. Blessed. |
| HP soak | — |
| SAN soak | 2 |
| Unique | Yes |
| Icons | 2 × `<int>` |
| Subtitle | Arcane and Unnatural |

Rules text:
```
Nora Warwick deck only. Unique.
You get +1 <int> while The Book of the Dead is in play.
<fre> After you successfully investigate: You may exhaust
The Book of the Dead — investigate again at your location
without spending an action.
<fre> After The Book of the Dead enters play: Search your
deck for any Insight or Relic card and draw it. Shuffle
your deck.
```
Flavor: `"With this knowledge, I can see the unseen."`

---

### 005 — The Collar of Sekhmet

| Field | Value |
|---|---|
| EON file | `Warwick-Asset-The-Collar-of-Sekhmet.eon` |
| PNG front | `RYP-NW-005-The-Collar-of-Sekhmet-Front.png` |
| PNG back | `RYP-NW-005-The-Collar-of-Sekhmet-Back.png` |
| Class | Rogue |
| Level | 0 |
| Cost | 2 |
| Slot | Body |
| Traits | Item. Relic. Blessed. |
| HP soak | 1 |
| SAN soak | 1 |
| Unique | Yes |
| Icons | 1 × `<com>` + 1 × `<wil>` |
| Subtitle | Worn in Ten Thousand Battles |

Rules text:
```
You get +1 <com> while The Collar of Sekhmet is in play.
```
Flavor: `"The curator said it was decorative. He had never worn it into the dark."`

---

### 006 — The Warwick Incendiary

| Field | Value |
|---|---|
| EON file | `Warwick-Event-The-Warwick-Incendiary.eon` |
| PNG front | `RYP-NW-006-The-Warwick-Incendiary-Front.png` |
| PNG back | `RYP-NW-006-The-Warwick-Incendiary-Back.png` |
| Class | Rogue |
| Level | 0 |
| Cost | 3 |
| Slot | — |
| Traits | Improvised. Relic. Cursed. |
| HP soak | — |
| SAN soak | — |
| Unique | No |
| Icons | 1 × `<wil>` + 1 × `<int>` |
| Subtitle | Do Not Shake |
| Base card | Dynamite Blast |

Rules text:
```
Choose a location. Deal 2 damage to each enemy at that
location. Each investigator at that location takes 1 damage.
Add 1 bless token to the chaos bag.
```
Flavor: `"The museum catalogue calls it a ceremonial vessel. It is not a ceremonial vessel."`

---

### 007 — Canopic Wrappings (Soak Attachment)

| Field | Value |
|---|---|
| EON file | `Warwick-Asset-Canopic-Wrappings.eon` |
| PNG front | `RYP-NW-007-Canopic-Wrappings-Front.png` |
| PNG back | `RYP-NW-007-Canopic-Wrappings-Back.png` |
| Class | Rogue |
| Level | 0 |
| Cost | 1 |
| Slot | — (attaches to ally) |
| Traits | Item. Relic. Blessed. |
| Icons | 1 × `<wil>` + 1 × `<int>` |

Rules text:
```
Attach to an Ally asset you control.
When attached: Choose HP or SAN. That ally gains
+2 of the chosen type permanently.
<fre> At the end of the upkeep phase: Heal 1 damage
from the attached ally.
```
Flavor: `"The jars remember their purpose. So do the wrappings."`

---

### 008 — The Scarab Amulet (Soak Attachment)

| Field | Value |
|---|---|
| EON file | `Warwick-Asset-The-Scarab-Amulet.eon` |
| PNG front | `RYP-NW-008-The-Scarab-Amulet-Front.png` |
| PNG back | `RYP-NW-008-The-Scarab-Amulet-Back.png` |
| Class | Rogue |
| Level | 0 |
| Cost | 1 |
| Slot | — (attaches to ally) |
| Traits | Item. Relic. Blessed. |
| Icons | 2 × `<wil>` |

Rules text:
```
Attach to an Ally asset you control.
When attached: Choose HP or SAN. That ally gains
+2 of the chosen type permanently.
<fre> At the end of the upkeep phase: Heal 1 horror
from the attached ally.
```
Flavor: `"Khepri rolls the sun. The scarab rolls away what would destroy you."`

---

### 009 — The Eye Amulet (Soak Attachment)

| Field | Value |
|---|---|
| EON file | `Warwick-Asset-The-Eye-Amulet.eon` |
| PNG front | `RYP-NW-009-The-Eye-Amulet-Front.png` |
| PNG back | `RYP-NW-009-The-Eye-Amulet-Back.png` |
| Class | Rogue |
| Level | 0 |
| Cost | 2 |
| Slot | — (attaches to ally) |
| Traits | Item. Relic. |
| Icons | 1 × `<int>` + 1 × `<wil>` |

Rules text:
```
Attach to an Ally asset you control.
When attached: Choose HP or SAN. That ally gains
+2 of the chosen type permanently.
<rea> After the attached ally soaks damage or horror:
Exhaust The Eye Amulet — prevent 1 of that damage
or horror.
```
Flavor: `"Horus lost his eye in battle and found it again. What it sees now is different."`

---

## Nora Warwick — Deck Cards (Strange Eons Ready)

---

### 010-011 — Tomb Cache (Ancient Cache ×2)

| Field | Value |
|---|---|
| EON file | `Warwick-Event-Tomb-Cache.eon` |
| PNG front | `RYP-NW-010-Tomb-Cache-Front.png` |
| Class | Neutral |
| Level | 0 |
| Cost | 0 |
| Traits | Supply. |
| Icons | 1 × `<wld>` |
| Base card | Ancient Cache |

Rules text: `Gain 3 resources.`
Flavor: `"Every expedition leaves something behind. She knows where to look."`

---

### 012-013 — The Warwick Clause (Lone Wolf ×2)

| Field | Value |
|---|---|
| EON file | `Warwick-Asset-The-Warwick-Clause.eon` |
| PNG front | `RYP-NW-012-The-Warwick-Clause-Front.png` |
| Class | Rogue |
| Level | 0 |
| Cost | 0 |
| Slot | — |
| Traits | Condition. |
| Icons | 1 × `<wld>` |
| Base card | Lone Wolf |

Rules text:
```
At the end of the round, if you are the only investigator
at your location: Gain 1 resource.
```
Flavor: `"The Warwick endowment has a clause. She's the only one who reads it."`

---

### 014-015 — The Pact of Kha (Faustian Bargain ×2)

| Field | Value |
|---|---|
| EON file | `Warwick-Event-The-Pact-of-Kha.eon` |
| PNG front | `RYP-NW-014-The-Pact-of-Kha-Front.png` |
| Class | Rogue |
| Level | 0 |
| Cost | 0 |
| Traits | Augury. |
| Icons | 1 × `<wld>` |
| Base card | Faustian Bargain |

Rules text: `Gain 4 resources. Add 2 curse tokens to the chaos bag.`
Flavor: `"Kha's price is always paid in darkness. She pays it anyway."`

---

### 016-017 — The Warwick Method (Crack the Case ×2)

| Field | Value |
|---|---|
| EON file | `Warwick-Event-The-Warwick-Method.eon` |
| PNG front | `RYP-NW-016-The-Warwick-Method-Front.png` |
| Class | Seeker |
| Level | 0 |
| Cost | 0 |
| Traits | Insight. |
| Icons | 1 × `<int>` |
| Base card | Crack the Case |

Rules text:
```
Fast. Play when you successfully investigate a location
and clear its last clue. Gain resources equal to that
location's shroud value.
```
Flavor: `"Find everything. Document nothing. Profit immediately."`

---

### 018-019 — Ancient Intuition (Working a Hunch ×2)

| Field | Value |
|---|---|
| EON file | `Warwick-Event-Ancient-Intuition.eon` |
| PNG front | `RYP-NW-018-Ancient-Intuition-Front.png` |
| Class | Seeker |
| Level | 0 |
| Cost | 2 |
| Traits | Insight. |
| Icons | 2 × `<int>` |
| Base card | Working a Hunch |

Rules text: `Fast. Discover 1 clue at your location.`
Flavor: `"Two hundred years of digs, catalogued and cross-referenced. She already knows what's here."`

---

### 020-021 — The Academic's Eye (Deduction ×2)

| Field | Value |
|---|---|
| EON file | `Warwick-Skill-The-Academics-Eye.eon` |
| PNG front | `RYP-NW-020-The-Academics-Eye-Front.png` |
| Class | Seeker |
| Level | 0 |
| Traits | Practiced. |
| Icons | 2 × `<int>` |
| Base card | Deduction |

Rules text:
```
If this skill test is successful while investigating,
discover 1 additional clue at your location.
```
Flavor: `"She sees what others miss. Professionally."`

---

### 022-023 — Desert Trick (Cheap Shot ×2)

| Field | Value |
|---|---|
| EON file | `Warwick-Event-Desert-Trick.eon` |
| PNG front | `RYP-NW-022-Desert-Trick-Front.png` |
| Class | Rogue |
| Level | 0 |
| Cost | 2 |
| Traits | Trick. |
| Icons | 1 × `<com>` + 1 × `<agi>` |
| Base card | Cheap Shot |

Rules text:
```
Fight. You get +1 <com> for this attack. If this attack
succeeds, deal 1 damage and evade the enemy.
```
Flavor: `"Oxford never taught her this. Egypt did."`

---

### 024 — The Warwick Incendiary (Dynamite Blast ×1)

| Field | Value |
|---|---|
| EON file | `Warwick-Event-The-Warwick-Incendiary.eon` |
| PNG front | `RYP-NW-026-The-Warwick-Incendiary-Front.png` |
| Class | Rogue |
| Level | 0 |
| Cost | 3 |
| Traits | Improvised. Relic. Cursed. |
| Icons | 1 × `<wil>` + 1 × `<int>` |
| Base card | Dynamite Blast |

Rules text:
```
Choose a location. Deal 2 damage to each enemy at that
location. Each investigator at that location takes 1 damage.
Add 1 bless token to the chaos bag.
```
Flavor: `"The museum catalogue calls it a ceremonial vessel. It is not a ceremonial vessel."`

---

### 019-020 — The Family Name (Calling in Favors ×2)

| Field | Value |
|---|---|
| EON file | `Warwick-Event-The-Family-Name.eon` |
| PNG front | `RYP-NW-027-The-Family-Name-Front.png` |
| Class | Rogue |
| Level | 0 |
| Cost | 0 |
| Traits | Connection. |
| Icons | 1 × `<wld>` |
| Base card | Calling in Favors |

Rules text:
```
Fast. Return an Ally asset you control to its owner's hand.
Draw 2 cards.
```
Flavor: `"The Warwick name opens doors. She uses it sparingly. Mostly."`

---

### 025-026 — The Scholar's Eye (Perception ×2)

| Field | Value |
|---|---|
| EON file | `Warwick-Skill-The-Scholars-Eye.eon` |
| PNG front | `RYP-NW-025-The-Scholars-Eye-Front.png` |
| Class | Seeker |
| Level | 0 |
| Traits | Practiced. |
| Icons | 2 × `<int>` |
| Base card | Perception |

Rules text:
```
If this skill test is successful while investigating,
discover 1 additional clue at your location.
```
Flavor: `"She has read everything ever written about what lies beneath the sand."`

---

### 027-028 — Desert Reflexes (Manual Dexterity ×1)

| Field | Value |
|---|---|
| EON file | `Warwick-Skill-Desert-Reflexes.eon` |
| PNG front | `RYP-NW-027-Desert-Reflexes-Front.png` |
| Class | Neutral |
| Level | 0 |
| Traits | Practiced. |
| Icons | 2 × `<agi>` |
| Base card | Manual Dexterity |

Rules text: `If this skill test is successful, you may immediately evade an enemy at your location.`
Flavor: `"When the tomb traps activate, you learn to move."`

---

### 029-030 — The Opportunist (Opportunist ×2)

| Field | Value |
|---|---|
| EON file | `Warwick-Skill-The-Opportunist.eon` |
| PNG front | `RYP-NW-031-The-Opportunist-Front.png` |
| Class | Rogue |
| Level | 0 |
| Traits | Practiced. |
| Icons | 2 × `<wld>` |
| Base card | Opportunist |

Rules text:
```
If this skill test is successful and no other investigators
committed cards to this test: Return The Opportunist to
your hand instead of discarding it.
```
Flavor: `"She works alone when it matters. By design."`

---

### 031-032 — The Warwick Gambit (Daring ×2)

| Field | Value |
|---|---|
| EON file | `Warwick-Skill-The-Warwick-Gambit.eon` |
| PNG front | `RYP-NW-033-The-Warwick-Gambit-Front.png` |
| Class | Rogue |
| Level | 0 |
| Traits | Innate. |
| Icons | 2 × `<wld>` |
| Base card | Daring |

Rules text: `If this skill test fails: Draw 1 card.`
Flavor: `"The family motto is not 'be careful'."`

---

### 033 — The Kopis (×1)

| Field | Value |
|---|---|
| EON file | `Warwick-Asset-The-Kopis.eon` |
| PNG front | `RYP-NW-035-The-Kopis-Front.png` |
| Class | Rogue |
| Level | 0 |
| Cost | 2 |
| Slot | Hand |
| Traits | Item. Weapon. Relic. |
| Icons | 1 × `<com>` + 1 × `<int>` |

Rules text:
```
<act> Fight. You get +1 <com> for this attack.
This attack deals +1 damage.
<fre> After you defeat an enemy with The Kopis:
Gain 2 resources.
```
Flavor: `"Every serious archaeologist carries one. Most don't use them like this."`

---

### 034 — The Khopesh (×1)

| Field | Value |
|---|---|
| EON file | `Warwick-Asset-The-Khopesh.eon` |
| PNG front | `RYP-NW-036-The-Khopesh-Front.png` |
| Class | Rogue |
| Level | 0 |
| Cost | 2 |
| Slot | Hand |
| Traits | Item. Weapon. Relic. |
| Icons | 2 × `<com>` |

Rules text:
```
<act> Fight. You get +1 <com> for this attack.
This attack deals +1 damage.
<fre> After you defeat an enemy with The Khopesh:
Gain 1 resource and draw 1 card.
```
Flavor: `"Ra's warriors carried these into battles older than memory. The blade remembers them all."`

---

### 035 — The Sekhem Sceptre (×1)

| Field | Value |
|---|---|
| EON file | `Warwick-Asset-The-Sekhem-Sceptre.eon` |
| PNG front | `RYP-NW-037-The-Sekhem-Sceptre-Front.png` |
| Class | Rogue |
| Level | 0 |
| Cost | 2 |
| Slot | Hand |
| Traits | Item. Weapon. Relic. |
| Icons | 1 × `<com>` + 1 × `<wil>` |

Rules text:
```
<act> Fight. You get +1 <com> for this attack.
This attack deals +1 damage.
After this attack resolves: Cancel the next horror
Nora Warwick would be dealt this round.
```
Flavor: `"Power is not always measured in wounds."`

---

### 036 — Ra-Night-Gaunt (×1)

| Field | Value |
|---|---|
| EON file | `Warwick-Asset-Ra-Night-Gaunt.eon` |
| PNG front | `RYP-NW-038-Ra-Night-Gaunt-Front.png` |
| Class | Rogue |
| Level | 0 |
| Cost | 3 |
| Slot | Ally |
| Traits | Ally. Monster. Blessed. |
| HP soak | 3 |
| SAN soak | 1 |
| Icons | 2 × `<com>` |

Rules text:
```
You get +1 <com> while Ra-Night-Gaunt is in play.
<rea> After Ra-Night-Gaunt is defeated: Deal 1 damage
to each enemy at Nora Warwick's location (if any).
```
Flavor: `"Solar fire in a creature of darkness. It burns what comes near her."`

---

### 037 — Anubis-Touched (×1)

| Field | Value |
|---|---|
| EON file | `Warwick-Asset-Anubis-Touched.eon` |
| PNG front | `RYP-NW-039-Anubis-Touched-Front.png` |
| Class | Rogue |
| Level | 0 |
| Cost | 3 |
| Slot | Ally |
| Traits | Ally. Monster. |
| HP soak | 1 |
| SAN soak | 4 |
| Icons | 1 × `<wil>` + 1 × `<com>` |

Rules text:
```
You get +1 <wil> while Anubis-Touched is in play.
Forced — When Nora Warwick would be dealt 2 or more
damage or horror from a single source: Place 1 of that
damage or horror on Anubis-Touched instead (your choice
of type).
```
Flavor: `"The guardian of the dead does not ask permission. It simply steps in front."`

---

### 038 — The Horus Heresy (×1)

| Field | Value |
|---|---|
| EON file | `Warwick-Asset-The-Horus-Heresy.eon` |
| PNG front | `RYP-NW-040-The-Horus-Heresy-Front.png` |
| Class | Rogue |
| Level | 0 |
| Cost | 4 |
| Slot | Ally |
| Traits | Ally. Monster. Mythos. |
| HP soak | 2 |
| SAN soak | 3 |
| Icons | 1 × `<int>` + 1 × `<wil>` |

Rules text:
```
You get +1 <int> and +1 <agi> while The Horus Heresy
is in play.
<fre> Once per round, after Nora Warwick discovers a
clue: Heal 1 horror from The Horus Heresy.
```
Flavor: `"What wears the face of gods. It feeds on what she finds."`

---

### 039 — The Collar of Sekhmet (deck copy, ×1)

Same card as pack card 005. Use same EON file.
PNG: `RYP-NW-041-The-Collar-of-Sekhmet-Front.png`

---

### 040 — The Scarab Compass (Lucky Cigarette Case ×1)

| Field | Value |
|---|---|
| EON file | `Warwick-Asset-The-Scarab-Compass.eon` |
| PNG front | `RYP-NW-042-The-Scarab-Compass-Front.png` |
| Class | Rogue |
| Level | 0 |
| Cost | 2 |
| Slot | Accessory |
| Traits | Item. Relic. |
| Icons | 1 × `<int>` |
| Base card | Lucky Cigarette Case |

Rules text:
```
After you reveal a chaos token with a negative modifier
during a skill test: Draw 1 card.
```
Flavor: `"It always points toward what she needs. She stopped questioning it."`

---

### 041 — River Water (Liquid Courage ×1)

| Field | Value |
|---|---|
| EON file | `Warwick-Event-River-Water.eon` |
| PNG front | `RYP-NW-043-River-Water-Front.png` |
| Class | Neutral |
| Level | 0 |
| Cost | 1 |
| Traits | Supply. |
| Icons | 1 × `<wil>` |
| Base card | Liquid Courage |

Rules text:
```
Heal 1 horror. If you have 3 or more resources:
Heal 2 horror instead.
```
Flavor: `"The Nile remembers. So does she."`

---

## Art Prompts — Nora Warwick

### 001 — Investigator Card
```
Cinematic gritty dark fantasy photograph. Professor Nora Warwick,
a British archaeologist in her 30s, sharp features, wearing a leather
flight jacket over khaki expedition clothes, holding an ancient scarab
amulet that glows faintly gold. Behind her, Egyptian hieroglyphs and
crumbling stone pillars. Dust motes in dim torchlight. Gritty, dark,
atmospheric, dramatic lighting. In her hand The Book of the Dead,
opened, with Nora peering in — its large, weighty body bound in Large
Gold Metal Binding, an eerie green glow emitting from the inside of
the book like it has its own life-force.
```
Status: PROMPT LOCKED — not yet generated.

---

## What To Do Next (In Order)

1. Generate art for Nora Warwick investigator card (prompt locked above)
2. Generate art prompts for all remaining pack cards (002-006, allies, weapons, soak cards)
3. Build .eon files in Strange Eons for all pack and deck cards
4. Export PNGs at 300 DPI — Front and Back for every card
5. Git commit all exports
6. Begin Upgrade Pack Strange Eons build (RYP-UP — 54 cards designed)

### Recent Changes (session update)
- Deck swaps: Pact of Kha ×2→×1, Expedition Protocol ×2→×1
- Replaced Scarab Compass + River Water with Cairo Revelation ×2 + Warwick Reasoning ×2
- Both new cards are unconditional — no trigger conditions
- Art prompt locked for Nora investigator card
- Deck is now 35 cards

---

## Key Design Decisions — Do Not Reverse

| Decision | Value | Reason |
|---|---|---|
| Bless ability | 1r → 1 bless/round | Matches Sister Mary rate, paid not free |
| Collection clue cost | 4r | Prevents automatic clue purchase |
| Horus Heresy cost | 4r | Double stat boost warrants premium |
| Family Debt penalty | 1 horror OR damage | Not both — too punishing |
| Ra on-defeat | "if any" | Timing clarification |
| Ally slots | 2 base | Charisma built in |
| Weapons | Nora only | Allies are shields not fighters |
| Soak cards | ×1 each, pack not deck | 3-to-3 parity with ally slots |

---

## Upgrade Pack Status (RYP-UP)

54 cards fully designed in:
`Upgrade Pack/RYP-UP-Upgrade-Pack-Card-Data.md`

NOT YET built in Strange Eons. This is the next major build phase after Nora Warwick.

---

## Emergency Context — If AI Has No Memory

If you are reading this with no prior context:
- This is a custom Arkham Horror LCG expansion project
- The user is Edward (GitHub: knowltonem)
- Five investigators designed, four printed, one in progress
- Current task: build Nora Warwick in Strange Eons
- Read Nora-Warwick-Card-Data.md for full card details
- Ask the user what they want to work on — do not assume
- Claude is primary AI, you are backup — maintain all standards
