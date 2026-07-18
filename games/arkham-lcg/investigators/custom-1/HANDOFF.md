# R'lyeh Expansion — AI Handoff Document

## READ THIS FIRST

This document exists so any AI assistant can pick up this project without losing context.
The primary AI is Claude (Anthropic). Secondary AIs are OpenCode and BigPickle.
When Claude's usage is paused, read this file and continue seamlessly.

---

## Project Summary

Custom Arkham Horror LCG expansion called **The R'lyeh Expansion**.
Seven custom investigator packs plus one shared upgrade pack.
Physical cards printed via Strange Eons software.
Repository: `C:\Users\edwar\Documents\games\board-game-vault` → GitHub: `knowltonem/Game-Vault`
Latest commit: `b453ccd` → main

---

## Repository Structure

```
games/arkham-lcg/investigators/custom-1/
├── HANDOFF.md                          ← YOU ARE HERE
├── MASTER-CATALOGUE.md
├── INVESTIGATOR-PROFILE-TEMPLATE.md
├── Jonathan Ironhide/                  ← COMPLETE ✅ needs PNG regen
├── Alistair Greystoke/                 ← COMPLETE ✅ needs PNG regen
├── Agnes Crane/                        ← COMPLETE ✅ needs PNG regen
├── Abel Redcloud/                      ← COMPLETE ✅ needs PNG regen
├── Nora Warwick/                       ← COMPLETE ✅
├── Bjorn Blackcast/                    ← IN PROGRESS 🔧 cards 025-037 not built
├── Ephraim Archer/                     ← COMPLETE ✅ 035 needs Strange Eons build
└── Upgrade Pack/                       ← DESIGNED ✅ not yet built in Strange Eons
```

---

## Standing Rules — NEVER VIOLATE

### Naming Conventions
| File Type | Convention | Example |
|---|---|---|
| Folders | `###-Card-Name` | `006-The-Red-Blade` |
| EON files | `RYP-XX-###-Card-Name.eon` | `RYP-EA-006-The-Red-Blade.eon` |
| PNG exports Front | `RYP-XX-###-Card-Name-Front.png` | `RYP-EA-006-The-Red-Blade-Front.png` |
| PNG exports Back | `RYP-XX-###-Card-Name-Back.png` | `RYP-EA-006-The-Red-Blade-Back.png` |
| Art files | `RYP-XX-###-Card-Name-Art.png` | `RYP-EA-006-The-Red-Blade-Art.png` |
| REF images | `000-REF-Description.png` | `000-REF-Ephraim-Archer-1.png` |
| Mini markers | Keep any Mini-Marker EON files — every investigator should have one |

### PNG Handling
- NEVER delete PNG files from card folders unless explicitly told to
- Only rename PNGs to convention, never delete them
- Strange Eons re-exports constantly — rename not delete

### Print Standards
- Every card print: full fenced code block per field (copy button)
- Art prompt with image filename immediately after each card
- After completing each card: clean up folder naming before moving to next
- Any change triggers a full card reprint

### Git Workflow
```
git -C "C:\Users\edwar\Documents\games\board-game-vault" add -A
git -C "C:\Users\edwar\Documents\games\board-game-vault" commit -m "Description"
git -C "C:\Users\edwar\Documents\games\board-game-vault" push
```

---

## Pack Codes

| Investigator | Pack Code | Class | Status |
|---|---|---|---|
| Jonathan Ironhide | RYP-JI | Guardian | ✅ Complete — needs PNG regen |
| Alistair Greystoke | RYP-AG | Seeker | ✅ Complete — needs PNG regen |
| Agnes Crane | RYP-AC | Survivor | ✅ Complete — needs PNG regen |
| Abel Redcloud | RYP-AR | Guardian | ✅ Complete — needs PNG regen |
| Nora Warwick | RYP-NW | Rogue | ✅ Complete |
| Bjorn Blackcast | RYP-BB | Mystic | 🔧 Cards 025-037 not yet built |
| Ephraim Archer | RYP-EA | Guardian | ✅ Complete — 035 needs build |

---

## Investigator Power Rankings

| Rank | Investigator | Class | Rating |
|---|---|---|---|
| 1 | Nora Warwick | Rogue | ⭐⭐⭐⭐⭐ |
| 2 | Bjorn Blackcast | Mystic | ⭐⭐⭐⭐⭐ |
| 3 | Alistair Greystoke | Seeker | ⭐⭐⭐⭐ |
| 4 | Ephraim Archer | Guardian | ⭐⭐⭐⭐ |
| 5 | Agnes Crane | Survivor | ⭐⭐⭐ |
| 6 | Abel Redcloud | Guardian | ⭐⭐⭐ |
| 7 | Jonathan Ironhide | Guardian | ⭐⭐⭐ |

---

## Investigator Stats

| Investigator | WIL | INT | COM | AGI | HP | SAN |
|---|---|---|---|---|---|---|
| Jonathan Ironhide | 3 | 2 | 5 | 3 | 9 | 7 |
| Alistair Greystoke | 3 | 5 | 3 | 2 | 7 | 7 |
| Agnes Crane | 4 | 3 | 3 | 3 | 6 | 9 |
| Abel Redcloud | 4 | 2 | 4 | 3 | 8 | 7 |
| Nora Warwick | 3 | 5 | 3 | 2 | 7 | 8 |
| Bjorn Blackcast | 5 | 3 | 2 | 3 | 6 | 10 |
| Ephraim Archer | 3 | 2 | 5 | 3 | 7 | 8 |

---

## Ephraim Archer (RYP-EA) — COMPLETE ✅

### Investigator Card
| Field | Value |
|---|---|
| Name | Ephraim Archer |
| Subtitle | The Wanderer |
| Class | Guardian |
| Traits | Sell Sword. |
| WIL | 3 / INT | 2 / COM | 5 / AGI | 3 |
| HP | 7 / SAN | 8 |
| Ability | Once per round: Before making a skill test, you may spend 1 resource to get +2 to that test. |
| Elder Sign | +2. Gain 3 resources. |
| Deckbuilding | Guardian 0-5, Mystic 0-2, Neutral 0-5 |
| Requirements | The Red Blade x1, The Black Cloak x1, The Dunwich Hounds x2 |
| Flavor | "I've seen things you people wouldn't believe." |
| Back Story | He found too many dark things in Dunwich. He fought his way back to Arkham, but something has followed him back. |

### Signature Cards
| # | Card | Type | Key Ability |
|---|---|---|---|
| 002 | The Red Blade | Hand (2) Asset | +1 COM, fight 2-3 damage, Spoils of an Old War |
| 003 | The Black Cloak | Body Asset | SAN soak 2, evade up to 2 enemies |
| 004-005 | The Dunwich Hounds x2 | Enemy Weakness | Hunter, disables ability while at location |

### Deck (30 cards, 006-035)
| # | Card | Function |
|---|---|---|
| 006-007 | Prepare for the Worst x2 | Search top 9 for any asset |
| 008-009 | What He's Owed x2 | Fast gain 3r |
| 010-011 | The Dunwich Relic x2 | Accessory, heal 1 damage or horror, 3 charges |
| 012 | Kori Kross | Ally, +1 COM, react 1 damage on engage |
| 013 | William Dread | Ally, +1 COM, react 1 damage on engage |
| 014 | Sebastian Fenn | Ally, +2 INT, free clue on move |
| 015 | The Man in Black | Ally, gain 1r per turn |
| 016-017 | RagTag x2 | Extra ally slot, 2 allies simultaneously |
| 018-019 | Ancient Fortune x2 | Arcane, draw 1 card after each kill |
| 020-021 | Fighter's Fury x2 | Skill com/com, +1 damage on fight success |
| 022-023 | I'll Take You With Me x2 | Fast fight, +2 COM, 1 horror on fail |
| 024-025 | Brush It Off x2 | Cancel treachery, take 1 horror |
| 026-027 | Mystic Blast x2 | AoE 2 damage all enemies, wld/wld |
| 028-029 | Old Soldier x2 | Skill wld/wld |
| 030-031 | Iron Will x2 | Skill wil/wil, draw on fail |
| 032-033 | Swift Shadows x2 | Skill agi/agi, move after evade |
| 034-035 | Hunt Them Down x2 | Search for enemy, fight with +2 COM |

### Folder Status
- 001-034: ✅ All clean
- 035: ⬜ Needs Strange Eons build
- Art folder: ✅ All named correctly
- Profile page: ✅ Ephraim-Archer-Profile.md

---

## Bjorn Blackcast (RYP-BB) — IN PROGRESS 🔧

### Investigator
| Field | Value |
|---|---|
| Name | Bjorn Blackcast |
| Subtitle | The Mist Borne |
| Class | Mystic |
| Traits | Shaman. Runebearer. |
| WIL | 5 / INT | 3 / COM | 2 / AGI | 3 |
| HP | 6 / SAN | 10 |
| Ability | Once per round: Before revealing a chaos token, exhaust a Rune asset to reveal 2 tokens and choose which applies. Return other to bag. |
| Elder Sign | +3. Heal 1 horror. |
| Deckbuilding | Mystic 0-5, Survivor 0-2, Seeker 0-1, Neutral 0-5 |
| Requirements | The Runic Staff x1, The Runic Helm x1, The Ragnarok x1, 1 random basic weakness |

### Build Status
| Component | Status |
|---|---|
| 001-024 EON/PNG | ✅ Built and correctly named |
| 025-037 | ⬜ Not yet built in Strange Eons |
| Art 001-024 | ✅ Generated and named |
| Art 025-037 | ⬜ Prompts written, not generated |
| Profile page | ✅ Written |
| Master Catalogue | ⬜ Not yet written |

### WIL Stacking
Base 5 + Staff +1 + Helm +1 + Thor's Honor +1 = WIL 8 maximum

---

## Alistair Greystoke (RYP-AG) — COMPLETE ✅

- Seeker, WIL 3 / INT 5 / COM 3 / AGI 2, HP 7 / SAN 7
- Subtitle: The Immortal Scholar
- Traits: Detective. Scholar. Antiquarian.
- 034 folders, all clean
- Art folder: all named correctly
- Missing art: 004 My Glass is Nearly Run — needs generation
- Profile page: ✅ Written

### Key Locked Decisions
- Wisdom of Antiquity: Hand slot
- Collector's Ledger: Arcane, gain 2r after ability fires
- Arkham's Ring: replaces Magnifying Glass, exhaust for +2 COM
- My Glass weakness: persistent horror drain, spend 5 clues to clear
- My Eyes and Ears defeat: take 1 horror not doom

---

## Jonathan Ironhide (RYP-JI) — COMPLETE ✅

- Guardian, WIL 3 / INT 2 / COM 5 / AGI 3, HP 9 / SAN 7
- 34 folders, all clean, EONs renamed to RYP-JI convention
- PNGs deleted — ready for regen with correct names
- 21 art files named to convention
- Hound of the Deep art: new prompt written — needs generation
- Profile page: ✅ Written

---

## Agnes Crane (RYP-AC) — COMPLETE ✅

- Survivor, WIL 4 / INT 3 / COM 3 / AGI 3, HP 6 / SAN 9
- Folders split, EONs renamed RYP-AC, PNGs deleted ready for regen
- Profile page: ✅ Written
- Deck review: PENDING

---

## Abel Redcloud (RYP-AR) — COMPLETE ✅

- Guardian, WIL 4 / INT 2 / COM 4 / AGI 3, HP 8 / SAN 7
- Folders split, EONs renamed RYP-AR, PNGs deleted ready for regen
- Profile page: ✅ Written
- Deck review: PENDING

---

## Nora Warwick (RYP-NW) — COMPLETE ✅

- Rogue, WIL 3 / INT 5 / COM 3 / AGI 2, HP 7 / SAN 8
- 39 folders all clean, all correctly named
- Full catalogue: Nora Warwick/RYP-NW-Master-Catalogue.md
- Card data: Nora Warwick/Nora-Warwick-Card-Data.md
- Profile: Nora Warwick/Nora-Warwick-Profile.md
- Ability: Once per round: Spend 1r to add 1 bless token
- Elder Sign: +1. Gain resources = shroud value

---

## Pending Items

### Immediate Priority
- [ ] Build Bjorn Blackcast 025-037 in Strange Eons
- [ ] Generate art for Bjorn 025-037
- [ ] Write RYP-BB Master Catalogue
- [ ] Build Ephraim Archer 035 in Strange Eons
- [ ] Regen PNGs for Ironhide, Greystoke, Agnes, Abel

### Secondary
- [ ] Review Agnes Crane deck
- [ ] Review Abel Redcloud deck
- [ ] Generate art for Ironhide 007 Hound of the Deep
- [ ] Generate art for Greystoke 004 My Glass is Nearly Run

---

## Key Design Decisions — DO NOT REVERSE

| Decision | Value |
|---|---|
| Folder naming | One folder per physical card, number = card number |
| PNG handling | NEVER delete PNGs unless explicitly told to |
| Mini markers | Keep Mini-Marker EON in 001 folder for all investigators |
| Greystoke traits | Detective. Scholar. Antiquarian. |
| Greystoke subtitle | The Immortal Scholar |
| Wisdom of Antiquity slot | Hand slot |
| My Glass weakness | Persistent horror drain, spend 5 clues to clear |
| Arkham's Ring | Replaces Magnifying Glass, exhaust for +2 COM |
| My Eyes and Ears defeat | Take 1 horror not doom |
| Bjorn ability | Exhaust Rune asset, reveal 2 tokens, choose 1 |
| Bjorn Elder Sign | +3. Heal 1 horror. |
| Ragnarok | Disables ability, clears on Elder Sign in 5-token reveal |
| Leif's Leap | Neutral accessory, +1 AGI, free move per round, no AOO |
| Sif's Blessing | Renamed from Sif's Love |
| The Valkyrie's Embrace | Renamed from Val's Embrace |
| Ephraim ability | Spend 1r to get +2 to any skill test once per round |
| Ephraim Elder Sign | +2. Gain 3 resources. |
| Red Blade | Hand (2), +1 COM, fight 2-3 damage |
| Black Cloak | Body, SAN soak 2, evade up to 2 enemies |
| Dunwich Hounds | x2 weakness, Hunter, disables ability while at location |
| RagTag | No slot, extra ally slot, 2 allies simultaneously |
| Ancient Fortune | Arcane, draw 1 card after each kill, permanent |
| Mystic Blast | AoE 2 damage all enemies, wld/wld, costs 3r |

---

## Emergency Context — If AI Has No Memory

If you are reading this with no prior context:
- This is a custom Arkham Horror LCG expansion project
- The user is Edward (GitHub: knowltonem)
- Seven investigators designed, six complete or near-complete
- Current priority: Complete Bjorn Blackcast (025-037) and regen PNGs for older investigators
- Read individual investigator card data files for full card details
- Ask the user what they want to work on — do not assume
- Claude is primary AI, you are backup — maintain all standards
