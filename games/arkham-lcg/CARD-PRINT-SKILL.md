---
name: arkham-strange-eons-card-print
description: Read Strange Eons .eon card files (used for Abraham Setrakian and other custom Arkham Horror LCG investigator packs in the board-game-vault Obsidian vault) and print card fields in a copy-paste-ready format for pasting into Strange Eons. Use when asked to "print card", "reprint", "print [card name]", when building/reviewing custom Arkham Horror LCG cards in games/arkham-lcg, or when needing to inspect a built .eon file's actual field names/values instead of guessing them.
---

# Arkham Horror LCG — Strange Eons Card Printing

This skill covers two things: how to read the real field names/values out of a built
Strange Eons `.eon` file, and the exact output format the user wants when they ask to
"print card" / "reprint [card]".

Use alongside `games/arkham-lcg/EDIT-RULES.md` (tool routing, batching, file-swap rules) —
this skill does not replace that file, it covers card printing specifically.

## Reading a `.eon` file

`.eon` files are Java-serialized object streams (magic bytes `AC ED 00 05`), not plain
text or XML. Do NOT try to read them with the Filesystem/DC `read_file` tool directly —
they'll come back as binary garbage. Do NOT loop byte-by-byte in PowerShell either
(`$bytes | ForEach-Object {...}` over a multi-MB file is extremely slow, effectively
hangs). Instead extract printable strings in one fast pass:

```powershell
$f = 'C:\path\to\RYP-AS-0NN-Card-Name.eon'
$bytes = [System.IO.File]::ReadAllBytes($f)
$s = [System.Text.Encoding]::GetEncoding('ISO-8859-1').GetString($bytes)
$matches = [regex]::Matches($s, '[\x20-\x7E]{4,}')
($matches | ForEach-Object { $_.Value }) | Select-Object -First 300 | Out-String -Width 200
```

Run this via Desktop Commander `start_process` (default shell is already powershell.exe —
don't wrap the command in an extra `powershell -Command "..."`, that breaks `$variable`
interpolation). Increase `Select-Object -First N` if the field you need isn't in the
first 300 matches; the embedded card art PNG's binary data starts appearing as noise
after the metadata block, so once you see PNG chunk markers (`IHDR`, `IDATx`, etc.) you've
passed the useful part.

### Caveats on what you can trust from the raw dump

- Field **names** (the actual Java HashMap keys used by the Strange Eons AHLCG plugin)
  are reliable — they're fixed string constants and show up cleanly.
- Field **values** that are unique/fresh strings are usually reliable and appear right
  after their key.
- Values that repeat a string already seen earlier in the file (e.g. multiple `Skill3`–
  `Skill6` all set to "None") get serialized as a back-reference (`q` marker) instead of
  the literal text, so they won't show up again in the dump. Don't assume a missing value
  means the field is unset — it likely just reused an earlier string.
- For the Investigator template's generic back-of-card boxes (`Text1NameBack`/`Text1Back`
  through `Text8NameBack`/`Text8Back`), do NOT assume dump-adjacency means the label and
  its value are paired — Java HashMap serialization order isn't guaranteed to interleave
  key/value cleanly, especially across back-references. Match content to its label by
  *meaning* (e.g. "Deck Size", "Deckbuilding Restrictions") rather than by TextN number.
  When genuinely ambiguous, say so rather than guessing — a wrong guess here means the
  user pastes text into the wrong box in Strange Eons.

### Known field names (Asset-type cards, `ArkhamHorrorLCG/diy/Asset.js`)

Artist, ResourceCost, CardClass, CardClass2, CardClass3, Traits, Slot, Slot2, Rules,
Flavor, Keywords (this is where "Uses (N supplies/ammo/etc.)" text lives),
KeywordsSpacing, Skill1–Skill6 (only as many appear as were actually touched — untouched
slots just don't show up, they default to None), Unique, Level, Stamina, Sanity,
PerInvestigatorStamina, PerInvestigatorSanity, Subtitle, Victory, CollectionNumber,
Collection, CollectionType, BackType.

### Known field names (Investigator-type cards, `ArkhamHorrorLCG/diy/Investigator.js`)

Traits, Rules (front ability text AND Elder Sign text combined in one field, separated by
a line break), Flavor, Subtitle, Willpower, Intellect, Combat, Agility, Stamina, Sanity,
CardClass, CollectionNumber, Collection, Unique, InvStoryBack (the back-of-card story
text), plus the generic Text1NameBack/Text1Back … Text8NameBack/Text8Back pairs — on
Abraham Setrakian's card these carry: Deck Size, Secondary Class Choice, Deckbuilding
Options, Deckbuilding Restrictions, Deckbuilding Requirements, Additional Restrictions
(exact box-number-to-label mapping may differ per investigator; read the labels, don't
assume the numbering is consistent across cards).

## The "print card" output format

When the user says "print card", "print [card name]", or "reprint [card]", they want to
copy-paste each field's value straight into Strange Eons without retyping. Output format:

- One field per block.
- The field's real Strange Eons name as a plain-text label line (use the actual field
  name from the lists above — `CardClass` not `Class`, `ResourceCost` not `Cost`,
  `Skill1`/`Skill2` not a combined `Icons` line, `Rules` not `Text`).
- Immediately below, the raw value alone inside a fenced code block (triple backtick),
  nothing else in the block — this is what makes the chat client render a copy button
  for just that value.
- If a field is legitimately blank/unset, still print the label with an empty block and
  a short note like `(none recorded)`.
- Source the values from the investigator's `Card-Data.md` (the documented/intended
  version), not from re-reading the `.eon` file each time — Card-Data.md is the source of
  truth the user edits going forward. Only read the `.eon` when specifically asked to
  compare/verify against what's actually built.
- If Card-Data.md's current text disagrees with what's already built in the `.eon` (i.e.
  the card was built before a later edit to Card-Data.md), flag the specific field and
  both versions, and ask which one is correct — don't silently pick one.

### Example (partial, for a Skill-icon field on an Asset card)

Skill1:
```
Combat
```

Skill2:
```
Combat
```

Skill3–Skill6:
```
None
```

## Confirming changes

Per earlier correction in this project: only edit Card-Data.md / SESSION-HANDOFF.md /
folders when the user gives a clear instruction to change something. An observation or
statement from the user (e.g. "X is basically Y reskinned") is not by itself a request to
change the file — ask or wait for an explicit instruction first.
