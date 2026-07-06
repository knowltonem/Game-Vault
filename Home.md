# 🏛️ R'lyeh Expansion — Home

> Custom Arkham Horror LCG expansion. Five investigators, one upgrade pack, more to come.

---

## Quick Navigation

- [[Arkham LCG Index]] — Full project index
- [[MASTER-CATALOGUE]] — Card catalogue master index
- [[HANDOFF]] — AI handoff document

---

## Investigators

| Investigator | Class | Status | Cards |
|---|---|---|---|
| [[Jonathan Ironhide]] | Guardian | ✅ Printed | 34 |
| [[Alistair Greystoke]] | Seeker | ✅ Printed | 39 |
| [[Agnes Crane]] | Survivor | ✅ Printed | 33 |
| [[Abel Redcloud]] | Guardian | ✅ Printed | 31 |
| [[Nora Warwick]] | Rogue | 🔧 In Progress | 36 |

---

## Packs

| Pack | Status |
|---|---|
| [[Upgrade Pack]] | ⬜ Not Started |
| Investigator 6 | ⬜ Not Designed |

---

## Recent Activity

```dataview
TABLE file.mtime AS "Last Modified"
FROM "games/arkham-lcg/investigators/custom-1"
WHERE file.mtime >= date(today) - dur(7 days)
SORT file.mtime DESC
LIMIT 10
```

---

*Repository: [knowltonem/Game-Vault](https://github.com/knowltonem/Game-Vault)*
