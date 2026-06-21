# 🎲 Board Game Vault

A personal wiki for board game notes, rules references, buying guides, and how-to resources.

---

## Games

```dataview
TABLE game-type AS "Type", players AS "Players", play-time AS "Time", complexity AS "Complexity", status AS "Status"
FROM "games"
WHERE file.name = "index"
SORT file.name ASC
```

### Browse manually
- [[games/lotr-lcg/index|Lord of the Rings: The Card Game (LCG)]]
- [[games/arkham-lcg/index|Arkham Horror: The Card Game (LCG)]]

---

## Quick links

- [[templates/game-template|➕ Add a new game (template)]]
- [[_assets/plugin-setup|⚙️ Plugin setup guide]]

---

> [!tip] Vault syncs automatically via the Obsidian Git plugin.
> Commit/push runs on a schedule. You can also trigger it manually with `Ctrl+P → Obsidian Git: Commit and push`.
