---
tags: [index, arkham-lcg]
---

# Arkham LCG — Project Index

## Project Overview

Custom expansion for Arkham Horror LCG called **The R'lyeh Expansion**.
Five custom investigator packs plus one shared upgrade pack.
Physical cards printed via Strange Eons software.

---

## Investigator Packs

```dataview
TABLE class AS "Class", status AS "Status", cards AS "Cards"
FROM "games/arkham-lcg/investigators/custom-1"
WHERE type = "investigator-index"
SORT file.name ASC
```

### Manual List
| Pack Code | Investigator | Class | Cards | Status | Catalogue |
|---|---|---|---|---|---|
| RYP-JI | [[Jonathan Ironhide\|Jonathan Ironhide]] | Guardian | 34 | ✅ Printed | [[Jonathan Ironhide/RYP-JI-Master-Catalogue\|Catalogue]] |
| RYP-AG | [[Alistair Greystoke\|Alistair Greystoke]] | Seeker | 39 | ✅ Printed | [[Alistair Greystoke/RYP-AG-Master-Catalogue\|Catalogue]] |
| RYP-AC | [[Agnes Crane\|Agnes Crane]] | Survivor | 33 | ✅ Printed | [[Agnes Crane/RYP-AC-Master-Catalogue\|Catalogue]] |
| RYP-AR | [[Abel Redcloud\|Abel Redcloud]] | Guardian | 31 | ✅ Printed | [[Abel Redcloud/RYP-AR-Master-Catalogue\|Catalogue]] |
| RYP-NW | [[Nora Warwick\|Nora Warwick]] | Rogue | 36 | 🔧 In Progress | [[Nora Warwick/RYP-NW-Master-Catalogue\|Catalogue]] |

---

## Shared Packs

| Pack Code | Name | Cards | Status | Catalogue |
|---|---|---|---|---|
| RYP-UP | [[Upgrade Pack\|Upgrade Pack]] | 54 | ⬜ Not Started | [[Upgrade Pack/RYP-UP-Master-Catalogue\|Catalogue]] |

---

## Future Packs

| Pack Code | Name | Type | Status |
|---|---|---|---|
| RYP-06 | Investigator 6 (TBD) | Investigator | ⬜ Not Designed |
| RYP-07 | Investigator 7 (TBD) | Investigator | ⬜ Not Designed |
| RYP-SD1 | Standalone Deck 1 (TBD) | Standalone | ⬜ Not Designed |
| RYP-CE1 | Campaign Encounter Pack 1 (TBD) | Encounter | ⬜ Not Designed |
| RYP-EX1 | Expansion Pack 1 (TBD) | Expansion | ⬜ Not Designed |

---

## Key Documents

| Document | Purpose |
|---|---|
| [[MASTER-CATALOGUE\|MASTER-CATALOGUE]] | Top-level card catalogue index |
| [[HANDOFF\|HANDOFF]] | AI continuity document |
| [[Nora Warwick/RYP-NW-Master-Catalogue\|RYP-NW Master Catalogue]] | Nora's full card print blocks |

---

## Build Status Key

| Symbol | Meaning |
|---|---|
| ✅ | Fully built, exported, printed |
| 🔧 | In progress |
| ⬜ | Not yet started |
| ❓ | Designed but not reviewed |

---

*[[Home]] | Repository: [knowltonem/Game-Vault](https://github.com/knowltonem/Game-Vault)*
