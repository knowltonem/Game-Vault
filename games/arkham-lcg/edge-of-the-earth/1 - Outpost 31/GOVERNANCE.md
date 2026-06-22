# Outpost 31 — Repository Governance

Read this before touching anything in this folder.

## Two Tracks
| Track | Folder | Rule |
|---|---|---|
| Original | `Outpost 31 - Original/` | Read-only source of truth. Delivered art (PNG), PDF, .doc, .zip are NEVER edited, renamed, or deleted. |
| Modified | `outpost31-mod/` | All new/changed material: extracted card data, corrected text, art redirects, logs. |

## Golden Rule
Only ever READ from the original. WRITE only to the mod.

## The One Exception
`Outpost 31 - Original/_card-data-original/` holds verbatim transcriptions of the original
card text (typos preserved). It is a reconstruction, not a delivered artifact, and does NOT
count toward the integrity manifest. Never fix it.

## Mod-only renames (apply during the art render pass, NOT to originals)
- Helicopter Pad -> Ice Runway (#9)
- Vehicle Storage / Storage Hanger -> Storage Hangar (#16)
- MaCready -> MacReady (matches 1982 film + designer scenario guide)

## Integrity
- `.original-checksums.sha256` = manifest of delivered files only (excludes _card-data-original).
- Verify: `./protect-original.sh verify` (run after big sessions).
- If the original folder is renamed/moved, REGENERATE the manifest.

## Naming
- Scenario subfolders: `<Name> - Original/` (spaces) and `<name>-mod/` (kebab).
- Mod data files: clean names (e.g. Radio-Room.md).
- Original transcriptions mirror original titles, typos included (e.g. Losing-Humnanity.md).
