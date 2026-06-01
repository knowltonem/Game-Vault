# 🎲 Board Game Vault

A personal board game wiki built in [Obsidian](https://obsidian.md), synced to GitHub via the [Obsidian Git](https://github.com/denolehov/obsidian-git) plugin.

## What's in here

- Detailed notes, rules references, and buying guides for board games
- Organized as an Obsidian vault — open the folder directly in Obsidian
- Dataview plugin powers cross-note queries and the home dashboard

## Current games

| Game | Type | Status |
|---|---|---|
| Lord of the Rings: The Card Game (LCG) | Cooperative LCG | Active |

## Setup

1. Clone this repo
2. Open the folder as a vault in Obsidian
3. Install community plugins: **Obsidian Git** and **Dataview**
4. See [`_assets/plugin-setup.md`](_assets/plugin-setup.md) for full configuration steps

## Structure

```
/
├── Home.md                  # Dashboard
├── templates/               # Note templates
│   └── game-template.md
├── games/
│   └── lotr-lcg/
│       ├── index.md         # Game hub
│       ├── notes/           # Rules, tips, concepts
│       └── buying/          # Buying guides & product lists
└── _assets/                 # Meta notes (setup guides, etc.)
```
