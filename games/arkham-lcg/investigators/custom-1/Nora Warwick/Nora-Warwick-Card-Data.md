# Professor Nora Warwick — Investigator Pack (RYP-NW)

← [[games/arkham-lcg/investigators/custom-1/index|Back to Custom Investigators]]

---

## Investigator Card

| Field | Value |
|---|---|
| **Name** | Professor Nora Warwick |
| **Subtitle** | The Warwick Endowment |
| **Class** | Rogue |
| **Traits** | Academic. Archaeologist. Blessed. |
| **Willpower** | 3 |
| **Intellect** | 5 |
| **Combat** | 3 |
| **Agility** | 2 |
| **Health** | 7 |
| **Sanity** | 8 |

### Ability
```
Once per round: Spend 1 resource to add 1 bless
token to the chaos bag.
```

### Elder Sign
```
+1. If you succeed, gain resources equal to the
shroud value of your location.
```

### Flavor
```
"The Warwick name has opened every tomb, every
archive, and every door that mattered. What I've
found has cosmic implications."
```

### Deckbuilding
```
Deck size: 30.
Rogue cards (0-5).
Seeker cards (0-2).
Guardian cards (0-2).
Mystic cards (0-1).
Neutral cards (0-5).
Signature cards: The Warwick Collection ×1,
The Book of the Dead ×1,
The Family Debt ×1, 1 random basic weakness.
```

---

## Signature Cards

---

### 002 — The Warwick Collection

| Field | Value |
|---|---|
| **Type** | Asset — Accessory |
| **Cost** | 0 |
| **Traits** | Item. Relic. Blessed. |
| **Slot** | Accessory |
| **SAN soak** | 2 |
| **Unique** | Yes |
| **Icons** | 1 × `<int>` + 1 × `<wil>` |

### Rules Text
```
Nora Warwick deck only. Unique.

You get +1 <int> while The Warwick Collection
is in play.

<fre> At the start of your turn: Gain 1 resource.

<act> Spend 4 resources: Discover 1 clue at
your location.

<fre> After you successfully investigate: You
may move 1 clue from your location to any
connecting location.
```

### Flavor
```
"The curator at the British Museum was quite
upset, until he saw the cheque."
```

---

### 003 — The Family Debt

| Field | Value |
|---|---|
| **Type** | Treachery |
| **Traits** | Flaw. Burden. |
| **Unique** | Yes |

### Rules Text
```
Nora Warwick deck only.

Revelation — The family calls in the debt.
Immediately spend resources equal to half the
current agenda's doom threshold (rounded up,
minimum 3).

If you cannot pay the full amount: For each
resource you cannot pay, take 1 horror or
1 damage (your choice).

<act> Spend 5 resources: Discard The Family Debt.
```

### Flavor
```
"The telegram arrived at the worst possible
moment. They always do."
```

---

### 004 — The Book of the Dead

| Field | Value |
|---|---|
| **Name** | The Book of the Dead |
| **Subtitle** | Arcane and Unnatural |
| **Type** | Asset — Arcane |
| **Cost** | 1r |
| **Traits** | Item. Tome. Relic. Blessed. |
| **Slot** | Arcane |
| **SAN soak** | 2 |
| **Unique** | Yes |
| **Icons** | 2 × `<int>` |

### Rules Text
```
Nora Warwick deck only. Unique.

You get +1 <int> while The Book of the Dead
is in play.

<fre> After you successfully investigate: You
may exhaust The Book of the Dead — investigate
again at your location without spending an action.

<fre> After The Book of the Dead enters play:
Search your deck for any Insight or Relic card
and draw it. Shuffle your deck.
```

### Flavor
```
"With this knowledge, I can see the unseen."
```

---

## Naming Convention

| File Type | Convention | Example |
|---|---|---|
| **Investigator .eon** | `Warwick-Sig-Investigator.eon` | `Warwick-Sig-Investigator.eon` |
| **Signature .eon** | `Warwick-Sig-[Type]-[Name].eon` | `Warwick-Sig-Asset-The-Warwick-Collection.eon` |
| **Regular deck .eon** | `Warwick-[Type]-[Name].eon` | `Warwick-Event-Lucky.eon` |
| **Exported PNGs** | `RYP-NW-###-[Name]-[Front/Back].png` | `RYP-NW-001-Nora-Warwick-Front.png` |

---

## Pack Code
```
RYP-NW
```

---

## Folder Structure

```
Nora Warwick/
├── art/
├── 001-Nora-Warwick/
│   └── Nora-mini/
├── 002-The-Warwick-Collection/
├── 003-The-Family-Debt/
└── Nora-Warwick-Card-Data.md
```

---

## Design Notes

### Character Summary
A 30-year-old British archaeologist bankrolled by the Warwick family fortune. Oxford educated, field hardened, and completely unafraid to throw money at problems that should be solved with caution. Looks like she belongs in a lecture hall. Turns out she's been doing this since her first dig in Egypt at age nineteen.

### Stat Analysis

| Stat | Value | Notes |
|---|---|---|
| WIL | 3 | Average — enough with skill commits |
| INT | 5 | Elite investigator — matches Greystoke |
| COM | 3 | Below average — compensated by expensive weapons |
| AGI | 2 | Genuinely low — she does not run from things |
| Health | 7 | Rogue-standard — fragile physically |
| Sanity | 8 | Strong — she's seen worse in private collections |

### Ability Analysis
**2r → 2 bless tokens** — the most aggressive bless generation in the set. At peak economy (4-6r per round) she can add 4 bless tokens per round. Faster than Abel's kill-trigger blesses, more consistent than Father Thomas's exhaust blesses.

### Elder Sign Analysis
**Gain resources equal to shroud value** — at INT 6 (with Collection) she frequently investigates high-shroud locations. Shroud 3 = +3r. Shroud 5 = +5r. The elder sign becomes a massive economy spike on exactly the locations she should be investigating anyway.

### The Warwick Collection Analysis
- **+1 INT** — pushes to INT 6, tied with Greystoke for highest investigate in the set
- **Free 1r per turn** — passive income funds the bless ability without touching hand
- **3r → clue + bless** — money buys clues directly, no test required
- **5r spent → 2 extra bless** — rewards big spending rounds automatically
- **2 SAN soak** — artifact insulates her mind

### The Family Debt Analysis
- **Scales with agenda doom threshold** — early scenarios: 3-4r. Late campaign: 6-7r
- **Minimum 3r** — never trivial even in scenario 1
- **Horror AND damage if unpaid** — 1 horror + 1 damage per resource short
- **Discard: 5r + action** — clean exit if prepared

### All Three Allies — Competing For Different Reasons

| Ally | HP | SAN | Passive | Special | Icons | Identity |
|---|---|---|---|---|---|---|
| Ra-Night-Gaunt | 3 | 1 | +1 COM | Deal 1 dmg to all enemies on defeat (if any) | 2×`<com>` | Physical tank |
| Anubis-Touched | 1 | 4 | +1 WIL | Forced absorb 1 from 2+ hits | `<wil>`+`<com>` | Horror specialist |
| The Horus Heresy | 2 | 3 | +1 INT +1 AGI | Heal 1 horror per clue discovered | `<int>`+`<wil>` | Knowledge sustain |

### Soak Card Best Matches

| Ally | Best Card | Final Soak | Why |
|---|---|---|---|
| Ra | Canopic Wrappings (HP) | **5/1** | Maximise physical tank |
| Anubis | Scarab Amulet (SAN) | **1/6** | Maximise horror absorption |
| Horus | Eye Amulet (SAN) | **2/5** + prevent | Horror sponge + survive physical hit |

### Full Soak Picture — All Combinations With Best Cards

| Configuration | HP total | SAN total | Play style |
|---|---|---|---|
| Ra (5/1) + Anubis (1/6) | **13** | **15** | Balanced — safe pairing |
| Ra (5/1) + Horus (2/5) | **14** | **14** | Offensive — max stats |
| Anubis (1/6) + Horus (2/5) | **10** | **19** | Horror fortress — less physically fragile now |

### The Hard Choices

| Pairing | Strengths | Weakness | When to pick |
|---|---|---|---|
| Ra + Anubis | Balanced HP and SAN | No INT/AGI boost | Standard scenarios |
| Ra + Horus | Max stats, self-sustaining horror soak | No big-hit absorb | Clue-heavy scenarios |
| Anubis + Horus | SAN 19, horror fortress | HP 9 — physically fragile | Horror-heavy encounter deck |


| Pairing | Dynamic |
|---|---|
| Nora + Ironhide | Funds his weapons, blesses his bag, he kills everything she uncovers |
| Nora + Greystoke | Two INT 5 investigators — extraordinarily fast clue clearing |
| Nora + Agnes | Nora's bless engine makes Agnes's chaos tokens dramatically better |
| Nora + Abel | Double bless engine — chaos bag almost entirely blessed within 3 rounds |

---

## Upgrade Path (Planned)

| Priority | Card | XP | Reason |
|---|---|---|---|
| 1 | The Warwick Collection (2) | 4 XP | Enhanced economy and bless generation |
| 2 | Lucky! (2) | 2 XP | Cancels revelations — protects the economy |
| 3 | Lola Santiago (3) | 6 XP | Elite Rogue ally — clues and resources |
| 4 | The Family Debt (2) | 4 XP | Reduced debt cost, faster discard |
| 5 | Chuck Fergus (5) | 10 XP | Ultimate Rogue support ally |

---

## Weapons — The Three Knives

All three weapons are Nora Warwick only. Same damage baseline, meaningfully different feel. Choose before each scenario based on what you need.

---

### The Kopis — The Efficient Blade
**Feel:** Economy swing | **Cost:** 2r | **Slot:** Hand

| Field | Value |
|---|---|
| Traits | Item. Weapon. Relic. |
| Icons | 1 × `<com>` + 1 × `<int>` |

```
<act> Fight. You get +1 <com> for this attack.
This attack deals +1 damage.
<fre> After you defeat an enemy with The Kopis:
Gain 2 resources.
```
*Flavor: "Every serious archaeologist carries one. Most don't use them like this."*

---

### The Khopesh — The Sacred Blade
**Feel:** Bless swing | **Cost:** 2r | **Slot:** Hand

| Field | Value |
|---|---|
| Traits | Item. Weapon. Relic. |
| Icons | 2 × `<com>` |

```
<act> Fight. You get +1 <com> for this attack.
This attack deals +1 damage.
<fre> After you defeat an enemy with The Khopesh:
Gain 1 resource and draw 1 card.
```
*Flavor: "Ra's warriors carried these into battles older than memory. The blade remembers them all."*

---

### The Sekhem Sceptre — The Mind Breaker
**Feel:** Defensive safety net | **Cost:** 2r | **Slot:** Hand

| Field | Value |
|---|---|
| Traits | Item. Weapon. Relic. |
| Icons | 1 × `<com>` + 1 × `<wil>` |

```
<act> Fight. You get +1 <com> for this attack.
This attack deals +1 damage.
After this attack resolves: Cancel the next horror
Nora Warwick would be dealt this round.
```
*Flavor: "Power is not always measured in wounds."*

---

## Weapon Summary

| Weapon | Cost | Damage | On Kill / Effect | Condition | Icons | Scenario Use |
|---|---|---|---|---|---|---|
| The Kopis | 2r | 1 | Gain 2r | On kill | `<com>` + `<int>` | Resource-starved |
| The Khopesh | 2r | 1 | Gain 1r + draw 1 card | On kill | 2 × `<com>` | Balanced refuel |
| The Sekhem Sceptre | 2r | 1 | Cancel next horror | Every attack | `<com>` + `<wil>` | Horror-heavy deck |

---

## Weapon Upgrade Paths

| Weapon | Lv 0 | Lv 2 | Lv 4 |
|---|---|---|---|
| The Kopis | 1 dmg, gain 2r | 2 dmg, gain 2r + draw 1 | 2 dmg, gain 3r + draw 1 + bless |
| The Khopesh | 1 dmg, 2 bless | 2 dmg, 2 bless + gain 1r | 2 dmg, 3 bless + gain 1r + splash |
| The Sekhem Sceptre | 1 dmg, cancel horror | 2 dmg, cancel + heal 1 | 2 dmg, cancel + heal 2 + cancel revelation |

---

### Soak Assets (×1 each)

**The Canopic Wrappings** — Cost 1r
```
Attach to an Ally asset you control.
When attached: Choose HP or SAN. That ally
gains +2 of the chosen type permanently.
<fre> At the end of the upkeep phase: Heal
1 damage from the attached ally.
```
*Flavor: "The jars remember their purpose. So do the wrappings."*

---

**The Scarab Amulet** — Cost 1r
```
Attach to an Ally asset you control.
When attached: Choose HP or SAN. That ally
gains +2 of the chosen type permanently.
<fre> At the end of the upkeep phase: Heal
1 horror from the attached ally.
```
*Flavor: "Khepri rolls the sun. The scarab rolls away what would destroy you."*

---

**The Eye Amulet** — Cost 2r
```
Attach to an Ally asset you control.
When attached: Choose HP or SAN. That ally
gains +2 of the chosen type permanently.
<rea> After the attached ally soaks damage
or horror: Exhaust The Eye Amulet — prevent
1 of that damage or horror.
```
*Flavor: "Horus lost his eye in battle and found it again. What it sees now is different."*

---

**The Collar of Sekhmet** — Cost 2r

| Field | Value |
|---|---|
| **Name** | The Collar of Sekhmet |
| **Subtitle** | Worn in Ten Thousand Battles |
| **Type** | Asset — Body |
| **Cost** | 2r |
| **Traits** | Item. Relic. Blessed. |
| **Slot** | Body |
| **HP soak** | 1 |
| **SAN soak** | 1 |
| **Unique** | Yes |
| **Icons** | 1 × `<com>` + 1 × `<wil>` |

```
You get +1 <com> while The Collar of Sekhmet
is in play.
```
*Flavor: "The curator said it was decorative. He had never worn it into the dark."*

---

---

**The Warwick Incendiary** — Cost 3r

| Field | Value |
|---|---|
| **Name** | The Warwick Incendiary |
| **Subtitle** | Do Not Shake |
| **Type** | Event |
| **Cost** | 3r |
| **Class** | Rogue |
| **Traits** | Improvised. Relic. Cursed. |
| **Icons** | 1 × `<wil>` + 1 × `<int>` |

```
Choose a location. Deal 2 damage to each enemy
at that location. Each investigator at that
location takes 1 damage.
Add 1 bless token to the chaos bag.
```
*Flavor: "The museum catalogue calls it a ceremonial vessel. It is not a ceremonial vessel."*

---

### Servitor Allies

**Ra-Night-Gaunt** — Combat Servitor
- Base: 3 HP / 1 SAN
- **Cost: 3r**
- COM 3 fixed
- Icons: 2 × `<com>`
- Passive: You get +1 `<com>` while Ra-Night-Gaunt is in play
- **On defeat:** Deal 1 damage to each enemy at Nora Warwick's location (if any)
- Soak slot: holds any soak asset
- Identity: Physical tank — goes out fighting
- No weapon slot — weapons are Nora only
- No secondary use — official ally design

**Anubis-Touched** — Defensive Servitor
- Base: 1 HP / 4 SAN
- **Cost: 3r**
- COM 3 fixed
- Icons: 1 × `<wil>` + 1 × `<com>`
- Passive: You get +1 `<wil>` while Anubis-Touched is in play
- **Forced:** When Nora Warwick would be dealt 2 or more damage or horror from a single source: Place 1 of that damage or horror on Anubis-Touched instead (your choice of type)
- Soak slot: holds any soak asset
- Identity: Horror specialist — silent guardian
- No weapon slot — weapons are Nora only
- No secondary use — official ally design

**The Horus Heresy** — Support Servitor
- Base: 2 HP / 3 SAN
- **Cost: 4r**
- COM 3 fixed
- Icons: 1 × `<int>` + 1 × `<wil>`
- Passive: You get +1 `<int>` and +1 `<agi>` while The Horus Heresy is in play
- **Free:** Once per round, after Nora Warwick discovers a clue: Heal 1 horror from The Horus Heresy
- Soak slot: holds any soak asset
- Identity: Knowledge sustains it — horror sponge
- No weapon slot — weapons are Nora only
- No secondary use — official ally design

### Weapon Icons

| Weapon | Icons |
|---|---|
| The Kopis | 1 × `<com>` + 1 × `<int>` |
| The Khopesh | 2 × `<com>` |
| The Sekhem Sceptre | 2 × `<wil>` |

### 2. Weapon Discard Options — RESOLVED
Removed. Icons are sufficient safety valve. Official weapon design standard maintained.

### Soak Asset Icons

| Soak Card | Icons | Secondary |
|---|---|---|
| Canopic Wrappings | 1 × `<wil>` + 1 × `<int>` | None — just icons |
| Scarab Amulet | 2 × `<wil>` | None — just icons |
| Eye Amulet | 1 × `<int>` + 1 × `<wil>` | None — just icons |

---

## Pending Design Decisions — Review Before Deck Build

### 1. Eye of Horus — Starting Deck or Upgrade Only?
RESOLVED: In starting deck at level 0. Name TBD (rename pending). Icons ensure it is never dead when third ally slot unavailable.

### 2. Weapon Discard Options — Keep or Remove?
Current: Each weapon has a fast discard effect when stranded.
Lean: Keep — Rogue flavor justifies it, stranded weapons are more punishing than stranded allies.

### 3. Ally Icons — RESOLVED
Confirmed as designed. Ra 2×COM, Anubis WIL+COM, Horus INT+WIL. No AGI icons intentional — Nora does not evade by design.

### 4. Soak Card Quantity — RESOLVED
×1 each. Perfect 3-to-3 parity with ally slots. Each soak card strategically distinct. No duplicates needed.

### 5. Ally Cost — RESOLVED
Ra-Night-Gaunt: 3r. Anubis-Touched: 3r. The Horus Heresy: 4r (extra stat boost justifies premium).

---

## 34-Card Deck

### Economy (5 cards)

| # | Card | Reskin Name | Type | Class | Qty |
|---|---|---|---|---|---|
| 004-005 | Ancient Cache | Tomb Cache | Event | Neutral | ×2 |
| 006-007 | Lone Wolf | The Warwick Clause | Asset | Rogue | ×2 |
| 008 | Faustian Bargain | The Pact of Kha | Event | Rogue | ×1 |

### Investigation (6 cards)

| # | Card | Reskin Name | Type | Class | Qty |
|---|---|---|---|---|---|
| 010-011 | Crack the Case | The Warwick Method | Event | Seeker | ×2 |
| 012-013 | Working a Hunch | Ancient Intuition | Event | Seeker | ×2 |
| 014-015 | Deduction | The Academic's Eye | Skill | Seeker | ×2 |

### Combat Support (3 cards)

| # | Card | Reskin Name | Type | Class | Qty |
|---|---|---|---|---|---|
| 016-017 | Cheap Shot | Desert Trick | Event | Rogue | ×2 |
| 018 | Dynamite Blast | The Warwick Incendiary | Event | Rogue | ×1 |

### Utility (2 cards)

| # | Card | Reskin Name | Type | Class | Qty |
|---|---|---|---|---|---|
| 019-020 | Calling in Favors | The Family Name | Event | Rogue | ×2 |

### Skills (7 cards)

| # | Card | Reskin Name | Type | Class | Qty |
|---|---|---|---|---|---|
| 021-022 | Opportunist | The Opportunist | Skill | Rogue | ×2 |
| 023-024 | Daring | The Warwick Gambit | Skill | Rogue | ×2 |
| 025-026 | Perception | The Scholar's Eye | Skill | Seeker | ×2 |
| 027 | Manual Dexterity | Desert Reflexes | Skill | Neutral | ×1 |

### Weapons (3 cards)

| # | Card | Reskin Name | Type | Class | Qty | Icons |
|---|---|---|---|---|---|---|
| 029 | The Kopis | The Kopis | Asset | Rogue | ×1 | `<com>` + `<int>` |
| 030 | The Khopesh | The Khopesh | Asset | Rogue | ×1 | 2 × `<com>` |
| 031 | The Sekhem Sceptre | The Sekhem Sceptre | Asset | Rogue | ×1 | `<com>` + `<wil>` |

### Allies (3 cards)

| # | Card | Type | Class | Qty | Icons | Secondary use |
|---|---|---|---|---|---|---|
| 032 | Ra-Night-Gaunt | Asset — Ally | Rogue | ×1 | 2 × `<com>` | Combat commits |
| 033 | Anubis-Touched | Asset — Ally | Rogue | ×1 | `<wil>` + `<com>` | Encounter + combat |
| 034 | The Horus Heresy | Asset — Ally | Rogue | ×1 | `<int>` + `<wil>` | Investigate + encounter |

### Equipment (1 card)

| # | Card | Reskin Name | Type | Class | Qty | Icons |
|---|---|---|---|---|---|---|
| 034 | The Collar of Sekhmet | The Collar of Sekhmet | Asset — Body | Rogue | ×1 | `<com>` + `<wil>` |

### Draw + Heal (4 cards)

| # | Card | Reskin Name | Type | Class | Qty | Role |
|---|---|---|---|---|---|---|
| 035-036 | Astounding Revelation | The Cairo Revelation | Event | Seeker | ×2 | Unconditional draw + 2r |
| 037-038 | Logical Reasoning | The Warwick Reasoning | Event | Seeker | ×2 | Unconditional 2 horror heal |

---

## Deck Summary

| Category | Cards | Slots |
|---|---|---|
| Economy | Tomb Cache, Warwick Clause, Pact of Kha | 5 |
| Investigation | Warwick Method, Ancient Intuition, Academic's Eye | 6 |
| Combat | Desert Trick, Warwick Incendiary | 3 |
| Utility | The Family Name | 2 |
| Skills | Opportunist, Gambit, Scholar's Eye, Desert Reflexes | 7 |
| Weapons | Kopis, Khopesh, Sekhem Sceptre | 3 |
| Allies | Ra-Night-Gaunt, Anubis-Touched, Horus Heresy | 3 |
| Equipment | Collar of Sekhmet | 1 |
| Draw + Healing | Cairo Revelation, Warwick Reasoning | 4 |
| **Total** | | **34** |

---

## Icon Coverage

| Test type | Icons | Sources |
|---|---|---|---|
| `<com>` | 10 | Ra ×2, Khopesh ×2, Desert Trick ×2, Kopis ×1, Anubis ×1, Sekhem ×1, Collar ×1 |
| `<int>` | 8 | Scholar's Eye ×4, Ancient Intuition ×4, Horus ×1, Kopis ×1, Academic's Eye ×2, Warwick Method ×2, Family Name ×2, Cairo Revelation ×2, Pact of Kha ×1 |
| `<wil>` | 7 | Warwick Reasoning ×4, Anubis ×1, Horus ×1, Sekhem ×1, Collar ×1, Warwick Incendiary ×1, Pact of Kha ×1 |
| `<wld>` | 10 | Warwick Gambit ×6, Opportunist ×2, Cairo Revelation ×2, Tomb Cache ×2 |
| `<agi>` | 4 | Desert Reflexes ×2, Desert Trick ×2, Family Name ×2, Warwick Clause ×2 |

---

## Ally As Skill Commit — Icon Replacements

| Ally | Replaces | Reasoning |
|---|---|---|
| Ra-Night-Gaunt 2×`<com>` | 1 copy of Desert Trick | Same combat icon coverage |
| The Horus Heresy `<int>`+`<wil>` | 1 copy of Academic's Eye | Same INT coverage |
| Anubis-Touched `<wil>`+`<com>` | 1 copy of Warwick Resolve | Adds WIL coverage previously absent |

---

## Reskin Flavor Lines

| Card | Reskin | Flavor |
|---|---|---|
| Ancient Cache | Tomb Cache | *"Every expedition leaves something behind. She knows where to look."* |
| Lone Wolf | The Warwick Clause | *"The Warwick endowment has a clause. She's the only one who reads it."* |
| Faustian Bargain | The Pact of Kha | *"Kha's price is always paid in darkness. She pays it anyway."* |
| Crack the Case | The Warwick Method | *"Find everything. Document nothing. Profit immediately."* |
| Working a Hunch | Ancient Intuition | *"Two hundred years of digs, catalogued and cross-referenced. She already knows what's here."* |
| Deduction | The Academic's Eye | *"She sees what others miss. Professionally."* |
| Cheap Shot | Desert Trick | *"Oxford never taught her this. Egypt did."* |
| Calling in Favors | The Family Name | *"The Warwick name opens doors. She uses it sparingly. Mostly."* |
| Perception | The Scholar's Eye | *"She has read everything ever written about what lies beneath the sand."* |
| Manual Dexterity | Desert Reflexes | *"When the tomb traps activate, you learn to move."* |
| Opportunist | The Opportunist | *"She works alone when it matters. By design."* |
| Daring | The Warwick Gambit | *"The family motto is not 'be careful'."* |
| Dynamite Blast | The Warwick Incendiary | *"The museum catalogue calls it a ceremonial vessel. It is not a ceremonial vessel."* |
| The Collar of Sekhmet | The Collar of Sekhmet | *"The curator said it was decorative. He had never worn it into the dark."* |

---

## Deckbuilding Check

| Rule | Cards | Count | Limit | Status |
|---|---|---|---|---|---|
| Rogue 0-5 | Warwick Clause, Pact of Kha, Desert Trick, Family Name, Opportunist, Daring, Kopis, Khopesh, Sekhem, Ra, Anubis, Horus, Desert Reflexes | 14 | No limit | ✅ |
| Seeker 0-2 | Warwick Method, Ancient Intuition, Academic's Eye, Scholar's Eye, Cairo Revelation, Warwick Reasoning | 12 | No limit | ✅ |
| Guardian 0-2 | (none in deck) | 0 | 4 max | ✅ |
| Neutral | Tomb Cache | 2 | No limit | ✅ |

