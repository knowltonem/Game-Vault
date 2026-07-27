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
Latest commit: `95c2959` → main

---

## Repository Structure

```
games/arkham-lcg/investigators/custom-1/
├── HANDOFF.md                          ← YOU ARE HERE
├── Jonathan Ironhide/                  ← COMPLETE ✅ fully built, EON verified
├── Alistair Greystoke/                 ← COMPLETE ✅ fully built, EON verified
├── Agnes Crane/                        ← COMPLETE ✅ 020 needs rebuild (wrong rules in EON)
├── Abel Redcloud/                      ← COMPLETE ✅ EON verified, Wendigo added (037)
├── Nora Warwick/                       ← COMPLETE ✅ EON verified
├── Bjorn Blackcast/                    ← COMPLETE ✅ all 37 cards built
├── Ephraim Archer/                     ← COMPLETE ✅ 035 needs Strange Eons build
├── Eleanor Heart/                      ← IN PROGRESS 🔧 deck designed, not yet built
└── The Man in Black/                   ← COMPLETE ✅ EON verified
```

---

## Standing Rules — NEVER VIOLATE

### Naming Conventions
| File Type | Convention | Example |
|---|---|---|
| Folders | `###-Card-Name` | `006-The-Red-Blade` |
| EON files | `RYP-XX-###-Card-Name.eon` | `RYP-JI-005-Kings-Talon.eon` |
| PNG exports Front | `RYP-XX-###-Card-Name-Front.png` | `RYP-JI-005-Kings-Talon-Front.png` |
| PNG exports Back | `RYP-XX-###-Card-Name-Back.png` | `RYP-JI-005-Kings-Talon-Back.png` |
| Art files | `RYP-XX-###-Card-Name-Art.png` | `RYP-JI-005-Kings-Talon-Art.png` |
| REF images | `000-REF-Description.png` | `000-REF-Ironhide-Concept-1.png` |
| Mini folders | `[Name]-mini` inside 001 folder | `Ironhide-mini/` |
| Mini EON | `[Name]-Mini-Marker.eon` | `Ironhide-Mini-Marker.eon` |

### Mini Marker Rule
Every 001 investigator folder SHALL contain a `[Name]-mini` subfolder with a `[Name]-Mini-Marker.eon` file.

### Source of Truth
EON files are the SOURCE OF TRUTH. Always verify Card-Data.md against EON files, not the other way around.

### PNG Handling
- NEVER delete PNG files from card folders unless explicitly told to
- Only rename PNGs to convention, never delete them
- Signature cards shuffle into deck and do NOT count toward deck size (30 cards)

### Git Workflow
```powershell
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

---

## Pack Codes

| Investigator | Pack Code | Class | Status |
|---|---|---|---|
| Jonathan Ironhide | RYP-JI | Guardian | ✅ Complete — fully built and verified |
| Alistair Greystoke | RYP-AG | Seeker | ✅ Complete — fully built and verified |
| Agnes Crane | RYP-AC | Survivor | ✅ Complete — 020 needs EON rebuild |
| Abel Redcloud | RYP-AR | Guardian | ✅ Complete — Wendigo (037) added |
| Nora Warwick | RYP-NW | Rogue | ✅ Complete |
| Bjorn Blackcast | RYP-BB | Mystic | ✅ Complete |
| Ephraim Archer | RYP-EA | Guardian | ✅ Complete — 035 needs build |
| Eleanor Heart | RYP-EH | Mystic | 🔧 Deck designed, not yet built |
| The Man in Black | RYP-MB | Rogue | ✅ Complete — EON verified |

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

## JONATHAN IRONHIDE (RYP-JI) — COMPLETE ✅

- Guardian, WIL 3 / INT 2 / COM 5 / AGI 3, HP 9 / SAN 7
- Subtitle: The R'lyeh Survivor. Traits: Hunter. Cursed.
- **Ability:** [rea] After you defeat an enemy: Gain 1 resource and deal 1 damage to each enemy at your location. (Limit once per round.)
- **Elder Sign:** +1. Draw 1 card and gain 1 resource.
- **Requirements:** Hollow Warden ×1, Hydra Hyde ×1, Echoes of R'lyeh ×1, 1 random Basic Weakness.
- 34 total folders. 30 deck cards (005-034).

### Key Cards
| # | Card | Rules |
|---|---|---|
| 002 | The Hollow Warden | Cost 0, Hand, 3 ammo. +2 COM +1 dmg, draw on kill. Reload 2r=2 ammo. Free +1 ammo on empty. |
| 003 | Hydra Hyde | Cost 2, Body, 3/3 soak. Reduce dmg or hor by 1. Spend 2r to shuffle back into deck on discard. |
| 004 | Echoes of R'lyeh | Weakness. Revelation: 2 horror. After kill: 1 horror. Spend 4r to discard. |
| 005-006 | King's Talon ×2 | Cost 2, Hand, COM/COM icons. +2 COM +1 dmg. [cur]=+2 dmg. Kill=heal 1 hor. +1 COM per dmg on target (max +3). |
| 007-008 | Hound of the Deep ×2 | Cost 3, Ally, 3/1 soak, AGI/AGI icons. +1 COM. Exhaust: deal 1 dmg to attacking enemy. |
| 009-010 | Luck of the Draw ×2 | Skill, INT/INT/INT icons. When you would discover 1 clue during this test, instead discover 2. |
| 021-022 | Premonitions ×2 | Cost 1, AGI/AGI icons. Search top 9 for Weapon asset. |

---

## ALISTAIR GREYSTOKE (RYP-AG) — COMPLETE ✅

- Seeker, WIL 3 / INT 5 / COM 3 / AGI 2, HP 7 / SAN 7
- Subtitle: The Immortal Scholar. Traits: Detective. Scholar. Antiquarian.
- **Ability:** [rea] After you successfully investigate: Draw 1 card and gain 1 resource. (Limit once per round.)
- **Elder Sign:** +1. Search your deck for any Tome, Relic, or Codex asset. Play it for free. Shuffle your deck.
- **Requirements:** Wisdom of Antiquity ×1, The Unbroken Codex ×1, The Collector's Ledger ×1, My Glass is Nearly Run ×1, The Greystoke Tomb ×1, Arkham Scrolls ×1, 1 random Basic Weakness.
- 37 total folders. 30 deck cards (008-037).

### Key Cards
| # | Card | Rules |
|---|---|---|
| 002 | Wisdom of Antiquity | Cost 0, no slot. +1 INT. Enter play: search Tome. Exhaust: free re-investigate. |
| 003 | The Unbroken Codex | Cost 1, Arcane, 2 SAN soak. Use INT for AGI on evade. Exhaust: ignore 1 horror. |
| 004 | The Collector's Ledger | Cost 1, Arcane, 1 SAN soak. After drawing from ability: gain 2r. |
| 005 | My Glass is Nearly Run | Weakness. End of upkeep: take 1 horror. Spend 3 clues to discard. |
| 006 | The Greystoke Tomb | Cost 2, Hand, AGI/AGI/AGI icons. Mythos: 4+ cards=+2r, 7+=heal 1 hor, 10+=heal 1 dmg. |
| 007 | Arkham Scrolls | Cost 2, Hand, INT/INT icons. Start of your turn: draw 1 card. |
| 008 | The Ancient Binding | Cost 3, Body, 3/3 soak. Defeated: return to deck and shuffle. |
| 009 | The Relic Harvester | Cost 2, Ally, 2/2 soak. Gain 1r per successful investigate. Exhaust: search top 5 for asset. |
| 010 | My Eyes and Ears | Cost 2, Ally, 1/3 soak. +1 clue per successful investigate. Defeat: place 1 doom. |
| 011 | The Summoner's Deck | Cost 2, Accessory. +1 ally slot. 2 unique allies simultaneously. Exhaust: shuffle defeated ally back. |

---

## ABEL REDCLOUD (RYP-AR) — COMPLETE ✅

- Guardian, WIL 4 / INT 2 / COM 4 / AGI 3, HP 8 / SAN 7
- Subtitle: The Last Keeper. Traits: Warrior. Mystic. Tribal.
- **Ability:** At the beginning of the Mythos phase: Add 1 bless token to the chaos bag.
- **Elder Sign:** +1. You may play Sacred Bond.
- 37 total folders. 30 deck cards (007-036). Wendigo weakness (037).

### Key Cards
| # | Card | Rules |
|---|---|---|
| 002 | The Sacred Spear | +2 COM +2 dmg. Succeed by 2: +3 dmg instead. |
| 003 | The Tribal Oath | Weakness. Mythos: 1 horror. Spend 3r to discard. |
| 004 | Sacred Bond | Set aside (Elder Sign). +3 INT. 3/3 soak, fades. |
| 005 | Sacred Wind | Set aside (Auto-fail). +1 all stats. 3/3 soak, fades. |
| 006 | Sacred Strength | Set aside (Cultist). +2 COM. Heal 1 hor/dmg per kill. 3/3 soak, fades. |
| 007 | Teeth of the Deep Ones | Accessory, 1r. +1 WIL. Reduce incoming damage OR horror by 1. |
| 037 | Wendigo | Weakness/Enemy. Fight 2 / Health 2 / Evade 4 / Damage 2. Hunter. Spawns on lowest-COM investigator. Abel cannot act against it. |

---

## NORA WARWICK (RYP-NW) — COMPLETE ✅

- Rogue, WIL 3 / INT 5 / COM 3 / AGI 2, HP 7 / SAN 8
- Subtitle: Professor. Traits: Academic. Archaeologist. Blessed.
- **Ability:** Once per round: Spend 1r to add 1 bless token.
- **Elder Sign:** +1. Gain resources equal to shroud value.
- 39 total folders. 28 deck cards (007-036, excl. 019-020 replaced).
- Signature cards shuffled in: 002-006, 037-039.

---

## THE MAN IN BLACK (RYP-MB) — COMPLETE ✅

- Rogue, WIL 3 / INT 3 / COM 4 / AGI 4, HP 7 / SAN 7
- Subtitle: Arkham Underground. Traits: Criminal. Operative.
- Permanents: The Fixer (Body), Cash in the Bag (Accessory) — start in play.
- 34 total folders. 30 deck cards (005-034).

---

## AGNES CRANE (RYP-AC) — COMPLETE ✅

- Survivor, WIL 4 / INT 3 / COM 1 / AGI 4, HP 8 / SAN 8
- 35 folders. 30 deck cards (006-035).
- ⚠️ Card 020 (Drawn to the Flame) has wrong rules in EON — needs rebuild.

---

## BJORN BLACKCAST (RYP-BB) — COMPLETE ✅

- Mystic, WIL 5 / INT 3 / COM 2 / AGI 3, HP 6 / SAN 10
- 37 folders. All built and verified.

---

## EPHRAIM ARCHER (RYP-EA) — COMPLETE ✅

- Guardian, WIL 3 / INT 2 / COM 5 / AGI 3, HP 7 / SAN 8
- ⚠️ Folder 035 needs Strange Eons build.

---

## ELEANOR HEART (RYP-EH) — IN PROGRESS 🔧

- Mystic, WIL 4 / INT 4 / COM 1 / AGI 4, HP 10 / SAN 7
- Subtitle: The Undying. Traits: Medic. Scholar.
- Folders 001-034 created. Not yet built in Strange Eons.

---

## Pending Items

- [ ] Agnes 020 Drawn to the Flame — rebuild in Strange Eons (wrong rules in EON)
- [ ] Ephraim Archer 035 — needs Strange Eons build
- [ ] Build Eleanor Heart in Strange Eons (001-034)

---

## Simulation Results

### Greystoke + Abel vs Midnight Masks — 500 runs
- **Win rate: 47.8%** (239/500)
- Avg win round: 6.5 | Avg defeat round: 4.5
- Defeat causes: Greystoke HP 55%, Greystoke SAN 31%, Abel SAN 7%, Abel HP 7%
- Wendigo spawns Round 4 — fires in 67% of games
- Win rate with Wendigo: 64% | Without: 23%

### Ironhide + Greystoke (planned pairing)
- Not yet simulated with updated Ironhide cards.

---

## Key Design Decisions — DO NOT REVERSE

| Decision | Value |
|---|---|
| Greystoke ability | Draw 1 + gain 1r after successful investigate (once per round) |
| Greystoke Elder Sign | Search deck for Tome/Relic/Codex, play free, shuffle |
| Greystoke My Glass | Spend 3 clues to discard |
| Greystoke deck | 008-037 = 30 cards. 002-007 = 6 signatures shuffled in |
| Abel Spirit Coyote | Cost 2r, soak 3/1, +1 COM, retaliate 1 dmg |
| Abel Teeth | Accessory, 1r, +1 WIL, reduce damage OR horror by 1 |
| Abel Tribal Oath | Spend 3r to discard |
| Abel set-asides | Bond=Elder Sign, Wind=Auto-fail, Strength=Cultist |
| Abel Wendigo | Fight 2 / Health 2 / Evade 4 / Damage 2. Hunter. Abel cannot act against it. |
| Nora Warwick Collection | Free evade exhaust, no AoO, no economy, 0r |
| Nora Sekhem Sceptre | Arcane slot |
| Nora Horus Heresy | Cost 2r |
| Nora Power of Ancients | WIL/WIL skill, draw 1 on success |
| MiB The Fixer | Permanent Body, exhaust fight +2 COM 3 dmg, kill=2r |
| MiB Cash in the Bag | Permanent Accessory, gain 1r per turn |
| Agnes 020-021 | Draw top encounter card. Gain 2 clues. Take from any location. WIL/WIL. |
| Ironhide ability | [rea] Defeat enemy: Gain 1r + deal 1 dmg to each enemy at location (once per round) |
| Ironhide Elder Sign | +1. Draw 1 card and gain 1 resource |
| Ironhide Hollow Warden | Cost 0, Hand, 3 ammo, +2 COM +1 dmg, draw on kill, free +1 ammo on empty |
| Ironhide Hydra Hyde | Cost 2, Body, 3/3 soak, reduce dmg or hor by 1, shuffle back on discard |
| Ironhide Echoes of R'lyeh | Revelation 2 horror, after kill 1 horror, spend 4r to discard |
| Ironhide King's Talon | Cost 2, Hand, COM/COM, +2 COM +1 dmg, [cur]=+2, kill=heal 1 hor |
| Ironhide Luck of the Draw | Skill, INT/INT/INT, discover 2 clues instead of 1 |
