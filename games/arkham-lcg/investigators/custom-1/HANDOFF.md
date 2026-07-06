# R'lyeh Expansion Ã¢â‚¬â€ AI Handoff Document

## READ THIS FIRST

This document exists so any AI assistant can pick up this project without losing context.
The primary AI is Claude (Anthropic). Secondary AIs are OpenCode and BigPickle.
When Claude's usage is paused, read this file and continue seamlessly.

---

## Project Summary

Custom Arkham Horror LCG expansion called **The R'lyeh Expansion**.
Five custom investigator packs plus one shared upgrade pack.
Physical cards printed via Strange Eons software.
Repository: `C:\Users\edwar\Documents\games\board-game-vault` Ã¢â€ â€™ GitHub: `knowltonem/Game-Vault`

---

## Repository Structure

```
games/arkham-lcg/investigators/custom-1/
Ã¢â€Å“Ã¢â€â‚¬Ã¢â€â‚¬ HANDOFF.md                          Ã¢â€ Â YOU ARE HERE
Ã¢â€Å“Ã¢â€â‚¬Ã¢â€â‚¬ card-reference.md                   Ã¢â€ Â Verified ArkhamDB card text
Ã¢â€Å“Ã¢â€â‚¬Ã¢â€â‚¬ index.md                            Ã¢â€ Â Project index
Ã¢â€Å“Ã¢â€â‚¬Ã¢â€â‚¬ Jonathan Ironhide/                  Ã¢â€ Â COMPLETE Ã¢Å“â€¦ printed
Ã¢â€Å“Ã¢â€â‚¬Ã¢â€â‚¬ Alistair Greystoke/                 Ã¢â€ Â COMPLETE Ã¢Å“â€¦ printed
Ã¢â€Å“Ã¢â€â‚¬Ã¢â€â‚¬ Agnes Crane/                        Ã¢â€ Â COMPLETE Ã¢Å“â€¦ printed
Ã¢â€Å“Ã¢â€â‚¬Ã¢â€â‚¬ Abel Redcloud/                      Ã¢â€ Â COMPLETE Ã¢Å“â€¦ printed
Ã¢â€Å“Ã¢â€â‚¬Ã¢â€â‚¬ Nora Warwick/                       Ã¢â€ Â IN PROGRESS Ã°Å¸â€Â§
Ã¢â€â€Ã¢â€â‚¬Ã¢â€â‚¬ Upgrade Pack/                       Ã¢â€ Â DESIGNED Ã¢Å“â€¦ not yet built in Strange Eons
```

---

## Standing Rules Ã¢â‚¬â€ NEVER VIOLATE

### Nora's Hand Ã¢â‚¬â€ Art Prompt Rule
Whenever Nora's hand appears in art: always a young woman's hand, lean and capable, smooth skin expedition-worn but not aged, fingers strong and precise. Never old, never male. Leather-jacketed sleeve always visible.

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

## Completed Investigators Ã¢â‚¬â€ Do Not Modify

### Jonathan Ironhide (RYP-JI) Ã¢Å“â€¦ PRINTED
Guardian. Will 3 / Int 2 / Com 5 / Agi 3. Health 9 / Sanity 7.
Curse payoff fighter. Hollow Warden signature weapon.

### Alistair Greystoke (RYP-AG) Ã¢Å“â€¦ PRINTED
Seeker. Will 3 / Int 5 / Com 3 / Agi 2. Health 7 / Sanity 7.
Ally swarm investigator. Summoner's Deck signature.

### Agnes Crane (RYP-AC) Ã¢Å“â€¦ PRINTED
Survivor. Will 4 / Int 3 / Com 3 / Agi 3. Health 6 / Sanity 9.
Horror prevention specialist. Night-Gaunt + Pale Child allies.

### Abel Redcloud (RYP-AR) Ã¢Å“â€¦ PRINTED
Guardian. Will 4 / Int 2 / Com 4 / Agi 3. Health 8 / Sanity 7.
Bless generator. Sacred Spear + Spirit Coyote.

---

## Nora Warwick Ã¢â‚¬â€ Current Status Ã°Å¸â€Â§

### Folder Numbering (2026-07-06)
**Why we restructured:** Cards with multiple copies (e.g., Grave Robber Ãƒâ€”2) previously shared one folder number with `a`/`b` suffixes (e.g., `013-Grave-Robber-a/b`). This made card numbers and folder numbers misalign in the deck list, causing confusion. Now each physical card has its own folder and unique number:

- **001-012**: Investigator + signature pack cards (fixed slots)
- **013-036**: Deck cards Ã¢â‚¬â€ each card copy gets its own number (e.g., `013-Grave-Robber`, `014-Grave-Robber`)
- No `a`/`b` suffixes anywhere
- PNG convention: `RYP-NW-###-Card-Name-Front/Back.png`
- `.eon` convention: `Warwick-[Type]-[Card-Name].eon` (signatures) or `RYP-NW-###-Card-Name.eon` (regular deck)

### What Is Done
- Investigator card — fully designed and locked
- All signature cards — fully designed and locked
- All pack cards — fully designed and locked
- 36-card deck — fully designed: all 22 card entries (13 unique ×2, 9 singletons)
- All card data in: `Nora Warwick/Nora-Warwick-Card-Data.md`
- All 36 Strange Eons blocks printed with art prompts
- All 36 folders created with correct naming conventions
- PNGs exported and renamed for all 36 cards (no -Face, correct RYP-NW-###- prefix)
- Deck pairs reordered to be adjacent (017-028)
- Nora vs Finn Edwards analysis complete

### What Is NOT Done
- Art generation (Midjourney) — not yet started
- Need to check if any .eon files need updates after renames

---

## Nora Warwick Ã¢â‚¬â€ Investigator Card

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
| Requirements | The Warwick Collection Ãƒâ€”1, The Book of the Dead Ãƒâ€”1, The Family Debt Ãƒâ€”1, 1 random basic weakness |
| Pack Code | RYP-NW |
| Flavor (front) | "These Pyramids Hold More Questions than Answers" |
| Story (back) | "The Warwick name has opened every tomb, every archive, and every door that mattered. What I've found has cosmic implications." |
| EON file | `Warwick-Sig-Investigator.eon` |
| PNG front | `RYP-NW-001-Nora-Warwick-Front.png` |
| PNG back | `RYP-NW-001-Nora-Warwick-Back.png` |

---

## Nora Warwick Ã¢â‚¬â€ All Pack Cards (Strange Eons Ready)

---

### 002 Ã¢â‚¬â€ The Warwick Collection

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
| HP soak | Ã¢â‚¬â€ |
| SAN soak | 2 |
| Unique | Yes |
| Icons | 1 Ãƒâ€” `<int>` + 1 Ãƒâ€” `<wil>` |

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

### 003 Ã¢â‚¬â€ The Family Debt

| Field | Value |
|---|---|
| EON file | `Warwick-Sig-Treachery-The-Family-Debt.eon` |
| PNG front | `RYP-NW-003-The-Family-Debt-Front.png` |
| PNG back | `RYP-NW-003-The-Family-Debt-Back.png` |
| Class | Rogue |
| Level | Signature |
| Type | Treachery Ã¢â‚¬â€ Weakness |
| Traits | Flaw. Burden. |
| Unique | Yes |
| Icons | Ã¢â‚¬â€ |

Rules text:
```
Nora Warwick deck only.
Revelation Ã¢â‚¬â€ Immediately spend resources equal to half the
current agenda's doom threshold (rounded up, minimum 3).
If you cannot pay the full amount: For each resource you
cannot pay, take 1 horror or 1 damage (your choice).
<act> Spend 5 resources: Discard The Family Debt.
```
Flavor: `"The telegram arrived at the worst possible moment. They always do."`

---

### 004 Ã¢â‚¬â€ Ra-Night-Gaunt

| Field | Value |
|---|---|
| EON file | `Warwick-Ally-Ra-Night-Gaunt.eon` |
| PNG front | `RYP-NW-004-Ra-Night-Gaunt-Front.png` |
| PNG back | `RYP-NW-004-Ra-Night-Gaunt-Back.png` |
| Class | Rogue |
| Level | 0 |
| Cost | 3 |
| Slot | Ally |
| Traits | Creature. Servitor. |
| HP soak | 3 |
| SAN soak | 1 |
| Unique | Yes |
| Icons | 2 Ãƒâ€” `<com>` |

Rules text:
```
Nora Warwick deck only. Unique.
You get +1 <com> while Ra-Night-Gaunt is in play.
<rea> When Ra-Night-Gaunt is defeated: Deal 1 damage to
each enemy at Nora Warwick's location.
```
Flavor: `"A Curse of Ancient Design."`

---

### 005 Ã¢â‚¬â€ Call of Anubis

| Field | Value |
|---|---|
| EON file | `Warwick-Ally-Call-of-Anubis.eon` |
| PNG front | `RYP-NW-005-Call-of-Anubis-Front.png` |
| PNG back | `RYP-NW-005-Call-of-Anubis-Back.png` |
| Class | Rogue |
| Level | 0 |
| Cost | 3 |
| Slot | Ally |
| Traits | Creature. Servitor. |
| HP soak | 1 |
| SAN soak | 4 |
| Unique | Yes |
| Icons | 1 Ãƒâ€” `<wil>` + 1 Ãƒâ€” `<com>` |

Rules text:
```
Nora Warwick deck only. Unique.
You get +1 <wil> while Anubis-Touched is in play.
<for> When Nora Warwick would be dealt 2 or more damage or
horror from a single source: Place 1 of that damage or
horror on Anubis-Touched instead (your choice of type).
```
Flavor: `"The jackal waits for all of us. This one waits for her enemies."`

---

### 006 Ã¢â‚¬â€ The Horus Heresy

| Field | Value |
|---|---|
| EON file | `Warwick-Sig-Asset-The-Horus-Heresy.eon` |
| PNG front | `RYP-NW-006-The-Horus-Heresy-Front.png` |
| PNG back | `RYP-NW-006-The-Horus-Heresy-Back.png` |
| Class | Rogue |
| Level | Signature |
| Cost | 4 |
| Slot | Ally |
| Traits | Creature. Servitor. |
| HP soak | 2 |
| SAN soak | 3 |
| Unique | Yes |
| Icons | 1 Ãƒâ€” `<int>` + 1 Ãƒâ€” `<wil>` |

Rules text:
```
Nora Warwick deck only. Unique.
You get +1 <int> and +1 <agi> while The Horus Heresy is
in play.
<fre> Once per round, after Nora Warwick discovers a clue:
Heal 1 horror from The Horus Heresy.
```
Flavor: `"The falcon's eye sees through every deception."`

---

### 007 Ã¢â‚¬â€ The Kopis

| Field | Value |
|---|---|
| EON file | `Warwick-Asset-The-Kopis.eon` |
| PNG front | `RYP-NW-007-The-Kopis-Front.png` |
| PNG back | `RYP-NW-007-The-Kopis-Back.png` |
| Class | Rogue |
| Level | 0 |
| Cost | 2 |
| Slot | Hand |
| Traits | Item. Weapon. Relic. |
| Icons | 1 Ãƒâ€” `<com>` + 1 Ãƒâ€” `<int>` |

Rules text:
```
Nora Warwick deck only.
<act> Fight. You get +1 <com> for this attack.
This attack deals +1 damage.
<fre> After you defeat an enemy with The Kopis:
Gain 2 resources.
```
Flavor: `"Found it on a dig. It whispers to me."`

---

### 008 Ã¢â‚¬â€ The Khopesh

| Field | Value |
|---|---|
| EON file | `Warwick-Asset-The-Khopesh.eon` |
| PNG front | `RYP-NW-008-The-Khopesh-Front.png` |
| PNG back | `RYP-NW-008-The-Khopesh-Back.png` |
| Class | Rogue |
| Level | 0 |
| Cost | 2 |
| Slot | Hand |
| Traits | Item. Weapon. Relic. |
| Icons | 2 Ãƒâ€” `<com>` |

Rules text:
```
Nora Warwick deck only.
<act> Fight. You get +1 <com> for this attack.
This attack deals +1 damage.
<fre> After you defeat an enemy with The Khopesh:
Gain 1 resource and draw 1 card.
```
Flavor: `"The blade remembers them all."`

---

### 009 Ã¢â‚¬â€ The Sekhem Sceptre

| Field | Value |
|---|---|
| EON file | `Warwick-Asset-The-Sekhem-Sceptre.eon` |
| PNG front | `RYP-NW-009-The-Sekhem-Sceptre-Front.png` |
| PNG back | `RYP-NW-009-The-Sekhem-Sceptre-Back.png` |
| Class | Rogue |
| Level | 0 |
| Cost | 2 |
| Slot | Hand |
| Traits | Item. Weapon. Relic. |
| Icons | 1 Ãƒâ€” `<com>` + 1 Ãƒâ€” `<wil>` |

Rules text:
```
Nora Warwick deck only.
<act> Fight. You get +1 <com> for this attack.
This attack deals +1 damage.
After this attack resolves: Cancel the next horror
Nora Warwick would be dealt this round.
```
Flavor: `"Power is not always measured in wounds."`

---

### 010 Ã¢â‚¬â€ The Book of the Dead

| Field | Value |
|---|---|
| EON file | `Warwick-Sig-Asset-The-Book-of-the-Dead.eon` |
| PNG front | `RYP-NW-010-The-Book-of-the-Dead-Front.png` |
| PNG back | `RYP-NW-010-The-Book-of-the-Dead-Back.png` |
| Class | Rogue |
| Level | Signature |
| Cost | 1 |
| Slot | Arcane |
| Traits | Item. Tome. Relic. Blessed. |
| HP soak | Ã¢â‚¬â€ |
| SAN soak | 2 |
| Unique | Yes |
| Icons | 2 Ãƒâ€” `<int>` |
| Subtitle | Arcane and Unnatural |

Rules text:
```
Nora Warwick deck only. Unique.
You get +1 <int> while The Book of the Dead is in play.
<fre> After you successfully investigate: You may exhaust
The Book of the Dead Ã¢â‚¬â€ investigate again at your location
without spending an action.
<fre> After The Book of the Dead enters play: Search your
deck for any Insight or Relic card and draw it. Shuffle
your deck.
```
Flavor: `"With this knowledge, I can see the unseen."`

---

### 011 Ã¢â‚¬â€ The Collar of Sekhmet

| Field | Value |
|---|---|
| EON file | `Warwick-Asset-The-Collar-of-Sekhmet.eon` |
| PNG front | `RYP-NW-011-The-Collar-of-Sekhmet-Front.png` |
| PNG back | `RYP-NW-011-The-Collar-of-Sekhmet-Back.png` |
| Class | Rogue |
| Level | 0 |
| Cost | 2 |
| Slot | Body |
| Traits | Item. Relic. Blessed. |
| HP soak | 1 |
| SAN soak | 1 |
| Unique | Yes |
| Icons | 1 Ãƒâ€” `<com>` + 1 Ãƒâ€” `<wil>` |
| Subtitle | Worn in Ten Thousand Battles |

Rules text:
```
+1 <com> while The Collar of Sekhmet is in play.
<rea> When The Collar of Sekhmet would be defeated:
Instead, shuffle it into your deck.
```
Flavor: `"The curator said it was decorative. He had never worn it into the dark."`

---

### 012 Ã¢â‚¬â€ Isfet's Fury

| Field | Value |
|---|---|
| EON file | `Warwick-Event-Isfets-Fury.eon` |
| PNG front | `RYP-NW-012-Isfets-Fury-Front.png` |
| PNG back | `RYP-NW-012-Isfets-Fury-Back.png` |
| Class | Rogue |
| Level | 0 |
| Cost | 3 |
| Slot | Ã¢â‚¬â€ |
| Traits | Improvised. Relic. Cursed. |
| HP soak | Ã¢â‚¬â€ |
| SAN soak | Ã¢â‚¬â€ |
| Unique | No |
| Icons | 1 Ãƒâ€” `<wil>` + 1 Ãƒâ€” `<int>` |
| Subtitle | Cosmic Chaos |
| Base card | Dynamite Blast |

Rules text:
```
Choose a location. Deal 2 damage to each enemy at that
location. Each investigator at that location takes 1 damage.
Add 1 bless token to the chaos bag.
```
Flavor: `"The museum catalogue calls it a ceremonial vessel. It is not a ceremonial vessel."`

---
## Nora Warwick - Deck Cards

Full Strange Eons blocks are generated per-card as we build them. See Nora-Warwick-Card-Data.md for the complete deck list and card data.

Last updated: folders reordered so paired cards are adjacent (017-028 renumbered). The Family Name removed, Pact of Kha ×2 and Expedition Protocol ×2 in deck.

Current 36-card deck:

| # | Card | Reskin | Type | Class | Qty |
|---|---|---|---|---|---|
| 013-014 | Ancient Cache | Grave Robber | Event | Neutral | x2 |
| 015-016 | Shortcut | Anti-Chamber | Event | Neutral | x2 |
| 017-018 | Faustian Bargain | The Pact of Kha | Event | Rogue | x2 |
| 019-020 | Elusive | Sand Veil | Event | Rogue | x2 |
| 021-022 | Working a Hunch | Ancient Intuition | Event | Seeker | x2 |
| 023-024 | Deduction | Oxford Studies | Skill | Seeker | x2 |
| 025-026 | Ra's Wrath | (custom) | Event | Rogue | x2 |
| 027-028 | Sobek's Gift | (custom) | Event | Guardian | x2 |
| 029-030 | Manual Dexterity | Pharaoh's Chariot | Skill | Neutral | x2 |
| 031-032 | (custom) | The Oxford Gambit | Skill | Rogue | x2 |
| 033-034 | (custom) | Power of Thebes | Skill | Rogue | x2 |
| 035-036 | Logical Reasoning | Nile's Blessing | Event | Guardian | x2 |

Weapons (007-009), allies (004-006), other assets (010-012) are defined in the Pack Cards section above.


---

## Card Print Format Ã¢â‚¬â€ DEFAULT (never change)

When printing any card for Strange Eons, always use this format.
Every field gets its own fenced code block with copy button.
After every card print, include the art prompt immediately after.

Field order:
1. Card Number
2. Set
3. Name
4. Subtitle
5. Type
6. Subtype
7. Class
8. Level
9. Unique
10. Cost
11. Slot
12. Traits
13. HP Soak
14. SAN Soak
15. Icons
16. Rules Text
17. Flavor
18. Copyright

Then immediately after: Art Prompt for that card.

Example format:
**Card Number**
```
002
```
**Set**
```
RYP-NW
```
...and so on for every field.

---

## Art Prompts -- Nora Warwick

### 001 - Nora Warwick Investigator Card
```
Cinematic gritty dark fantasy photograph. Close to mid body
shot, low camera angle looking sharply upward. Professor Nora
Warwick, British archaeologist, early 30s, at the precise
moment she reads something in The Book of the Dead that
cannot be unread -- head tilted slightly downward toward the
open pages, eyes narrowed in focused inquisition not wide
with surprise.

Expression: pure focused inquisition. Eyes narrowed slightly,
not wide -- she is reading, not reacting. Head tilted the
precise degree of someone who has found the passage they were
looking for and is now extracting every detail from it. One
eyebrow fractionally raised -- not surprise, recognition.
She has suspected this. The book is confirming it. Her mouth
is set in a firm line, jaw forward, the expression of a woman
who catalogues the impossible professionally and is currently
cataloguing this. No terror. No awe. Assessment.

One hand pressed flat against the open page as if to stop it
moving, the other gripping the brass spine so hard her
knuckles are white. Dark complexion weathered by fieldwork,
sharp angular features, hair pulled severely back with loose
strands lit green from below. Wearing a worn brown leather
flight jacket over khaki expedition shirt. Around her neck:
ancient Egyptian scarab amulet, lapis lazuli, catching green
light from the book and throwing it back gold.

The Book of the Dead: massive, oppressively heavy. Deep
matte black cover with deep geometric crosshatch pattern
pressed into it. Four aged brass scarab beetle clasps at
each corner, scroll-cylinder closures along the right
edge. Left spine: thick wrapped brass cylindrical rod
binding. Cover face: a large tarnished brass circular
medallion with geometric star cutwork, winged scarab
beetle raised in the centre. Left of the medallion: a
carved black cartouche panel with Egyptian hieroglyphs
and figures in raised relief. The book is open -- the
pages within casting that eerie cold green light upward,
the black cover and tarnished brass clasps catching the
green and throwing it back dark. The aged brass does not
gleam -- it absorbs the light and releases it slowly,
like the book is reluctant to be read.

Background: crumbling Egyptian burial chamber, towering
stone pillars with hieroglyphs shifting in peripheral,
one fallen. Wrong geometry -- angles that do not resolve
correctly. Dust rising around her feet catching green and
gold light spiraling upward. Void black at absolute edges.
Warm amber torchlight far behind her -- the only normal
light in frame, barely reaching her.

Mood: professional certainty in the face of the impossible.
She has found what she came for. It is worse than expected.
She is already three steps ahead of what to do with it.
This is Tuesday.

Style: gritty cinematic realism, Ridley Scott lighting,
real film grain, extreme high contrast, three colour energy
mixing on face and hands, macro detail on expression and
open pages. Colour palette: cold green, deep gold, electric
blue-white, void black, amber edges. 8K. --ar 3:2 --v 7
```
Status: PROMPT LOCKED -- not yet generated.

---

## What To Do Next (In Order)

1. Generate art for Nora Warwick investigator card (prompt locked above)
2. Generate art prompts for all remaining pack cards (002-006, allies, weapons, soak cards)
3. Build .eon files in Strange Eons for all pack and deck cards
4. Export PNGs at 300 DPI Ã¢â‚¬â€ Front and Back for every card
5. Git commit all exports
6. Begin Upgrade Pack Strange Eons build (RYP-UP Ã¢â‚¬â€ 54 cards designed)

### Recent Changes (session update)
- Removed The Family Name ×2 from deck
- Added second copies of Pact of Kha and Expedition Protocol (back to ×2 each)
- Reordered folders so all pairs are adjacent (017-028 renumbered)
- Replaced Expedition Protocol with custom **Sobek's Gift** (Guardian 0, Fast, each investigator draws 1)
- Replaced The Opportunist ×2 with **Pharaoh's Chariot** ×2 (Manual Dexterity reskin, Neutral, 3×AGI)
- Replaced The Cairo Revelation ×2 with **Power of Thebes** ×2 (custom Rogue skill, 2×COM+2×AGI, fight/evade only)
- Replaced The Warwick Reasoning ×2 with **Nile's Blessing** ×2 (Logical Reasoning reskin, heal 2 horror)
- Created custom **The Oxford Gambit** (Rogue 0 skill, 3×AGI, +2 on evade, free move on success)
- Cleaned and renamed all PNGs exported by Strange Eons agent (removed -Face suffix, added RYP-NW-###- prefix)
- All 36 folders have correct naming conventions
- Deck stands at 33 cards toward 30 minimum across 22 card entries
- Full Nora vs Finn Edwards comparison done: Nora rated A-/B+, stronger team player than Finn

---

## Key Design Decisions Ã¢â‚¬â€ Do Not Reverse

| Decision | Value | Reason |
|---|---|---|
| Bless ability | 1r Ã¢â€ â€™ 1 bless/round | Matches Sister Mary rate, paid not free |
| Collection clue cost | 4r | Prevents automatic clue purchase |
| Horus Heresy cost | 4r | Double stat boost warrants premium |
| Family Debt penalty | 1 horror OR damage | Not both Ã¢â‚¬â€ too punishing |
| Ra on-defeat | "if any" | Timing clarification |
| Ally slots | 2 base | Charisma built in |
| Weapons | Nora only | Allies are shields not fighters |
| Soak cards | Ãƒâ€”1 each, pack not deck | 3-to-3 parity with ally slots |

---

## Upgrade Pack Status (RYP-UP)

54 cards fully designed in:
`Upgrade Pack/RYP-UP-Upgrade-Pack-Card-Data.md`

NOT YET built in Strange Eons. This is the next major build phase after Nora Warwick.

---

## Emergency Context Ã¢â‚¬â€ If AI Has No Memory

If you are reading this with no prior context:
- This is a custom Arkham Horror LCG expansion project
- The user is Edward (GitHub: knowltonem)
- Five investigators designed, four printed, one in progress
- Current task: build Nora Warwick in Strange Eons
- Read Nora-Warwick-Card-Data.md for full card details
- Ask the user what they want to work on Ã¢â‚¬â€ do not assume
- Claude is primary AI, you are backup Ã¢â‚¬â€ maintain all standards
