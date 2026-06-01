# Plugin Setup Guide

← [[Home|Back to Home]]

Two community plugins power this vault. Install them via **Settings → Community plugins → Browse**.

---

## 1. Obsidian Git

Syncs the vault to your GitHub repo automatically.

### Install & connect

1. Open **Settings → Community plugins → Browse**
2. Search "Obsidian Git" → Install → Enable
3. Go to **Settings → Obsidian Git**
4. Set your GitHub credentials (personal access token recommended):
   - [Create a token](https://github.com/settings/tokens) with `repo` scope
   - Enter it in the plugin's "Authentication/Password" field
5. Set your **Author name** and **Author email** (used for git commits)

### Recommended settings

| Setting | Value |
|---|---|
| Auto pull interval | 10 minutes |
| Auto commit and sync interval | 20 minutes |
| Commit message | `vault: auto-sync {{date}}` |
| Pull on startup | ✅ Enabled |

### Manual sync

Open the command palette (`Ctrl+P` / `Cmd+P`) and search:
- `Obsidian Git: Commit all changes` — commit everything
- `Obsidian Git: Push` — push to GitHub
- `Obsidian Git: Pull` — pull latest from GitHub
- `Obsidian Git: Commit and sync` — does all three in one step

---

## 2. Dataview

Lets notes query each other like a database. Powers the game index table on [[Home]].

### Install

1. **Settings → Community plugins → Browse**
2. Search "Dataview" → Install → Enable
3. Enable **"Enable JavaScript Queries"** in Dataview settings (optional but useful later)

### How it's used here

The Home dashboard uses a Dataview query to list all games automatically. Any note with `game-type`, `players`, and `status` in its frontmatter will appear in the table. When you add a new game, copy the [[templates/game-template|game template]] — the frontmatter is already set up.

---

## Initial repo setup

If you're setting this up for the first time:

```bash
# In your terminal, inside the vault folder:
git init
git add .
git commit -m "initial vault setup"
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
git push -u origin main
```

Then open the vault in Obsidian and the Git plugin will take over from there.

---

## .gitignore

The repo includes a `.gitignore` that excludes plugin binaries (which are large and user-specific) while keeping your config files. You'll need to install community plugins on each device, but your **settings and note content** will sync automatically.
