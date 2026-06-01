# 🎲 Board Game Vault

> Your personal command center for board game research, collection tracking, and buying intel.

---

## 🕹️ My Games

```dataview
TABLE game-type AS "Type", players AS "Players", status AS "Status"
FROM "games"
WHERE file.name = "index"
SORT file.name ASC
```

---

## 📦 Collection at a Glance

```dataview
TABLE product AS "Product", type AS "Type", owned AS "Owned?"
FROM "games/lotr-lcg/collection"
WHERE file.name != "my-collection"
SORT file.name ASC
```

---

## 🛒 Wishlist — Next Purchases

```dataview
TABLE notes AS "Notes"
FROM "games/lotr-lcg/collection"
WHERE file.name = "my-collection"
```

> [!tip] Top picks right now
> - **Heirs of Númenor** — Noble Knight NM $55 — recent arrival, won't last
> - **The Dark of Mirkwood** — ~$20, continues the core campaign
> - **The Black Riders Saga** — Noble Knight Mint $34.95, hard to find anywhere else
> - 🔗 [Browse Noble Knight LOTR LCG](https://www.nobleknight.com/Products/Lord-of-the-Rings-LCG-The---Core-Starters-and-Assorted)

---

## ⚡ Quick Actions

> [!example] Jump in
> - 📖 [[games/lotr-lcg/notes/rules|Rules & turn phases]]
> - 🧠 [[games/lotr-lcg/notes/tips|Tips & strategy]]
> - 🃏 [[games/lotr-lcg/collection/my-collection|My full collection + wishlist]]
> - 🛒 [[games/lotr-lcg/buying/guide|Buying guide]]

> [!example] Add content
> - ➕ [[templates/game-template|Add a new game]]
> - ⚙️ [[_assets/plugin-setup|Plugin setup guide]]

---

## 🎯 What to Play Next

> [!note] Scenarios ranked by where you are
> 1. **Passage Through Mirkwood** — start here, easiest intro ✅ *in Revised Core Set*
> 2. **Journey Along the Anduin** — next step up, watch for the Hill Troll ✅ *in Revised Core Set*
> 3. **Escape from Dol Guldur** — hard mode, hero gets captured at start ✅ *in Revised Core Set*
> 4. **Dark of Mirkwood scenarios** — continues campaign 🛒 *need to buy*

---

## 📰 Resources

| Site | What it's for |
|---|---|
| [RingsDB](https://ringsdb.com) | Card database + deck builder |
| [Hall of Beorn](https://hallofbeorn.com/LotR) | Card search + scenario explorer |
| [Hall of Gondor](https://hallofgondor.com) | Campaign cards reference |
| [Vision of the Palantir](https://visionofthepalantir.com) | New player guides |
| [Noble Knight](https://www.nobleknight.com/Products/Lord-of-the-Rings-LCG-The---Core-Starters-and-Assorted) | Best source for used/hard-to-find products |
| [BGG Marketplace](https://boardgamegeek.com/boardgame/349067/marketplace) | Secondary market |
