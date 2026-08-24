# Card-Data Edit Rules — Token Efficiency

## TOOL ROUTING — USE THE RIGHT TOOL
- **Filesystem tools**: Simple reads of small known text files. Use when file content is needed in context and no shell is required.
- **Desktop Commander**: All file operations on Windows (delete, rename, move), PowerShell commands, large files, binary files, multi-step shell operations. Default for anything touching the repo.
- **Claude bash_tool**: Linux container only — pip installs, Python scripts running in Claude's environment. Never for the user's Windows filesystem.
- **Never** use both Filesystem and DC for the same file operation in one turn — pick one.
- **Prefer DC over Filesystem** when both could work — DC is more powerful and avoids redundant tool calls.

## REPRINT AFTER CHANGES
- After any card change is saved to Card-Data, if the user has asked for a print/reprint of that card, reprint the full card block immediately after confirming the save.
- Format: Name, Type, Cost, Traits, Icons, Rules text — clean and readable.
- Do this automatically without being asked again.

## EDIT FIRST, READ ONLY ON FAILURE
1. Always attempt `edit_file` or `edit_block` blind.
2. Only read the file if the edit fails.
3. Never read a file "just to check" before editing.

## BATCH UPDATES
- Combine all changes to one file into a single `edit_file` call with multiple edits array entries.
- Never make two separate calls to the same file in one turn.

## AUDIT TABLE UPDATES
- Always update the audit totals in the same call as the card icon change.
- Never do audit update as a separate call.

## FILE SWAPS
- Always delete old RYP PNGs and rename new exports in one PowerShell block.
- Never split delete and rename into separate DC calls.

## CARD-DATA ICON FORMAT
- Single icon: `| **Icons** | \`<xxx>\` |`
- Double icon: `| **Icons** | \`<xxx><xxx>\` |`
- No icons: `| **Icons** | — (no icons) |`
- Audit table row: `| XXX (TYPE) | N |`

## FILE SWAP DETAIL
- Old PNGs to delete: `RYP-XX-NNN-Card-Name-Front.png` and `RYP-XX-NNN-Card-Name-Back.png`
- New exports to rename: `Card-Name-Front-Face.png` → `RYP-XX-NNN-Card-Name-Front.png` and `Card-Name-Back-Face.png` → `RYP-XX-NNN-Card-Name-Back.png`
- NEVER delete the `.eon` file. Ever.
- NEVER delete any file that is not a RYP-named PNG.

## NEVER
- Read a file to find a string that is predictable from context.
- Make more than one DC process call per file swap.
- Split a Card-Data update and its audit update across two turns.
- Delete a `.eon` file.
- Delete anything other than the old RYP-named Front and Back PNGs.
