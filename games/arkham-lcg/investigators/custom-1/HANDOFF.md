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
Latest commit: `28f3eab` → main

---

## Repository Structure

```
games/arkham-lcg/investigators/custom-1/
├── HANDOFF.md                          ← YOU ARE HERE
├── Jonathan Ironhide/                  ← COMPLETE ✅ needs PNG regen
├── Alistair Greystoke/                 ← COMPLETE ✅ needs PNG regen
├── Agnes Crane/                        ← COMPLETE ✅ all 35 cards built — 020 needs rebuild
├── Abel Redcloud/                      ← COMPLETE ✅ all 36 folders, 30 deck cards, EON verified
├── Nora Warwick/                       ← COMPLETE ✅ all 39 folders, 28 deck cards, EON verified
├── Bjorn Blackcast/                    ← COMPLETE ✅ all 37 cards built
├── Ephraim Archer/                     ← COMPLETE ✅ 035 needs Strange Eons build
├── Eleanor Heart/                      ← IN PROGRESS 🔧 deck designed, not yet built
└── The Man in Black/                   ← COMPLETE ✅ all 34 cards built, EON verified
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

### Source of Truth
**Individual Card-Data.md files are the source of truth for each investigator.** The Master Catalogue (RYP-XX-Master-Catalogue.md) must be updated to match the Card-Data.md file. Card-Data.md may be updated by the user at any time — always re-read it before making changes.

| Investigator | Card-Data File | Master Catalogue |
|---|---|---|
| Abel Redcloud | `Abel Redcloud/Abel-Redcloud-Card-Data.md` | `Abel Redcloud/` (no MC yet) |
| Nora Warwick | `Nora Warwick/Nora-Warwick-Card-Data.md` | `Nora Warwick/RYP-NW-Master-Catalogue.md` |
| Eleanor Heart | `Eleanor Heart/Eleanor-Heart-Card-Data.md` | (no MC yet) |
| Agnes Crane | `Agnes Crane/Agnes-Crane-Card-Data.md` | (no MC yet) |
| Bjorn Blackcast | (check folder) | (check folder) |
| Ephraim Archer | (check folder) | (check folder) |
| Jonathan Ironhide | (check folder) | (check folder) |
| Alistair Greystoke | (check folder) | (check folder) |
| The Man in Black | (check folder) | (check folder) |

### PNG Handling
- NEVER delete PNG files from card folders unless explicitly told to
- Only rename PNGs to convention, never delete them
- Strange Eons re-exports constantly — rename not delete

### Git Workflow
```
git -C "C:\Users\edwar\Documents\games\board-game-vault" add -A
git -C "C:\Users\edwar\Documents\games\board-game-vault" commit -m "Description"
git -C "C:\Users\edwar\Documents\games\board-game-vault" push
```

### EON Reading Method
EON files are binary Java serialized objects. Extract text using PowerShell:
```powershell
$bytes = [System.IO.File]::ReadAllBytes($eon.FullName)
$text = [System.Text.Encoding]::UTF8.GetString($bytes)
# Search for: Rulest, Traitst, Subtitlet, Flavort, Staminat, Sanityt, Intellectt, Combatt, Agilityt, Willpowerq, Costt
```
EON files are the SOURCE OF TRUTH — always verify Card-Data.md against EON files.

---

## Pack Codes

| Investigator | Pack Code | Class | Status |
|---|---|---|---|
| Jonathan Ironhide | RYP-JI | Guardian | ✅ Complete — needs PNG regen |
| Alistair Greystoke | RYP-AG | Seeker | ✅ Complete — needs PNG regen |
| Agnes Crane | RYP-AC | Survivor | ✅ COMPLETE — 35 cards built — 020 needs rebuild (wrong rules) |
| Abel Redcloud | RYP-AR | Guardian | ✅ COMPLETE — 36 folders, 30 deck cards, EON verified |
| Nora Warwick | RYP-NW | Rogue | ✅ COMPLETE — 39 folders, 28 deck cards, EON verified |
| Bjorn Blackcast | RYP-BB | Mystic | ✅ COMPLETE — all 37 cards built |
| Ephraim Archer | RYP-EA | Guardian | ✅ Complete — 035 needs build |
| Eleanor Heart | RYP-EH | Mystic | 🔧 Deck designed, not yet built |
| The Man in Black | RYP-MB | Rogue | ✅ COMPLETE — all 34 cards built, EON verified |

---

## Investigator Stats (EON VERIFIED)

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

## ABEL REDCLOUD (RYP-AR) — COMPLETE ✅ (EON VERIFIED)

- Guardian, WIL 4 / INT 2 / COM 4 / AGI 3, HP 8 / SAN 7
- Subtitle: The Last Keeper. Traits: Warrior. Mystic. Tribal.
- Ability: At the beginning of the Mythos phase: Add 1 bless token to the chaos bag and heal one damage.
- Elder Sign: +1. You may play Sacred Bond.
- Auto-fail: You may play Sacred Wind.
- Cultist: You may play Sacred Strength.
- Deck: 30 cards (007-036). 36 total folders (001-036).
- See Abel-Redcloud-Card-Data.md for full EON-verified deck list.

### Key Cards (EON Verified)
| # | Card | Rules |
|---|---|---|
| 002 | The Sacred Spear | +2 COM +2 dmg. Succeed by 2: +3 dmg instead. |
| 003 | The Tribal Oath | Mythos horror. Spend 3r to discard. |
| 004 | Sacred Bond | Set aside. Elder Sign → +3 INT. 3/3 soak, fades 1/1 per round. |
| 005 | Sacred Wind | Set aside. Auto-fail → +1 all stats. 3/3 soak, fades 1/1 per round. |
| 006 | Sacred Strength | Set aside. Cultist → +2 COM, heal 1 hor/dmg per kill. 3/3 soak, fades. |
| 007 | Teeth of the Deep Ones | Accessory, 1r. +1 WIL. Reduce incoming damage OR horror by 1. |
| 010-011 | Spirit Coyote ×2 | Ally, 2r. +1 COM. 3/1 soak. Retaliate 1 dmg on hit. |
| 035-036 | River of Gold ×2 | Fast. Gain 3 resources. |

---

## NORA WARWICK (RYP-NW) — COMPLETE ✅ (EON VERIFIED)

- Rogue, WIL 3 / INT 5 / COM 3 / AGI 2, HP 7 / SAN 8
- Subtitle: Professor. Traits: Academic. Archaeologist. Blessed.
- Ability: Once per round: Spend 1r to add 1 bless token.
- Elder Sign: +1. Gain resources = shroud value.
- 39 total folders. 28 deck cards (007-036 excl. 019-020 Sand Veil removed).
- Signature cards shuffled in: 002-006 (Collection, Debt, 3 Allies), 037-039 (3 Soak Attachments).
- See Nora-Warwick-Card-Data.md for full EON-verified deck list.

### Key Cards (EON Verified)
| # | Card | Rules |
|---|---|---|
| 002 | Warwick Collection | 0r. +1 INT. [act] Exhaust: evade enemy without testing, no AoO. |
| 003 | Family Debt | Half doom threshold (min 3r) or take dmg/hor. 5r to discard. |
| 004 | Ra-Night-Gaunt | 0r, 3/1 soak. +1 COM. On defeat: 1 dmg each enemy at location. |
| 005 | Call of Anubis | 3r, 1/4 soak. +1 WIL. Forced absorb 1 from 2+ dmg/hor hits. |
| 006 | Horus Heresy | 2r, 2/3 soak. +1 INT +1 AGI. Heals 1 hor per clue discovered. |
| 009 | Sekhem Sceptre | Arcane slot, 2r. +1 COM +1 dmg. Cancel next horror this round. |
| 019-020 | Power of the Ancients ×2 | NEW. Skill WIL/WIL. Max 1 per test. Draw 1 on success. |

---

## THE MAN IN BLACK (RYP-MB) — COMPLETE ✅ (EON VERIFIED)

- Rogue, WIL 3 / INT 3 / COM 4 / AGI 4, HP 7 / SAN 7
- Subtitle: Arkham Underground. Traits: Criminal. Operative.
- Ability: At start of turn: Spend any resources, choose 1 stat, per 2r = +1 to that stat until end of round.
- Elder Sign: +1. Gain 3 resources.
- 2 Ally slots. No Arcane slot. No Spell cards.
- Permanents: The Fixer (Body), Cash in the Bag (Accessory) — start in play outside deck.
- Deck: 30 cards (005-034).
- See Man-in-Black folder for full deck list.

### Key Cards (EON Verified)
| # | Card | Rules |
|---|---|---|
| 002 | The Fixer | Permanent. Body. [act] Exhaust: Fight +2 COM 3 damage. Kill: gain 2r. |
| 003 | Cash in the Bag | Permanent. Accessory. Start of turn: gain 1r. |
| 004 | Sneaky Pete | Weakness. Take 2 horror. Spawn at location. While in play: cannot gain resources. |
| 022-023 | Lights Out ×2 | 2r. [act] Fight +1 COM. Each enemy takes 2 dmg. Take 1 horror. |
| 031 | I Know A Guy | 2r. Search deck for any asset, play it at 0 cost. |

---

## AGNES CRANE (RYP-AC) — COMPLETE ✅

- Survivor, WIL 4 / INT 3 / COM 1 / AGI 4, HP 8 / SAN 8
- Subtitle: The Haunted One. Traits: Mystic. Cursed. Survivor.
- Ability: Once per round: Reveal top 2 encounter cards. Return 1 to top, 1 to bottom.
- Elder Sign: +1. Rearrange top 3 encounter cards in any order.
- 35 total folders (001-035). 30 deck cards (006-035).
- ⚠️ KNOWN ISSUE: Card 020 (Drawn to the Flame) has wrong rules text in EON — says "investigate +2 INT" but should say "draw top encounter card, discover 2 clues." Needs rebuild in Strange Eons.

### Key Cards (EON Verified)
| # | Card | Rules |
|---|---|---|
| 002 | The Night-Gaunt | Ally 3r. 3/2 soak. +1 WIL. [rea] prevent 1 horror on exhaust + deal 1 dmg. |
| 003 | The Haunted Veil | Accessory 0r. 0/3 soak. [rea] Reduce horror by 1 AND deal 1 dmg to enemy. |
| 004 | The Voice Below | Weakness. Revelation horror. Mythos horror. [act] WIL(4) to discard. |
| 034 | Storm of Spirits | 3r. [act] Fight +1 WIL using WIL. Succeed: 2 dmg each enemy at location. |
| 035 | Salem's Lot | Hand 0r. Unique. [rea] After discard weakness: gain 2r. |

---

## BJORN BLACKCAST (RYP-BB) — COMPLETE ✅

- Mystic, WIL 5 / INT 3 / COM 2 / AGI 3, HP 6 / SAN 10
- Subtitle: The Mist Borne. Traits: Shaman. Runebearer.
- All 37 folders clean. All EON/PNG built and correctly named.

---

## ALISTAIR GREYSTOKE (RYP-AG) — COMPLETE ✅

- Seeker, WIL 3 / INT 5 / COM 3 / AGI 2, HP 7 / SAN 7
- Subtitle: The Immortal Scholar. Traits: Detective. Scholar. Antiquarian.
- Missing art: 004 My Glass is Nearly Run — needs generation.

---

## JONATHAN IRONHIDE (RYP-JI) — COMPLETE ✅

- Guardian, WIL 3 / INT 2 / COM 5 / AGI 3, HP 9 / SAN 7
- PNGs need regen. Hound of the Deep art needs generation.

---

## EPHRAIM ARCHER (RYP-EA) — COMPLETE ✅

- Guardian, WIL 3 / INT 2 / COM 5 / AGI 3, HP 7 / SAN 8
- Subtitle: The Wanderer. Traits: Sell Sword.
- Ability: Spend 1r → +2 to any skill test once per round.
- Folder 035 needs Strange Eons build.

---

## ELEANOR HEART (RYP-EH) — IN PROGRESS 🔧

- Mystic, WIL 4 / INT 4 / COM 1 / AGI 4, HP 10 / SAN 7
- Subtitle: The Undying. Traits: Medic. Scholar.
- Ability: After card heals dmg/hor: +1 bonus heal per 3 damage on Eleanor.
- Folders 001-034 created. Not yet built in Strange Eons.

---

## Pending Items

### Immediate Priority
- [ ] Agnes 020 Drawn to the Flame — rebuild in Strange Eons (wrong rules text in EON)
- [ ] Build Eleanor Heart in Strange Eons (001-034)
- [ ] Build Ephraim Archer 035 in Strange Eons
- [ ] Regen PNGs for Ironhide, Greystoke
- [ ] Generate art for Greystoke 004 My Glass is Nearly Run

### Completed This Session
- [x] Abel Redcloud full EON verification and Card-Data rewrite
- [x] Nora Warwick full EON verification and Card-Data rewrite
- [x] Abel Teeth of the Deep Ones — now reduces damage OR horror by 1
- [x] Abel Spirit Coyote — cost reduced from 3r to 2r
- [x] Nora Warwick Collection — redesigned as free evade, no economy
- [x] Nora Sekhem Sceptre — moved to Arcane slot
- [x] Nora Horus Heresy — cost reduced from 4r to 2r
- [x] Nora Sand Veil ×2 — removed, replaced by Power of the Ancients ×2 (WIL/WIL skill)
- [x] Nora Power of the Ancients — new card 019-020, WIL/WIL, draw 1 on success
- [x] Art cleanup — all 4 investigators clean, unused art removed
- [x] Full folder audit — MiB, Nora, Abel, Agnes all verified clean

---

## Key Design Decisions — DO NOT REVERSE

| Decision | Value |
|---|---|
| Abel Sacred Spear | No bless generation. +2 COM +2 dmg, +3 on succeed by 2 |
| Abel Tribal Oath | Spend 3r to discard (not WIL test) |
| Abel Spirit Coyote | Cost 2r, soak 3/1, +1 COM, retaliate 1 dmg |
| Abel Teeth | Accessory, 1r, +1 WIL, reduce damage OR horror by 1 |
| Abel set-asides | Bond=Elder Sign, Wind=Auto-fail, Strength=Cultist. All 3/3 soak, fade 1+1/round |
| Nora ability | Spend 1r → 1 bless (once per round) |
| Nora Warwick Collection | Free evade (exhaust, no test, no AoO). No economy. 0r cost. |
| Nora Sekhem Sceptre | Arcane slot (not Hand) |
| Nora Horus Heresy | Cost 2r |
| Nora Sand Veil | REMOVED — replaced by Power of the Ancients |
| Nora Power of the Ancients | WIL/WIL skill, max 1 per test, draw 1 on success |
| Nora deck structure | 007-036 = 28 deck cards. 002-006+037-039 = 8 signature cards shuffled in |
| MiB The Fixer | Permanent, Body, exhaust fight +2 COM 3 damage, kill = 2r |
| MiB Cash in the Bag | Permanent, Accessory, gain 1r per turn |
| MiB deck size | 30 cards (005-034) |
| MiB 2 ally slots | Built into investigator card |
| MiB no Arcane | No arcane slots, no spell cards |
| Agnes ability | Reveal top 2 encounter cards, return 1 top 1 bottom |
| Agnes Elder Sign | +1. Rearrange top 3 encounter cards |
| Agnes COM | 1 (Strange Eons minimum) |
| Agnes HP/SAN | 8/8 |

---

## Simulation Results (EON Verified Card Data)

### Abel + Nora vs Spreading Flames — ✅ VICTORY Round 9 (88.5% win rate over 200 games)
- Servant of Flame defeated (6 HP, fight 4)
- Nora Warwick INT5 excellent at investigating (shroud 2-3 locations)
- Abel WIL4/COM4 strong at fighting and mythos resilience
- Bless tokens from both investigators' abilities stack effectively
- AI learns to move between locations for clues

### Previous sim (Midnight Masks) — ✅ VICTORY Round 8
- Doom 8/11. All 4 cultists found.
- Bless 16 tokens, 0 curse.
- All 3 Abel set-asides appeared.
- Teeth reduced Conglomeration attack to 0 dmg + 0 hor.
- Spirit Coyote (2r) killed Swarm of Rats by retaliation alone.
- Horus Heresy (2r) played Round 1 — decisive INT boost all game.

### Previous sim (Museum) — ❌ DEFEAT Round 3 (worst-case spawn)
- Museum Curator + Hunting Horror both spawned Round 1.
- Abel no defensive assets in opening hand — died Round 3.
- Not a card balance issue — variance/spawn issue.

---

## Game Simulator (Python CLI)

A Python-based game simulator for testing custom investigators against scenarios.

**Location:** `simulator/` (inside `arkham-lcg/`)

### Quick Start
```bash
cd simulator
py run.py simulate -i abel_redcloud,nora_warwick -s spreading_flames
py run.py simulate -i abel_redcloud,nora_warwick -s spreading_flames -n 100  # Monte Carlo
py run.py list-investigators
py run.py list-scenarios
```

### Tech Stack
- Python 3.14, Click (CLI), Rich (display), PyYAML (config)
- JSON data files for investigators and scenarios
- Game logs saved to `simulator/logs/`

### Architecture
- `engine/models.py` — Card, Investigator, Enemy, Location, Agenda, Act, GameState
- `engine/chaos_bag.py` — Token draw, bless/curse management
- `engine/skill_test.py` — Skill test resolution
- `engine/combat.py` — Fight and evade resolution
- `engine/phases.py` — Mythos, Investigation, Enemy, Upkeep phases
- `engine/game.py` — Main game loop, win/loss conditions
- `engine/ai_player.py` — Priority-based AI decision making
- `engine/effects.py` — Card effect processing framework
- `cli/main.py` — Click CLI commands
- `cli/display.py` — Rich display helpers

### Current State
- ✅ Full game loop working (all 4 phases)
- ✅ Abel Redcloud + Nora Warwick JSON data loaded
- ✅ Spreading Flames scenario (5 locations, encounter deck, 3 agendas/acts)
- ✅ Servant of Flame boss spawns on Agenda 1 advance
- ✅ AI moves between locations to gather clues
- ✅ Monte Carlo simulation (-n flag)
- ✅ 88.5% win rate over 200 games (Abel + Nora vs Spreading Flames)
- 🔧 Card effects framework (effects.py) — skeleton only
- 🔧 Deck builder — placeholder
- ⬜ Campaign mode (trauma/XP between scenarios)
- ⬜ Additional investigators and scenarios
