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
Once per round: Spend 2 resources to add 2 bless
tokens to the chaos bag.
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
resource you cannot pay, take 1 horror and
1 damage.

<act> Spend 5 resources: Discard The Family Debt.
```

### Flavor
```
"The telegram arrived at the worst possible
moment. They always do."
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
| Ra-Night-Gaunt | 3 | 1 | +1 COM | Deal 1 dmg to all enemies on defeat | 2×`<com>` | Physical tank |
| Anubis-Touched | 1 | 4 | +1 WIL | Forced absorb 1 from 2+ hits | `<wil>`+`<com>` | Horror specialist |
| The Horus Heresy | 1 | 3 | +1 INT +1 AGI | Heal 1 horror per clue discovered | `<int>`+`<wil>` | Knowledge sustain |

### Soak Card Best Matches

| Ally | Best Card | Final Soak | Why |
|---|---|---|---|
| Ra | Canopic Wrappings (HP) | **5/1** | Maximise physical tank |
| Anubis | Scarab Amulet (SAN) | **1/6** | Maximise horror absorption |
| Horus | Eye Amulet (SAN) | **1/5** + prevent | Horror sponge + active prevention |

### Full Soak Picture — All Combinations With Best Cards

| Configuration | HP total | SAN total | Play style |
|---|---|---|---|
| Ra (5/1) + Anubis (1/6) | **13** | **15** | Balanced — safe pairing |
| Ra (5/1) + Horus (1/5) | **13** | **14** | Offensive — max stats |
| Anubis (1/6) + Horus (1/5) | **9** | **19** | Horror fortress — physically fragile |

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

### Servitor Allies

**Ra-Night-Gaunt** — Combat Servitor
- Base: 3 HP / 1 SAN
- **Cost: 3r**
- COM 3 fixed
- Icons: 2 × `<com>`
- Passive: You get +1 `<com>` while Ra-Night-Gaunt is in play
- **On defeat:** Deal 1 damage to each enemy at Nora Warwick's location
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
- Base: 1 HP / 3 SAN
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

## 30-Card Deck (TBD)

*Deck design pending. Core cards to consider:*

**Economy:** Emergency Cache, Lucky Cigarette Case, Lone Wolf
**Investigation:** Pilfer, Pickpocketing, Shortcut
**Combat:** .41 Derringer, Butterfly Swords, Cheap Shot
**Support:** Teamwork, Calling in Favors, Liquid Courage
**Skills:** Manual Dexterity, Opportunist, Daring

*Full deck will be built after signature cards are confirmed.*
