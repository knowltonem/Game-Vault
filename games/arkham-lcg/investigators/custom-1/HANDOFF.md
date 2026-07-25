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
Latest commit: `00ef1a9` → main

---

## Repository Structure

```
games/arkham-lcg/investigators/custom-1/
├── HANDOFF.md                          ← YOU ARE HERE
├── Jonathan Ironhide/                  ← COMPLETE ✅ needs PNG regen
├── Alistair Greystoke/                 ← COMPLETE ✅ needs PNG regen
├── Agnes Crane/                        ← COMPLETE ✅ all 35 cards built
├── Abel Redcloud/                      ← COMPLETE ✅ needs PNG regen
├── Nora Warwick/                       ← COMPLETE ✅
├── Bjorn Blackcast/                    ← COMPLETE ✅ all 37 cards built
├── Ephraim Archer/                     ← COMPLETE ✅ 035 needs Strange Eons build
├── Eleanor Heart/                      ← IN PROGRESS 🔧 deck designed, not yet built
├── The Man in Black/                   ← COMPLETE ✅ all 34 cards built
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
| Agnes Crane | RYP-AC | Survivor | ✅ COMPLETE — all 35 cards built |
| Abel Redcloud | RYP-AR | Guardian | ✅ Complete — needs PNG regen |
| Nora Warwick | RYP-NW | Rogue | ✅ Complete |
| Bjorn Blackcast | RYP-BB | Mystic | ✅ COMPLETE — all 37 cards built |
| Ephraim Archer | RYP-EA | Guardian | ✅ Complete — 035 needs build |
| Eleanor Heart | RYP-EH | Mystic | 🔧 Deck designed, not yet built |
| The Man in Black | RYP-MB | Rogue | ✅ COMPLETE — all 34 cards built |

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
| Agnes Crane | 4 | 3 | 1 | 4 | 8 | 8 |
| Abel Redcloud | 4 | 2 | 4 | 3 | 8 | 7 |
| Nora Warwick | 3 | 5 | 3 | 2 | 7 | 8 |
| Bjorn Blackcast | 5 | 3 | 2 | 3 | 6 | 10 |
| Ephraim Archer | 3 | 2 | 5 | 3 | 7 | 8 |
| Eleanor Heart | 4 | 4 | 1 | 4 | 10 | 7 |
| The Man in Black | 3 | 3 | 4 | 4 | 7 | 7 |

---

## THE MAN IN BLACK (RYP-MB) — COMPLETE ✅

### Backstory
A quiet, pale, sad-looking man who is unmistakably dangerous. Nobody knows his real name. He moves through Arkham's underground economy with absolute authority — cash in hand, shotgun on his back, contacts everywhere. Born in Arkham. Raised in its alleys. He never left because he never needed to. The underground was his from the start. Now something has changed in Arkham — things coming through that don't respond to cash, don't honour debts, don't understand the rules. They are bad for business. Not on his watch.

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
| Ability | At the start of the round: You may spend any number of resources. Choose 1 skill (WIL, INT, COM, or AGI). For each 2 resources spent, get +1 to that skill until the end of the round. |
| Elder Sign | +1. Gain 3 resources. |
| Deckbuilding | Rogue cards level 0-5, Neutral cards level 0-5, up to 15 Guardian cards level 0-1. No Spell cards of any level. No Arcane assets. You have 2 Ally slots instead of 1. |
| Requirements | The Fixer x1, Cash in the Bag x1, Sneaky Pete x1, 1 random basic weakness. |
| Pack Code | RYP-MB |

### Signature Cards (Permanents — start in play, outside deck)
| # | Card | Type | Slot | Rules Text |
|---|---|---|---|---|
| 002 | The Fixer | Permanent Asset | Body | Permanent. MiB only. [action] Exhaust: Fight. +2 COM. 3 damage. After defeat: Gain 2r. No icons. |
| 003 | Cash in the Bag | Permanent Asset | Accessory | Permanent. MiB only. At start of your turn: Gain 1 resource. No icons. |
| 004 | Sneaky Pete | Enemy Weakness | — | Revelation: Take 2 horror. Spawn Sneaky Pete at your location. While in play: Cannot gain resources. Subtitle: Double Crossed. Fight 3 / Evade 4 / HP 3 / 1 dmg 1 horror. Hunter. Retaliate. Flavor: "I should've known." |

### Full Deck — 30 Cards (005-034)

| # | Card | Type | Class | Cost | Icons | Rules Text |
|---|---|---|---|---|---|---|
| 005-006 | The Saturday Night Special x2 | Asset — Hand | Rogue | 3r | com/com | Uses (4 ammo). [action] Spend 1 ammo: Fight. +1 COM. +1 damage. Subtitle: Meat in the Pot. Flavor: "Let it cook." |
| 007-008 | Cash Flow x2 | Event | Rogue | 0r | wld | Fast. Gain 3 resources. Subtitle: Arkham Underground Standard. Flavor: "The underground has its own economy. He runs most of it." |
| 009-010 | The Sure Thing x2 | Skill | Rogue | — | wld/com | If successful: Gain 3 resources. Subtitle: Arkham Odds. Flavor: "The odds are always in his favour." |
| 011-012 | Old Habit x2 | Asset | Neutral | 1r | wld/wil | [action] Exhaust + take 1 horror: Heal 2 damage from any investigator at your location. Subtitle: Lit Up. Flavor: "He lights it after every job. Win or lose." |
| 013 | It's Time x1 | Asset — No Slot | Neutral | 4r | int/wld | +1 AGI and +1 INT while in play. [free] End of round: Heal 1 horror from yourself. Subtitle: Pocket Watch. Flavor: "Arkham runs on its own clock." |
| 014 | Big Tommy x1 | Asset — Ally | Rogue | 3r | com/wld | +1 AGI. 3/0 soak. [reaction] When you would take damage from enemy attack: Exhaust Big Tommy — he takes it instead. Subtitle: He Takes The Hit. Flavor: "Tommy is paid well." |
| 015 | Old Man Winters x1 | Asset — Ally | Neutral | 3r | wil/wld | +1 WIL. 2/2 soak. [reaction] When you would take damage or horror: Exhaust Old Man Winters — he takes it instead. Subtitle: From the Old Neighbourhood. Flavor: "He's seen the neighbourhood change." |
| 016-017 | 5 Card Stud x2 | Skill | Rogue | — | wld/wld | No rules text. Subtitle: Arkham Rules. Flavor: "I Don't Lose." |
| 018-019 | Point Blank x2 | Skill | Rogue | — | com/com | If successful while fighting: Deal +1 damage. Subtitle: Dead to Rights. Flavor: "At this range, even the Old One can't save you." |
| 020 | Arkham Underground x1 | Event | Rogue | 0r | agi/int | Fast. Choose asset you control with uses (ammo, secrets, or charges). Fully replenish uses to starting value. Subtitle: Call in a Favour. Flavor: "One call. Whatever he needs. No questions." |
| 021 | Informant x1 | Event | Rogue | 1r | int/int | Fast. Draw 2 cards. Subtitle: Arkham Never Sleeps. Flavor: "By the time you hear it, he already knew." |
| 022-023 | Lights Out x2 | Event | Rogue | 2r | int/wil | [action] Fight. +1 COM. Each enemy at your location takes 2 damage. You take 1 horror. Subtitle: You're Going Down. Flavor: "Let's be done with this job." |
| 024-025 | Not My Problem x2 | Event | Rogue | 1r | wil/wld | Fast. Cancel effects of a non-weakness treachery just drawn. Take 1 horror. Subtitle: Arkham Underground Policy. Flavor: "He's seen worse. Not worried." |
| 026-027 | Casing the Joint x2 | Event | Rogue | 1r | agi/agi | [action] Investigate using AGI instead of INT. If succeed: Discover 1 additional clue. Subtitle: Arkham Instinct. Flavor: "Every exit. Every face. Every angle. He clocks it all." |
| 028-029 | Up The Sleeve x2 | Event | Rogue | 2r | agi/agi | Fast. Draw 3 cards. Subtitle: Card Shark. Flavor: "He never plays a fair hand." |
| 030 | Trap Door x1 | Event | Rogue | 3r | agi/agi | Fast. Automatically evade an enemy engaged with you. That enemy remains exhausted until end of next round. Move to a connected location. Subtitle: Behind the Bar. Flavor: "He knows every back exit in Arkham. This one is his favourite." |
| 031 | I Know A Guy x1 | Event | Rogue | 2r | wld | Search your deck for any Asset and play it, reducing cost to 0. Shuffle your deck. Subtitle: Arkham Underground Delivery. Flavor: "Whatever he needs. Whoever has it. One call." |
| 032-033 | Pray for Me Father x2 | Asset | Neutral | 3r | wil/wld | Uses (4 supplies). [action] Spend 1 supply: Choose an investigator at your location to heal 1 horror. Then that investigator tests WIL (2). If succeed: Heal 1 additional horror. Subtitle: Last Rites. Flavor: "Father, forgive me." |
| 034 | Arkham Underground x2 | Event | Rogue | 0r | agi/int | (Same as 020 — second copy) |

### Icon Distribution (Final)
| Stat | Count |
|---|---|
| wld | 16 |
| com | 12 |
| agi | 14 |
| wil | 8 |
| int | 4 |

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

### Build Status
| Item | Status |
|---|---|
| Folders 001-034 | ✅ All created and correctly named |
| EON files | ✅ All built in Strange Eons |
| PNG files | ✅ All exported and correctly named |
| Art files | ✅ All generated |
| REF files | ✅ All correctly named |
| Quick Look | ✅ RYP-MB-001 in Quick Look folder |

### Key Design Decisions — LOCKED
| Decision | Value |
|---|---|
| The Fixer | Permanent, Body slot, no icons, exhaust fight +2 COM 3 damage, kill = 2r |
| Cash in the Bag | Permanent, Accessory slot, no icons, gain 1r per turn |
| Both Permanents | Start in play, outside deck, no skill icons |
| Deck size | 30 cards (005-034) |
| 2 Ally slots | Built into investigator card |
| No Arcane | Restriction — no arcane slots, no spell cards |
| Ability | Declared at START OF THE ROUND — choose stat, spend resources |
| Sneaky Pete | HP 3, fight 3, evade 4, Hunter, Retaliate, blocks all resource gain |
| It's Time | Cost 4r, no slot, +1 AGI +1 INT, heal 1 horror per round |
| Lights Out | [action] fight +1 COM, AoE 2 damage all enemies, take 1 horror, icons int/wil |
| Arkham Underground | x2 (020 and 034), fast, fully replenish any asset uses |
| Trap Door | Cost 3r, fast, auto-evade, enemy stays exhausted next round, move |
| Pray for Me Father | Cost 3r, reskin Liquid Courage, SAN heal |
| Saturday Night Special | Cost 3r, [action] spend 1 ammo, fight +1 COM, +1 damage |

### Best Pairings
| Partner | Rating | Why |
|---|---|---|
| Nora Warwick | ⭐⭐⭐⭐⭐ | Bless engine scales his ability |
| Bjorn Blackcast | ⭐⭐⭐⭐⭐ | Token control makes resource spending reliable |
| Alistair Greystoke | ⭐⭐⭐⭐⭐ | Perfect role split |
| Eleanor Heart | ⭐⭐⭐⭐ | Unique damage-taking dynamic |
| Agnes Crane | ⭐⭐⭐⭐ | Encounter control + combat |
| Ephraim Archer | ⭐⭐⭐ | Redundant combat |
| Abel Redcloud | ⭐⭐ | No clue engine |

---

## ELEANOR HEART (RYP-EH) — IN PROGRESS 🔧

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
| 002 | Medical Bag | Asset | Hand | Uses 4 charges. Action spend 1 charge: heal 1 dmg or horror any investigator. Reaction after other heal: double it. |
| 003 | The Innsmouth Codex | Asset | Accessory | +1 INT. Action exhaust: investigate INT. Success = +1 clue. Fail = draw 1 card. |
| 004 | The Fog of Innsmouth | Weakness | — | Revelation: take 2 horror, can't self-heal until discarded. Action WIL 4 test to discard. |

### Full Deck (30 cards, 005-034)
| # | Card | Function | Icons |
|---|---|---|---|
| 005-006 | Take What You Need x2 | Search top 7 for any asset | int/wld |
| 007-008 | Special Allowance x2 | Fast gain 3r | wld |
| 009-010 | Last Resort x2 | AoE fight INT or WIL, 2 dmg all enemies, take 1 dmg + 1 horror | wil/int |
| 011-012 | Military Tactics x2 | Fast draw 3 cards | int/int |
| 013-014 | Arcane Practice x2 | Fight WIL, +1 dmg, +1 more on succeed by 2 | int/int |
| 015-016 | Triage x2 | Arcane slot, 5 charges, heal 1 dmg or horror any investigator | wil/wil |
| 017-018 | Patch Up x2 | Fast heal 1 dmg AND 1 horror any investigator | wil/int |
| 019-020 | Fort Warren Chapel x2 | Arcane slot, SAN soak 1, after heal: add 1 bless token | wil/wil |
| 021-022 | Army Resupply x2 | Fast replenish up to 3 charges on any asset | wil/int |
| 023-024 | Do No Harm x2 | Fast cancel treachery, take 1 horror | wil/wil |
| 025-026 | The Codex Revealed x2 | Fast discover 1 clue without investigation | int/int |
| 027 | Innsmouth Lessons x1 | Arcane slot, after successful investigate: discover 1 clue + gain 1r | int/int |
| 028 | Private Parker x1 | Ally, 0/3 soak, +1 AGI, draw 1 card after each heal | agi/wld |
| 029 | Chaplain Adama x1 | Ally, 0/3 soak, +1 WIL, gain 1r after each bless token added | wil/wld |
| 030-031 | Dead Calm x2 | Skill wil/wil, draw 1 on fail | wil/wil |
| 032-033 | Focused Mind x2 | Skill int/int, draw 1 on success | int/int |
| 034 | The Undying Will x1 | Skill wil/int/wld, no rules text | wil/int/wld |

### Build Status
- Folders 001-034: ✅ All created and correctly named
- Strange Eons: ⬜ Not yet built
- Art: ✅ 001 (investigator), 002 (Medical Bag), 003 (Innsmouth Codex), 004 (Fog of Innsmouth), 019 (Fort Warren Chapel), 027 (Innsmouth Lessons), 028 (Private Parker), 029 (Chaplain Adama) correctly named
- Art: ⚠️ 14 files incorrectly labeled as 004 variants — needs cleanup (user will handle later)

---

## EPHRAIM ARCHER (RYP-EA) — COMPLETE ✅

- Guardian, WIL 3 / INT 2 / COM 5 / AGI 3, HP 7 / SAN 8
- Subtitle: The Wanderer. Traits: Sell Sword.
- Ability: Spend 1r → +2 to any skill test once per round
- Elder Sign: +2. Gain 3 resources.
- Folder 035: ⬜ Needs Strange Eons build

---

## BJORN BLACKCAST (RYP-BB) — COMPLETE ✅

- Mystic, WIL 5 / INT 3 / COM 2 / AGI 3, HP 6 / SAN 10
- Subtitle: The Mist Borne. Traits: Shaman. Runebearer.
- Ability: Exhaust Rune asset → reveal 2 tokens, choose 1
- Elder Sign: +3. Heal 1 horror.
- All 37 folders clean. All EON/PNG built and correctly named.
- WIL max: Base 5 + Staff +1 + Helm +1 + Thor's Honor +1 = WIL 8

---

## ALISTAIR GREYSTOKE (RYP-AG) — COMPLETE ✅

- Seeker, WIL 3 / INT 5 / COM 3 / AGI 2, HP 7 / SAN 7
- Subtitle: The Immortal Scholar. Traits: Detective. Scholar. Antiquarian.
- Missing art: 004 My Glass is Nearly Run

---

## JONATHAN IRONHIDE (RYP-JI) — COMPLETE ✅

- Guardian, WIL 3 / INT 2 / COM 5 / AGI 3, HP 9 / SAN 7
- PNGs deleted — ready for regen
- Hound of the Deep art needs generation

---

## AGNES CRANE (RYP-AC) — COMPLETE ✅

- Survivor, WIL 4 / INT 3 / COM 3 / AGI 3, HP 6 / SAN 9
- 5 signature cards (001-005), 30 deck cards (006-034) = 35 total pack cards
- Key fix: Cherished Keepsake corrected to ×1 (006), Leather Coat at 007
- 034: Storm of Spirits — AoE spell, uses WIL instead of COM, costs charges instead of ammo
- Deck review: PENDING

---

## ABEL REDCLOUD (RYP-AR) — COMPLETE ✅

- Guardian, WIL 4 / INT 2 / COM 4 / AGI 3, HP 8 / SAN 7
- Deck review: PENDING

---

## NORA WARWICK (RYP-NW) — COMPLETE ✅

- Rogue, WIL 3 / INT 5 / COM 3 / AGI 2, HP 7 / SAN 8
- 39 folders all clean. Full catalogue written.
- Ability: Once per round: Spend 1r → add 1 bless token
- Elder Sign: +1. Gain resources = shroud value

---

## Pending Items

### Immediate Priority
- [ ] Build Eleanor Heart in Strange Eons (001-034)
- [ ] Build Ephraim Archer 035 in Strange Eons
- [ ] Regen PNGs for Ironhide, Greystoke, Agnes, Abel
- [ ] Write RYP-BB Master Catalogue

### Secondary
- [x] Agnes Crane COMPLETE -- 35 cards built
- [ ] Review Abel Redcloud deck
- [ ] Generate art for Ironhide 007 Hound of the Deep
- [ ] Generate art for Greystoke 004 My Glass is Nearly Run
- [ ] Write Man in Black profile page

---

## Key Design Decisions — DO NOT REVERSE

| Decision | Value |
|---|---|
| Folder naming | One folder per physical card |
| PNG handling | NEVER delete PNGs unless explicitly told to |
| MiB The Fixer | Permanent, Body slot, no icons, exhaust fight +2 COM 3 damage, kill = 2r |
| MiB Cash in the Bag | Permanent, Accessory slot, no icons, gain 1r per turn |
| MiB deck size | 30 cards (005-034) |
| MiB 2 ally slots | Built into investigator card |
| MiB no Arcane | No arcane slots, no spell cards |
| MiB ability | Declared at START OF ROUND, choose stat, per 2r = +1 |
| MiB Sneaky Pete | HP 3, fight 3, evade 4, Hunter, Retaliate, blocks all resource gain |
| MiB It's Time | Cost 4r, no slot, +1 AGI +1 INT, heal 1 horror per round |
| MiB Lights Out | [action] fight +1 COM, AoE 2 damage, take 1 horror, icons int/wil |
| MiB Arkham Underground | x2 (020+034), fast, fully replenish any asset uses, icons agi/int |
| MiB Trap Door | Cost 3r, fast, auto-evade, enemy stays exhausted next round, move |
| MiB Pray for Me Father | Cost 3r, reskin Liquid Courage, SAN heal |
| MiB Saturday Night Special | Cost 3r, [action] spend 1 ammo, fight +1 COM, +1 damage |
| Eleanor class | Mystic primary |
| Eleanor COM | 1 (Strange Eons minimum) |
| Eleanor HP | 10 — scales healing power as she takes damage |
| Eleanor no weapons | No Weapon cards level 1-5 enforced |
| Agnes Storm of Spirits | 034, AoE fight WIL 2 dmg all enemies at location, 3 charges, uses WIL instead of COM, spell asset
| Bjorn ability | Exhaust Rune asset → reveal 2 tokens, choose 1 |
| Ephraim ability | Spend 1r → +2 to any skill test once per round |

---

## Emergency Context — If AI Has No Memory

If you are reading this with no prior context:
- This is a custom Arkham Horror LCG expansion project
- The user is Edward (GitHub: knowltonem)
- Nine investigators designed, seven complete or near-complete
- The Man in Black (RYP-MB) is FULLY COMPLETE — 34 cards, all built, all art done
- Current priority: Build Eleanor Heart and Bjorn Blackcast in Strange Eons
- Read individual investigator sections above for full card details
- Ask the user what they want to work on — do not assume

