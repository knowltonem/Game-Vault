# R'lyeh Expansion — AI Handoff Document

## READ THIS FIRST

This document exists so any AI assistant can pick up this project without losing context.
The primary AI is Claude (Anthropic). Secondary AIs are OpenCode and BigPickle.
When Claude's usage is paused, read this file and continue seamlessly.

---

## Project Summary

Custom Arkham Horror LCG expansion called **The R'lyeh Expansion**.
Eight custom investigator packs plus one shared upgrade pack.
Physical cards printed via Strange Eons software.
Repository: `C:\Users\edwar\Documents\games\board-game-vault` → GitHub: `knowltonem/Game-Vault`
Latest commit: `feaff2d` → main

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
└── Upgrade Pack/                       ← DESIGNED ✅ not yet built in Strange Eons
```

---

## Standing Rules — NEVER VIOLATE

### Naming Conventions
| File Type | Convention | Example |
|---|---|---|
| Folders | `###-Card-Name` | `006-The-Red-Blade` |
| EON files | `RYP-XX-###-Card-Name.eon` | `RYP-EH-006-Take-What-You-Need.eon` |
| PNG exports Front | `RYP-XX-###-Card-Name-Front.png` | `RYP-EH-006-Take-What-You-Need-Front.png` |
| PNG exports Back | `RYP-XX-###-Card-Name-Back.png` | `RYP-EH-006-Take-What-You-Need-Back.png` |
| Art files | `RYP-XX-###-Card-Name-Art.png` | `RYP-EH-006-Take-What-You-Need-Art.png` |
| REF images | `000-REF-Description.png` | `000-REF-Eleanor-Heart-1.jpeg` |
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
|---|---|---|---|---|
| Jonathan Ironhide | RYP-JI | Guardian | ✅ Complete — needs PNG regen |
| Alistair Greystoke | RYP-AG | Seeker | ✅ Complete — needs PNG regen |
| Agnes Crane | RYP-AC | Survivor | ✅ Complete — needs PNG regen |
| Abel Redcloud | RYP-AR | Guardian | ✅ Complete — needs PNG regen |
| Nora Warwick | RYP-NW | Rogue | ✅ Complete |
| Bjorn Blackcast | RYP-BB | Mystic | ✅ Complete — 37 .eon, 1 missing |
| Ephraim Archer | RYP-EA | Guardian | ✅ Complete |
| Eleanor Heart | RYP-EH | Mystic | 🔧 Deck designed, not yet built in Strange Eons |

---

## Investigator Power Rankings

| Rank | Investigator | Class | Rating |
|---|---|---|---|
| 1 | Nora Warwick | Rogue | ⭐⭐⭐⭐⭐ |
| 2 | Bjorn Blackcast | Mystic | ⭐⭐⭐⭐⭐ |
| 3 | Alistair Greystoke | Seeker | ⭐⭐⭐⭐ |
| 4 | Ephraim Archer | Guardian | ⭐⭐⭐⭐ |
| 5 | Eleanor Heart | Mystic | ⭐⭐⭐⭐ |
| 6 | Agnes Crane | Survivor | ⭐⭐⭐ |
| 7 | Abel Redcloud | Guardian | ⭐⭐⭐ |
| 8 | Jonathan Ironhide | Guardian | ⭐⭐⭐ |

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

---

## Eleanor Heart (RYP-EH) — IN PROGRESS 🔧 (Strange Eons)

### Backstory
Former Army nurse, Lieutenant, stationed at Fort Warren (Massachusetts) — a real Civil War fort on Georges Island near Boston Harbor, close to Innsmouth. She was not a combat medic — a base nurse, educated, precise, kept records. She went to Innsmouth. She doesn't remember what happened. She woke on the beach alone, sand in her lungs, something cold where her heartbeat used to be. Her unit of 12 didn't come back. She wanders Arkham now, healing others while searching for answers about herself. She put her weapons down after Innsmouth and will not pick them up again.

### Investigator Card
| Field | Value |
|---|---|
| Name | Eleanor Heart |
| Subtitle | The Undying |
| Class | Mystic |
| Traits | Medic. Scholar. |
| WIL | 4 |
| INT | 4 |
| COM | 1 |
| AGI | 4 |
| HP | 10 |
| SAN | 7 |
| Ability | After one of your card effects heals damage or horror from an investigator: Heal 1 additional damage or horror for each 3 damage currently on Eleanor Heart. |
| Elder Sign | +2. You may heal 2 damage or horror from Eleanor Heart. All investigators at your location draw 1 card. |
| Deckbuilding | Mystic 0-3, Neutral 0-5, cards that "heal damage or horror" 0-5, up to 15 Seeker and/or Guardian cards 0-1. No Weapon cards level 1-5. |
| Pack Code | RYP-EH |

### Healing Scale
| Damage on Eleanor | Bonus Healing |
|---|---|
| 0-2 | +0 |
| 3-5 | +1 |
| 6-8 | +2 |
| 9 | +3 |

### High HP Design Intent
HP 10 is intentional — as Eleanor takes damage her healing power increases. At 9 damage she is one hit from death and healing +3 on every heal. The tension: let her take damage to amplify healing, or protect her and lose the bonus.

### Signature Cards
| # | Card | Type | Slot | Notes |
|---|---|---|---|---|
| 002 | Medical Bag | Asset | Hand | Uses 4 charges, heal 1 dmg or horror. Doubles heals via reaction. Subtitle: Issued at Fort Warren. Flavor: "Fort Warren issued it. Innsmouth changed it. Now it's different." |
| 003 | The Innsmouth Codex | Asset | Accessory | +1 INT. Action exhaust: investigate INT. Success = +1 clue. Fail = draw 1 card. Flavor: "She wasn't supposed to see it. Now she can't unsee it." |
| 004 | The Fog of Innsmouth | Weakness | — | Revelation: take 2 horror, can't self-heal until discarded. Action WIL 4 test to discard. Flavor: "Twelve people went into Innsmouth. The fog claimed them." |

### Full Deck (30 cards, 005-034)
| # | Card | Type | Class | Function |
|---|---|---|---|---|
| 005-006 | Take What You Need x2 | Event | Neutral | Search top 7 for any asset |
| 007-008 | Special Allowance x2 | Event | Neutral | Fast gain 3r |
| 009-010 | Last Resort x2 | Event | Mystic | AoE fight INT or WIL, 2 dmg all enemies, take 1 dmg + 1 horror |
| 011-012 | Military Tactics x2 | Event | Neutral | Fast draw 3 cards |
| 013-014 | Arcane Practice x2 | Event | Mystic | Fight WIL, +1 dmg, +1 more on succeed by 2. Icons: int/int |
| 015-016 | Triage x2 | Asset | Mystic | Arcane slot, 5 charges, action: heal 1 dmg or horror any investigator |
| 017-018 | Patch Up x2 | Event | Mystic | Fast, heal 1 dmg AND 1 horror any investigator |
| 019-020 | Fort Warren Chapel x2 | Asset | Mystic | Arcane slot, SAN soak 1, free: after you heal add 1 bless token |
| 021-022 | Army Resupply x2 | Event | Neutral | Fast, replenish up to 3 charges on any asset you control |
| 023-024 | Do No Harm x2 | Event | Mystic | Fast cancel treachery, take 1 horror |
| 025-026 | The Codex Revealed x2 | Event | Seeker | Fast discover 1 clue without investigation |
| 027 | Innsmouth Lessons x1 | Asset | Seeker | Arcane slot, free: after successful investigate discover 1 clue + gain 1r |
| 028 | Private Parker x1 | Asset | Neutral | Ally, 0/3 soak, +1 AGI, free draw 1 card after each heal |
| 029 | Chaplain Adama x1 | Asset | Neutral | Ally, 0/3 soak, +1 WIL, free gain 1r after each bless token added |
| 030-031 | Dead Calm x2 | Skill | Neutral | wil/wil, draw 1 on fail |
| 032-033 | Focused Mind x2 | Skill | Neutral | int/int, draw 1 on success |
| 034 | The Undying Will x1 | Skill | Neutral | wil/int/wld, no rules text |

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
- Profile: ✅ Eleanor-Heart-Profile.md created
- Card Data: ✅ Eleanor-Heart-Card-Data.md created
- Art Prompts: ✅ RYP-EH-Art-Prompts.md written
- Strange Eons: ⬜ Not yet built
- Art: 6 REF images in art folder (000-REF-Eleanor-Heart-1 through 6)

### Key Design Decisions — LOCKED
| Decision | Value |
|---|---|
| Class | Mystic primary |
| COM | 1 (Strange Eons minimum, she won't fight) |
| HP | 10 — scales healing power as she takes damage |
| Healing scale | +1 bonus per 3 damage on Eleanor |
| No weapons | No Weapon cards level 1-5 enforced |
| Medical Bag slot | Hand slot |
| Innsmouth Codex slot | Accessory slot |
| Triage slot | Arcane slot |
| Fort Warren Chapel slot | Arcane slot |
| Innsmouth Lessons slot | Arcane slot |
| Army Resupply | Fast, replenish up to 3 charges, neutral |
| Parker soak | 0 HP / 3 SAN |
| Adama soak | 0 HP / 3 SAN |

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
- Profile page: ✅ Ephraim-Archer-Profile.md

---

## Bjorn Blackcast (RYP-BB) — IN PROGRESS 🔧

- Mystic, WIL 5 / INT 3 / COM 2 / AGI 3, HP 6 / SAN 10
- Subtitle: The Mist Borne. Traits: Shaman. Runebearer.
- Ability: Exhaust Rune asset → reveal 2 tokens, choose 1
- Elder Sign: +3. Heal 1 horror.
- 001-024 EON/PNG built and correctly named
- Art 001-024 generated and named
- 025-037 not yet built in Strange Eons
- Art prompts for 025-037 written, not yet generated
- WIL max: Base 5 + Staff +1 + Helm +1 + Thor's Honor +1 = WIL 8

---

## Alistair Greystoke (RYP-AG) — COMPLETE ✅

- Seeker, WIL 3 / INT 5 / COM 3 / AGI 2, HP 7 / SAN 7
- Subtitle: The Immortal Scholar. Traits: Detective. Scholar. Antiquarian.
- 034 folders, all clean. Missing art: 004 My Glass is Nearly Run.
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
- 34 folders, all clean. PNGs deleted — ready for regen.
- Hound of the Deep art: new prompt written — needs generation.
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
- [ ] Build Eleanor Heart in Strange Eons (001-034)
- [ ] Build Bjorn Blackcast 025-037 in Strange Eons (37 .eon, 1 missing)
- [ ] Write RYP-BB Master Catalogue
- [ ] Generate art for Bjorn 025-037
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
| Army Resupply | Replenish up to 3 charges, fast, neutral |
| Parker soak | 0 HP / 3 SAN |
| Adama soak | 0 HP / 3 SAN |

---

## Emergency Context — If AI Has No Memory

If you are reading this with no prior context:
- This is a custom Arkham Horror LCG expansion project
- The user is Edward (GitHub: knowltonem)
- Eight investigators designed, six complete or near-complete
- Current priority: Build Eleanor Heart and Bjorn Blackcast in Strange Eons
- Read individual investigator sections above for full card details
- Ask the user what they want to work on — do not assume
- Claude is primary AI, you are backup — maintain all standards
