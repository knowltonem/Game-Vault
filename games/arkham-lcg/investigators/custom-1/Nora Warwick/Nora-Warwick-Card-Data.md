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
Nora Warwick deck only.

You get +1 <int> while The Warwick Collection
is in play.

<fre> At the start of your turn: Gain 1 resource.

<act> Spend 3 resources: Discover 1 clue at your
location and add 1 bless token to the chaos bag.

<fre> After you spend 5 or more resources in a
single round: Add 2 bless tokens to the chaos bag.
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

### Team Synergies

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

## 30-Card Deck (TBD)

*Deck design pending. Core cards to consider:*

**Economy:** Emergency Cache, Lucky Cigarette Case, Lone Wolf
**Investigation:** Pilfer, Pickpocketing, Shortcut
**Combat:** .41 Derringer, Butterfly Swords, Cheap Shot
**Support:** Teamwork, Calling in Favors, Liquid Courage
**Skills:** Manual Dexterity, Opportunist, Daring

*Full deck will be built after signature cards are confirmed.*
