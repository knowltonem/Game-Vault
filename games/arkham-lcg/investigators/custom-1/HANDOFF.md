# R'lyeh Expansion — AI Handoff Document

## READ THIS FIRST

This document exists so any AI assistant can pick up this project without losing context.
The primary AI is Claude (Anthropic). Secondary AIs are OpenCode and BigPickle.
When Claude's usage is paused, read this file and continue seamlessly.

---

## Project Summary

Custom Arkham Horror LCG expansion called **The R'lyeh Expansion**.
Nine custom investigator packs plus one shared upgrade pack.
Physical cards printed via Strange Eons software.
Repository: `C:\Users\edwar\Documents\games\board-game-vault` → GitHub: `knowltonem/Game-Vault`
Latest commit: `416f4ef` → main

---

## Repository Structure

```
games/arkham-lcg/investigators/custom-1/
├── HANDOFF.md                          ← YOU ARE HERE
├── Jonathan Ironhide/                  ← COMPLETE ✅ needs PNG regen
├── Alistair Greystoke/                 ← COMPLETE ✅ needs PNG regen
├── Agnes Crane/                        ← COMPLETE ✅ needs PNG regen
├── Abel Redcloud/                      ← COMPLETE ✅ needs PNG regen
├── Nora Warwick/                       ← COMPLETE ✅
├── Bjorn Blackcast/                    ← IN PROGRESS 🔧 025-037 not built
├── Ephraim Archer/                     ← COMPLETE ✅ 035 needs Strange Eons build
├── Eleanor Heart/                      ← IN PROGRESS 🔧 deck designed, not yet built
├── The Man in Black/                   ← IN PROGRESS 🔧 deck designed, not yet built
└── Upgrade Pack/                       ← DESIGNED ✅ not yet built in Strange Eons
```

---

## Standing Rules — NEVER VIOLATE

### Naming Conventions
| File Type | Convention | Example |
|---|---|---|
| Folders | `###-Card-Name` | `006-The-Red-Blade` |
| EON files | `RYP-XX-###-Card-Name.eon` | `RYP-MB-005-The-Saturday-Night-Special.eon` |
| PNG exports Front | `RYP-XX-###-Card-Name-Front.png` | `RYP-MB-005-The-Saturday-Night-Special-Front.png` |
| PNG exports Back | `RYP-XX-###-Card-Name-Back.png` | `RYP-MB-005-The-Saturday-Night-Special-Back.png` |
| Art files | `RYP-XX-###-Card-Name-Art.png` | `RYP-MB-005-The-Saturday-Night-Special-Art.png` |
| REF images | `000-REF-Description.png` | `000-REF-The-Man-in-Black-1.png` |
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
| Eleanor Heart | RYP-EH | Mystic | 🔧 Deck designed, not yet built |
| The Man in Black | RYP-MB | Rogue | 🔧 Deck designed, not yet built |

---

## Investigator Power Rankings

| Rank | Investigator | Class | Rating |
|---|---|---|---|
| 1 | Nora Warwick | Rogue | ⭐⭐⭐⭐⭐ |
| 2 | Bjorn Blackcast | Mystic | ⭐⭐⭐⭐⭐ |
| 3 | Alistair Greystoke | Seeker | ⭐⭐⭐⭐ |
| 4 | Ephraim Archer | Guardian | ⭐⭐⭐⭐ |
| 5 | Eleanor Heart | Mystic | ⭐⭐⭐⭐ |
| 6 | The Man in Black | Rogue | ⭐⭐⭐⭐ |
| 7 | Agnes Crane | Survivor | ⭐⭐⭐ |
| 8 | Abel Redcloud | Guardian | ⭐⭐⭐ |
| 9 | Jonathan Ironhide | Guardian | ⭐⭐⭐ |

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
| Eleanor Heart | 4 | 4 | 1 | 4 | 10 | 7 |
| The Man in Black | 3 | 3 | 4 | 4 | 7 | 7 |

---

## The Man in Black (RYP-MB) — IN PROGRESS 🔧

### Backstory
A quiet, pale, sad-looking man who is unmistakably dangerous. Nobody knows his real name. He moves through Arkham's underground economy with absolute authority — cash in hand, shotgun on his back, contacts everywhere. He fights when he has to, funds everything else.

### Investigator Card
| Field | Value |
|---|---|
| Name | The Man in Black |
| Subtitle | Arkham Underground |
| Class | Rogue |
| Traits | Criminal. Operative. |
| WIL | 3 |
| INT | 3 |
| COM | 4 |
| AGI | 4 |
| HP | 7 |
| SAN | 7 |
| Ability | Once per round: You may spend any number of resources. For each 2 resources spent, get +1 to any skill test until end of round. |
| Elder Sign | +1. Gain 3 resources. |
| Deckbuilding | Rogue 0-5, Neutral 0-5, up to 15 Guardian cards 0-1. No Spell cards of any level. No Arcane assets. |
| Special | You have 2 Ally slots instead of 1. |
| Pack Code | RYP-MB |

### Signature Cards (Both Permanent — start in play)
| # | Card | Type | Slot | Notes |
|---|---|---|---|---|
| 002 | The Fixer | Permanent Asset | Body | Exhaust: fight +2 COM, 3 damage. Kill = gain 2r. No icons. |
| 003 | Cash in the Bag | Permanent Asset | Accessory | At start of turn: gain 1r. No icons. |
| 004 | Doublecrossed + Sneaky Pete | Weakness | — | Revelation: take 2 horror, spawn Sneaky Pete enemy. While Pete lives: cannot gain resources. Pete: fight 3, evade 4, HP 3, damage 1/horror 1, Hunter, Retaliate. |

### CRITICAL — Permanents
- The Fixer and Cash in the Bag are PERMANENT cards
- They DO NOT go in the deck
- They DO NOT count toward deck size
- They START IN PLAY every game automatically
- They have NO skill icons
- They CANNOT be discarded or destroyed

### Full Deck (28 cards — NOT 30, because 2 Permanents outside deck)
| # | Card | Type | Class | Category | Icons |
|---|---|---|---|---|---|
| 005-006 | The Saturday Night Special x2 | Asset — Hand | Rogue | Combat / Firearm | com/com |
| 007-008 | Cash Flow x2 | Event | Rogue | Economy | wld |
| 009-010 | The Sure Thing x2 | Skill | Rogue | Economy / Skill | wld/com |
| 011-012 | Old Habit x2 | Asset | Neutral | HP Heal | wld/wil |
| 013 | It's Time x1 | Asset — No Slot | Neutral | SAN Heal / INT+AGI | int/wld |
| 014 | Big Tommy x1 | Asset — Ally | Rogue | HP Soak / AGI Boost | com/wld |
| 015 | Old Man Winters x1 | Asset — Ally | Neutral | HP+SAN Soak / WIL | wil/wld |
| 016-017 | 5 Card Stud x2 | Skill | Rogue | Wild / AGI | agi/wld |
| 018-019 | Point Blank x2 | Skill | Rogue | Combat | com/com |
| 020-021 | Arkham Underground x2 | Event | Rogue | Ammo Reload | wld/wld |
| 022-023 | Last Call x2 | Event | Rogue | AoE Combat | com/wld |
| 024-025 | Not My Problem x2 | Event | Rogue | Treachery Cancel | wil/wld |
| 026-027 | Casing the Joint x2 | Event | Rogue | AGI Investigate | agi/agi |
| 028-029 | Up The Sleeve x2 | Event | Rogue | Card Draw | agi/agi |
| 030 | I Know A Guy x1 | Event | Rogue | Asset Search | wld |

### Icon Distribution
| Stat | Count |
|---|---|
| wld | 14 |
| com | 12 |
| agi | 12 |
| wil | 6 |
| int | 1 |
| Total | 45 |

### Slot Picture
| Slot | Card |
|---|---|
| Hand | The Saturday Night Special |
| Hand | Open |
| Arcane | ❌ Restricted |
| Arcane | ❌ Restricted |
| Accessory | Cash in the Bag (Permanent) |
| Body | The Fixer (Permanent) |
| Ally | Big Tommy |
| Ally | Old Man Winters |
| No Slot | It's Time |

### Folder Status
- 001-030: ✅ All folders created and correctly named
- Strange Eons: ⬜ Not yet built
- Art: 3 REF images in art folder

### Key Design Decisions — LOCKED
| Decision | Value |
|---|---|
| The Fixer | Permanent, Body slot, exhaust fight +2 COM 3 damage, kill = 2r |
| Cash in the Bag | Permanent, Accessory slot, gain 1r per turn |
| Both Permanents | No skill icons, start in play, outside deck count |
| Deck size | 28 cards (not 30 — 2 Permanents outside) |
| 2 Ally slots | Built into investigator card from start |
| No Arcane | Restriction enforces non-supernatural identity |
| No Spells | Same restriction |
| Sneaky Pete | HP 3, fight 3, evade 4, Hunter, Retaliate |
| It's Time | No slot, +1 AGI +1 INT, heal 1 horror per round |
| Casing the Joint | AGI instead of INT for investigate, +1 clue on success |
| Arkham Underground | Fast, fully replenish any asset's uses |
| I Know A Guy | Search deck for any asset, play for free |

### Best Pairings
| Partner | Rating | Why |
|---|---|---|
| Nora Warwick | ⭐⭐⭐⭐⭐ | Bless engine makes ability spending scale beyond design intent |
| Bjorn Blackcast | ⭐⭐⭐⭐⭐ | Token control makes resource spending reliable |
| Alistair Greystoke | ⭐⭐⭐⭐⭐ | Perfect role split — Greystoke clues, MiB kills |
| Eleanor Heart | ⭐⭐⭐⭐ | Unique damage-taking dynamic, MiB powers her healing |
| Agnes Crane | ⭐⭐⭐⭐ | Encounter control + combat |
| Ephraim Archer | ⭐⭐⭐ | Redundant combat |
| Abel Redcloud | ⭐⭐ | No clue engine |

---

## Eleanor Heart (RYP-EH) — IN PROGRESS 🔧

### Investigator Card
| Field | Value |
|---|---|
| Name | Eleanor Heart |
| Subtitle | The Undying |
| Class | Mystic |
| Traits | Medic. Scholar. |
| WIL | 4 / INT | 4 / COM | 1 / AGI | 4 |
| HP | 10 / SAN | 7 |
| Ability | After one of your card effects heals damage or horror from an investigator: Heal 1 additional damage or horror for each 3 damage currently on Eleanor Heart. |
| Elder Sign | +2. You may heal 2 damage or horror from Eleanor Heart. All investigators at your location draw 1 card. |
| Deckbuilding | Mystic 0-3, Neutral 0-5, cards that heal damage or horror 0-5, up to 15 Seeker and/or Guardian cards 0-1. No Weapon cards level 1-5. |
| Pack Code | RYP-EH |

### Healing Scale
| Damage on Eleanor | Bonus Healing |
|---|---|
| 0-2 | +0 |
| 3-5 | +1 |
| 6-8 | +2 |
| 9 | +3 |

### Signature Cards
| # | Card | Type | Slot | Notes |
|---|---|---|---|---|
| 002 | Medical Bag | Asset | Hand | Uses 4 charges. Action spend 1 charge: heal 1 dmg or horror any investigator. Reaction after other heal: double it. Subtitle: Issued at Fort Warren. |
| 003 | The Innsmouth Codex | Asset | Accessory | +1 INT. Action exhaust: investigate INT. Success = +1 clue. Fail = draw 1 card. Subtitle: The Language Is Beyond Her. She Knows What It Says. |
| 004 | The Fog of Innsmouth | Weakness | — | Revelation: take 2 horror, can't self-heal until discarded. Action WIL 4 test to discard. |

### Full Deck (30 cards, 005-034)
| # | Card | Type | Class | Function | Icons |
|---|---|---|---|---|---|
| 005-006 | Take What You Need x2 | Event | Neutral | Search top 7 for any asset | int/wld |
| 007-008 | Special Allowance x2 | Event | Neutral | Fast gain 3r | wld |
| 009-010 | Last Resort x2 | Event | Mystic | AoE fight INT or WIL, 2 dmg all enemies, take 1 dmg + 1 horror | wil/int |
| 011-012 | Military Tactics x2 | Event | Neutral | Fast draw 3 cards | int/int |
| 013-014 | Arcane Practice x2 | Event | Mystic | Fight WIL, +1 dmg, +1 more on succeed by 2 | int/int |
| 015-016 | Triage x2 | Asset | Mystic | Arcane slot, 5 charges, action: heal 1 dmg or horror any investigator | wil/wil |
| 017-018 | Patch Up x2 | Event | Mystic | Fast heal 1 dmg AND 1 horror any investigator | wil/int |
| 019-020 | Fort Warren Chapel x2 | Asset | Mystic | Arcane slot, SAN soak 1, after heal: add 1 bless token | wil/wil |
| 021-022 | Army Resupply x2 | Event | Neutral | Fast replenish up to 3 charges on any asset | wil/int |
| 023-024 | Do No Harm x2 | Event | Mystic | Fast cancel treachery, take 1 horror | wil/wil |
| 025-026 | The Codex Revealed x2 | Event | Seeker | Fast discover 1 clue without investigation | int/int |
| 027 | Innsmouth Lessons x1 | Asset | Seeker | Arcane slot, after successful investigate: discover 1 clue + gain 1r | int/int |
| 028 | Private Parker x1 | Asset — Ally | Neutral | 0/3 soak, +1 AGI, draw 1 card after each heal | agi/wld |
| 029 | Chaplain Adama x1 | Asset — Ally | Neutral | 0/3 soak, +1 WIL, gain 1r after each bless token added | wil/wld |
| 030-031 | Dead Calm x2 | Skill | Neutral | wil/wil, draw 1 on fail | wil/wil |
| 032-033 | Focused Mind x2 | Skill | Neutral | int/int, draw 1 on success | int/int |
| 034 | The Undying Will x1 | Skill | Neutral | wil/int/wld, no rules text | wil/int/wld |

### Slot Picture
| Slot | Card |
|---|---|
| Hand | Medical Bag + 1 open |
| Arcane | Triage + Fort Warren Chapel OR Innsmouth Lessons |
| Accessory | The Innsmouth Codex |
| Body | Open |
| Ally | Open (Parker or Adama) |

### Folder Status
- 001-034: ✅ All folders created and correctly named
- Strange Eons: ⬜ Not yet built
- Art: ✅ All 21 art files generated and correctly named
- Art prompts: ✅ RYP-EH-Art-Prompts.md in Eleanor Heart folder

---

## Ephraim Archer (RYP-EA) — COMPLETE ✅

### Investigator
- Guardian, WIL 3 / INT 2 / COM 5 / AGI 3, HP 7 / SAN 8
- Subtitle: The Wanderer. Traits: Sell Sword.
- Ability: Spend 1r → +2 to any skill test once per round
- Elder Sign: +2. Gain 3 resources.
- Folder 035: ⬜ Needs Strange Eons build
- Profile page: ✅ Written

### Deck (30 cards, 006-035)
006-007 Prepare for the Worst x2 | 008-009 What He's Owed x2 | 010-011 The Dunwich Relic x2 | 012 Kori Kross | 013 William Dread | 014 Sebastian Fenn | 015 The Man in Black | 016-017 RagTag x2 | 018-019 Ancient Fortune x2 | 020-021 Fighter's Fury x2 | 022-023 I'll Take You With Me x2 | 024-025 Brush It Off x2 | 026-027 Mystic Blast x2 | 028-029 Old Soldier x2 | 030-031 Iron Will x2 | 032-033 Swift Shadows x2 | 034-035 Hunt Them Down x2

---

## Bjorn Blackcast (RYP-BB) — IN PROGRESS 🔧

- Mystic, WIL 5 / INT 3 / COM 2 / AGI 3, HP 6 / SAN 10
- Subtitle: The Mist Borne. Traits: Shaman. Runebearer.
- Ability: Exhaust Rune asset → reveal 2 tokens, choose 1
- Elder Sign: +3. Heal 1 horror.
- 001-024 EON/PNG built and correctly named
- Art 001-024 generated and named
- 025-037 not yet built in Strange Eons
- WIL max: Base 5 + Staff +1 + Helm +1 + Thor's Honor +1 = WIL 8

---

## Alistair Greystoke (RYP-AG) — COMPLETE ✅

- Seeker, WIL 3 / INT 5 / COM 3 / AGI 2, HP 7 / SAN 7
- Subtitle: The Immortal Scholar. Traits: Detective. Scholar. Antiquarian.
- 034 folders all clean. Missing art: 004 My Glass is Nearly Run.
- Profile page: ✅ Written
- Key locked: Wisdom of Antiquity = Hand slot. Collector's Ledger = Arcane, gain 2r after ability. My Glass = persistent horror drain, spend 5 clues to clear. My Eyes and Ears defeat = 1 horror not doom.

---

## Jonathan Ironhide (RYP-JI) — COMPLETE ✅

- Guardian, WIL 3 / INT 2 / COM 5 / AGI 3, HP 9 / SAN 7
- 34 folders clean. PNGs deleted — ready for regen.
- Hound of the Deep art: prompt written — needs generation.
- Profile page: ✅ Written

---

## Agnes Crane (RYP-AC) — COMPLETE ✅

- Survivor, WIL 4 / INT 3 / COM 3 / AGI 3, HP 6 / SAN 9
- Folders clean. Profile page: ✅ Written. Deck review: PENDING

---

## Abel Redcloud (RYP-AR) — COMPLETE ✅

- Guardian, WIL 4 / INT 2 / COM 4 / AGI 3, HP 8 / SAN 7
- Folders clean. Profile page: ✅ Written. Deck review: PENDING

---

## Nora Warwick (RYP-NW) — COMPLETE ✅

- Rogue, WIL 3 / INT 5 / COM 3 / AGI 2, HP 7 / SAN 8
- 39 folders all clean. Full catalogue written. Profile written.
- Ability: Once per round: Spend 1r → add 1 bless token
- Elder Sign: +1. Gain resources = shroud value

---

## Pending Items

### Immediate Priority
- [ ] Build The Man in Black in Strange Eons (001-030)
- [ ] Build Eleanor Heart in Strange Eons (001-034)
- [ ] Build Bjorn Blackcast 025-037 in Strange Eons
- [ ] Generate art for Bjorn 025-037
- [ ] Write RYP-BB Master Catalogue
- [ ] Build Ephraim Archer 035 in Strange Eons
- [ ] Regen PNGs for Ironhide, Greystoke, Agnes, Abel
- [ ] Generate art for The Man in Black — all cards
- [ ] Write art prompts for The Man in Black

### Secondary
- [ ] Eleanor Heart Strange Eons builds
- [ ] Review Agnes Crane deck
- [ ] Review Abel Redcloud deck
- [ ] Generate art for Ironhide 007 Hound of the Deep
- [ ] Generate art for Greystoke 004 My Glass is Nearly Run

---

## Key Design Decisions — DO NOT REVERSE

| Decision | Value |
|---|---|
| Folder naming | One folder per physical card |
| PNG handling | NEVER delete PNGs unless explicitly told to |
| Mini markers | Keep Mini-Marker EON in 001 folder for all investigators |
| Greystoke subtitle | The Immortal Scholar |
| Greystoke traits | Detective. Scholar. Antiquarian. |
| Wisdom of Antiquity slot | Hand slot |
| My Glass weakness | Persistent horror drain, spend 5 clues to clear |
| Arkham's Ring | Replaces Magnifying Glass, exhaust for +2 COM |
| My Eyes and Ears defeat | Take 1 horror not doom |
| Bjorn ability | Exhaust Rune asset → reveal 2 tokens, choose 1 |
| Bjorn Elder Sign | +3. Heal 1 horror. |
| Ragnarok | Disables ability, clears on Elder Sign in 5-token reveal |
| Leif's Leap | Neutral accessory, +1 AGI, free move per round |
| Sif's Blessing | Renamed from Sif's Love |
| The Valkyrie's Embrace | Renamed from Val's Embrace |
| Ephraim ability | Spend 1r → +2 to any skill test once per round |
| Ephraim Red Blade | Hand (2), +1 COM, fight 2-3 damage |
| Ephraim Black Cloak | Body, SAN soak 2, evade up to 2 enemies |
| Ephraim Dunwich Hounds | x2 weakness, Hunter, disables ability while at location |
| Ephraim RagTag | No slot, extra ally slot, 2 allies simultaneously |
| Ephraim Ancient Fortune | Arcane, draw 1 card after each kill, permanent |
| Ephraim Mystic Blast | AoE 2 damage all enemies, wld/wld, costs 3r |
| Eleanor class | Mystic primary |
| Eleanor COM | 1 (Strange Eons minimum) |
| Eleanor HP | 10 — scales healing power as she takes damage |
| Eleanor healing scale | +1 bonus heal per 3 damage on Eleanor |
| Eleanor no weapons | No Weapon cards level 1-5 enforced |
| Medical Bag slot | Hand slot |
| Innsmouth Codex slot | Accessory slot |
| Triage slot | Arcane slot |
| Fort Warren Chapel slot | Arcane slot |
| Army Resupply | Fast, replenish up to 3 charges, neutral |
| Parker soak | 0 HP / 3 SAN |
| Adama soak | 0 HP / 3 SAN |
| MiB The Fixer | Permanent, Body slot, no icons, exhaust fight +2 COM 3 damage, kill = 2r |
| MiB Cash in the Bag | Permanent, Accessory slot, no icons, gain 1r per turn |
| MiB deck size | 28 cards (2 Permanents outside deck) |
| MiB 2 ally slots | Built into investigator card from start |
| MiB no Arcane | Restriction — no arcane slots, no spell cards |
| MiB Sneaky Pete | HP 3, fight 3, evade 4, Hunter, Retaliate |
| MiB It's Time | No slot, +1 AGI +1 INT, heal 1 horror per round, no soak |
| MiB Casing the Joint | AGI investigate, +1 clue on success |
| MiB Arkham Underground | Fast, fully replenish any asset uses |
| MiB I Know A Guy | Search deck for any asset, play for free |
| MiB icon distribution | wld 14 / com 12 / agi 12 / wil 6 / int 1 |

---

## Emergency Context — If AI Has No Memory

If you are reading this with no prior context:
- This is a custom Arkham Horror LCG expansion project
- The user is Edward (GitHub: knowltonem)
- Nine investigators designed, six complete or near-complete
- Current priority: Build Man in Black and Eleanor Heart in Strange Eons
- Read individual investigator sections above for full card details
- Ask the user what they want to work on — do not assume
- Claude is primary AI, you are backup — maintain all standards
