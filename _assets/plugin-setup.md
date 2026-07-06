# Obsidian Plugin Setup

## Currently Installed

| Plugin | Purpose | Status |
|---|---|---|
| obsidian-git | Auto-commit and sync to GitHub | ✅ Installed |
| dataview | Auto-generated tables from frontmatter | ✅ Installed |

## Recommended Additional Plugins

Install these from Obsidian Settings → Community Plugins → Browse:

| Plugin | ID | Purpose | Priority |
|---|---|---|---|
| Templater | templater-obsidian | Smart templates with variables | 🔥 High |
| Kanban | obsidian-kanban | Card build tracking board | 🔥 High |
| Iconize | obsidian-icon-folder | Icons on folders and files | 🟡 Medium |
| Better Word Count | better-word-count | Accurate word/char counts | 🟡 Medium |
| Dataview | dataview | Already installed | ✅ Done |
| Tag Wrangler | tag-wrangler | Manage tags across vault | 🟡 Medium |
| Folder Notes | folder-notes | Click folder to open index note | 🔥 High |

## Dataview Setup

Dataview is installed. To use it, add frontmatter to notes:

```yaml
---
tags: [investigator, rogue]
type: investigator-index
class: Rogue
status: In Progress
cards: 36
pack_code: RYP-NW
---
```

Then query with:
```dataview
TABLE class, status, cards
FROM #investigator
SORT class ASC
```

## Obsidian Git Setup

obsidian-git is installed. Recommended settings:
- Auto pull interval: 10 minutes
- Auto push interval: 10 minutes  
- Commit message: `vault: auto-commit {{date}}`
- Pull on startup: enabled

## Folder Notes Setup

After installing Folder Notes plugin:
- Each investigator folder will open its index note when clicked
- e.g. clicking "Nora Warwick" folder opens Nora-Warwick.md automatically

## Graph View Tips

Open Graph View (Ctrl+G) to see connections between:
- All investigator index notes
- Catalogue files
- Card data files
- HANDOFF and MASTER-CATALOGUE

For best results, filter by tag in Graph View:
- `tag:#investigator` — show only investigator notes
- `tag:#ryp-nw` — show only Nora Warwick notes
