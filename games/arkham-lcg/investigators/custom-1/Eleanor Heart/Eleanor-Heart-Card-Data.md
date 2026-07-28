# Eleanor Heart — Investigator Pack (RYP-EH)

← [[games/arkham-lcg/investigators/custom-1/index|Back to Custom Investigators]]

---

## Investigator Card

| Field | Value |
|---|---|
| **Name** | Eleanor Heart |
| **Subtitle** | The Undying |
| **Class** | Mystic |
| **Traits** | Medic. Scholar. |
| **Willpower** | 4 |
| **Intellect** | 4 |
| **Combat** | 1 |
| **Agility** | 4 |
| **Health** | 8 |
| **Sanity** | 9 |

### Ability
```
[rea] After Eleanor Heart takes damage or horror: Heal 1 damage or
horror from any investigator at your location. If Eleanor Heart has
3 or more damage on her, heal 2 instead. If she has 6 or more, heal 3.
If she has 7 or more, heal 4. (Limit once per round.)
```

### Elder Sign
```
+2. You may heal 2 damage or horror from Eleanor Heart.
All investigators at your location draw 1 card.
```

### Flavor (front)
```
"She's Still Standing"
```

### Story (back)
```
"She went to Innsmouth. She doesn't remember what happened.
Her unit of 12 didn't come back. She wanders Arkham now,
healing others while searching for answers about herself."
```

### Deckbuilding
```
Deck size: 30.
Mystic cards (0-3).
Neutral cards (0-5).
Cards that "heal damage or horror" (0-5).
Seeker and/or Guardian cards (0-1), up to 15 total.
No Weapon cards level 1-5.
Signature cards: Medical Bag ×1, The Innsmouth Codex ×1,
The Fog of Innsmouth ×1, 1 random basic weakness.
```

---

## Signature Cards

### 002 — Medical Bag

| Field | Value |
|---|---|
| **Subtitle** | Issued at Fort Warren |
| **Type** | Asset — Hand |
| **Cost** | 2r |
| **Traits** | Item. Medical. |
| **Slot** | Hand |
| **Unique** | Yes |
| **Icons** | 1 × `<int>` |

### Rules Text
```
Eleanor Heart deck only. Unique.

Medical Bag enters play with 4 charges.

<act> Spend 1 charge: Heal 1 damage or 1 horror
from an investigator at your location.
```

### Flavor
```
"Fort Warren issued it. Innsmouth changed it. Now it's different."
```

---

### 003 — The Innsmouth Codex

| Field | Value |
|---|---|
| **Subtitle** | Knowledge That Should Not Be |
| **Type** | Asset — Accessory |
| **Cost** | 1r |
| **Traits** | Item. Tome. Cursed. |
| **Slot** | Accessory |
| **Unique** | Yes |
| **Icons** | 1 × `<int>` + 1 × `<wil>` |

### Rules Text
```
Eleanor Heart deck only. Unique.

You get +1 <int> while The Innsmouth Codex is in play.

<act> Exhaust The Innsmouth Codex: Investigate. You
investigate using <int> instead of <int>. If you succeed,
discover 1 additional clue at your location. If you fail,
draw 1 card.
```

### Flavor
```
"She wasn't supposed to see it. Now she can't unsee it."
```

---

### 004 — The Fog of Innsmouth

| Field | Value |
|---|---|
| **Type** | Treachery — Weakness |
| **Traits** | Flaw. |
| **Unique** | Yes |

### Rules Text
```
Eleanor Heart deck only.

Revelation — Take 2 horror.

Forced — After each enemy attacks you: Take 1 damage.

<act> Spend 3 resources: Discard The Fog of Innsmouth.
```

### Flavor
```
"Twelve people went into Innsmouth. The fog claimed them."
```

---

## Healing Scale

| Damage on Eleanor | Total Heal | Status |
|---|---|---|
| 0-2 | 1 | Safe |
| 3-5 | 2 | Wounded |
| 6 | 3 | Hurt |
| 7 | 4 | Critical — next hit kills |

---

## Player Cards

### 005-006 — Take What You Need
- **Cost:** 1r
- **Type:** Event
- **Class:** Neutral
- **Traits:** Spirit.
- **Icons:** 1 × `<wld>`

```
Search the top 7 cards of your deck for any asset and
draw it. Shuffle your deck.
```
*Flavor: "She knows exactly what she needs."*

---

### 007-008 — Special Allowance
- **Cost:** 0r
- **Type:** Event
- **Class:** Neutral
- **Traits:** Fortune.
- **Icons:** 1 × `<wld>`

```
Fast. Gain 3 resources.
```
*Flavor: "The army pays for what it needs. No questions."*

---

### 009-010 — Clarity of Mind
- **Cost:** 1r
- **Type:** Event
- **Class:** Mystic
- **Traits:** Spell.
- **Icons:** 1 × `<wil>` + 1 × `<wld>`

```
Fast. Heal 2 horror from any investigator at your location.
```
*Flavor: "She holds the chaos at bay, just long enough."*

---

### 011-012 — Military Tactics
- **Cost:** 1r
- **Type:** Event
- **Class:** Neutral
- **Traits:** Tactic.
- **Icons:** 1 × `<wld>`

```
Fast. Draw 3 cards.
```
*Flavor: "Always have a plan."*

---

### 013-014 — Arcane Practice
- **Cost:** 2r
- **Type:** Event
- **Class:** Mystic
- **Traits:** Spell. Practiced.
- **Icons:** 2 × `<int>`

```
<act> Fight. You fight using <wil> instead of
<com>. You get +1 <wil> for this attack. If this
attack succeeds by 2 or more, deal +1 damage.
```
*Flavor: "Fort Warren trained her hands. Innsmouth trained the rest."*

---

### 015-016 — Triage
- **Cost:** 2r
- **Type:** Asset — Arcane
- **Class:** Mystic
- **Traits:** Spell. Medical.
- **Slot:** Arcane
- **Icons:** 1 × `<wil>` + 1 × `<int>`

```
Triage enters play with 5 charges.

<act> Spend 1 charge: Heal 1 damage or 1 horror
from an investigator at your location.
```
*Flavor: "Some wounds are not physical. She treats them the same."*

---

### 017-018 — Patch Up
- **Cost:** 1r
- **Type:** Event
- **Class:** Mystic
- **Traits:** Medical. Practiced.
- **Icons:** 1 × `<wil>` + 1 × `<wld>`

```
Fast. Heal 1 damage and 1 horror from an investigator
at your location.
```
*Flavor: "There's always time for this."*

---

### 019-020 — Fort Warren Chapel
- **Cost:** 1r
- **Type:** Asset — Arcane
- **Class:** Mystic
- **Traits:** Spell. Blessed.
- **Slot:** Arcane
- **SAN soak:** 1
- **Icons:** 1 × `<wil>`

```
<fre> After you heal damage or horror from any
investigator: You may add 1 bless token to the
chaos bag.
```
*Flavor: "She lights a candle every morning. She doesn't know why."*

---

### 021-022 — Army Resupply
- **Cost:** 0r
- **Type:** Event
- **Class:** Neutral
- **Traits:** Supply. Tactic.
- **Icons:** 1 × `<wld>`

```
Fast. Replenish up to 3 charges on any asset you
control.
```
*Flavor: "Always arrives when you need it most."*

---

### 023-024 — Do No Harm
- **Cost:** 0r
- **Type:** Event
- **Class:** Mystic
- **Traits:** Spell. Ward.
- **Icons:** 1 × `<wil>` + 1 × `<wld>`

```
Fast. Cancel a treachery card that is about to
affect any investigator at your location.
```
*Flavor: "The first oath. Still binding."*

---

### 025-026 — The Codex Revealed
- **Cost:** 1r
- **Type:** Event
- **Class:** Seeker
- **Traits:** Insight.
- **Icons:** 2 × `<int>`

```
Fast. Discover 1 clue at your location without
investigating.
```
*Flavor: "The book shows her what she needs to know."*

---

### 027 — Innsmouth Lessons
- **Cost:** 2r
- **Type:** Asset — Arcane
- **Class:** Seeker
- **Traits:** Tome. Cursed. Insight.
- **Slot:** Arcane
- **HP soak:** 1
- **Icons:** 1 × `<int>` + 1 × `<wld>`

```
<fre> After you successfully investigate: You may
discover 1 additional clue at your location and
gain 1 resource.
```
*Flavor: "It keeps teaching her."*

---

### 028 — Private Parker
- **Cost:** 3r
- **Type:** Asset — Ally
- **Class:** Neutral
- **Traits:** Ally. Military.
- **Slot:** Ally
- **HP soak:** 0
- **SAN soak:** 3
- **Icons:** 1 × `<agi>` + 1 × `<wld>`

```
You get +1 <agi> while Private Parker is in play.

<fre> After Eleanor Heart heals damage or horror
from any investigator: Draw 1 card.
```
*Flavor: "He was assigned to her. He doesn't know why. He shows up anyway."*

---

### 029 — Chaplain Adama
- **Cost:** 3r
- **Type:** Asset — Ally
- **Class:** Neutral
- **Traits:** Ally. Military. Blessed.
- **Slot:** Ally
- **HP soak:** 0
- **SAN soak:** 3
- **Icons:** 1 × `<wil>` + 1 × `<wld>`

```
You get +1 <wil> while Chaplain Adama is in play.

<fre> After you add a bless token to the chaos bag:
Gain 1 resource.
```
*Flavor: "He blesses her anyway. Regardless of what she's become."*

---

### 030-031 — Ward of Protection
- **Cost:** 1r
- **Type:** Event
- **Class:** Mystic
- **Traits:** Spell.
- **Icons:** 1 × `<wil>` + 1 × `<wld>`

```
Fast. Cancel the effects of a non-weakness treachery just
drawn by any investigator at your location. Take 1 horror.
```
*Flavor: "Not today."*

---

### 032-033 — Focused Mind
- **Cost:** —
- **Type:** Skill
- **Class:** Neutral
- **Icons:** 2 × `<int>`

```
If this test succeeds: Draw 1 card.
```
*Flavor: "She can focus through anything."*

---

### 034 — The Undying Will
- **Cost:** —
- **Type:** Skill
- **Class:** Neutral
- **Icons:** 1 × `<wil>` + 1 × `<int>` + 1 × `<wld>`

```
No additional rules text.
```
*Flavor: "She doesn't know if she can die anymore. She has decided that makes things easier."*

---

## Naming Convention

| File Type | Convention | Example |
|---|---|---|
| **Investigator .eon** | `Heart-Sig-Investigator.eon` | `Heart-Sig-Investigator.eon` |
| **Signature .eon** | `Heart-Sig-[Type]-[Name].eon` | `Heart-Sig-Asset-Medical-Bag.eon` |
| **Regular deck .eon** | `Heart-[Type]-[Name].eon` | `Heart-Event-Take-What-You-Need.eon` |
| **Exported PNGs** | `RYP-EH-###-[Name]-[Front/Back].png` | `RYP-EH-001-Eleanor-Heart-Front.png` |

---

## Pack Code
```
RYP-EH
```

---

## Folder Structure
```
Eleanor Heart/
├── art/
├── 001-Eleanor-Heart/
├── 002-Medical-Bag/
├── ...
└── Eleanor-Heart-Card-Data.md
```

---

## Design Notes

### Character Summary
Former Army nurse, Lieutenant, stationed at Fort Warren. Went to Innsmouth with her unit of 12. She's the only one who came back. She doesn't remember what happened, but something came back with her — something that heals more than it should, something that will not let her die. She wanders Arkham now, healing other investigators while searching for answers about herself. She put her weapons down after Innsmouth and will not pick them up again.

### Stat Analysis

| Stat | Value | Notes |
|---|---|---|
| WIL | 4 | Strong — drives her spells and healing |
| INT | 4 | Excellent — clue potential with Codex |
| COM | 1 | Dump stat — she will not fight physically |
| AGI | 4 | Fast — can evade when needed |
| Health | 10 | Massive — powers her healing scale |
| Sanity | 7 | Above average |

### Healing Scale Analysis
The core mechanic. At 0-2 damage: baseline heals. At 3-5: +1 bonus. At 6-8: +2 bonus. At 9: +3 bonus but one hit from defeat. The tension is deliberate — the player must choose between keeping Eleanor safe (weaker heals) or letting her take damage to amplify her healing (risking defeat).

### Slot Picture

| Slot | Card |
|---|---|
| Hand | Medical Bag + 1 open |
| Arcane | Triage + Fort Warren Chapel OR Innsmouth Lessons |
| Accessory | The Innsmouth Codex |
| Body | Open |
| Ally | Private Parker OR Chaplain Adama |

### Deck Summary

| Category | Cards | Slots |
|---|---|---|
| Search | Take What You Need | 2 |
| Economy | Special Allowance, Army Resupply | 4 |
| Combat | Last Resort, Arcane Practice | 4 |
| Healing | Triage, Patch Up | 4 |
| Cancel | Do No Harm | 2 |
| Utility | Fort Warren Chapel | 2 |
| Clue | The Codex Revealed, Innsmouth Lessons | 3 |
| Allies | Private Parker, Chaplain Adama | 2 |
| Draw | Military Tactics | 2 |
| Skills | Dead Calm, Focused Mind, The Undying Will | 5 |
| **Total** | | **30** |
