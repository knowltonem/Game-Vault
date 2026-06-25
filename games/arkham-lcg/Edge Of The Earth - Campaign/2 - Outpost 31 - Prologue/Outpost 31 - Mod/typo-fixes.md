# Typo & Style Punch List — Strange Eons Render Pass

> Consolidated list of every text fix flagged during card-data extraction.
> These are corrections to apply when re-rendering card art in Strange Eons.
> **None are period/anachronism issues** — those are tracked separately in the art-direction note.

Legend:
`📄` = Card data .md file — Mod Changes section updated (source of truth for corrected text)
`🎨` = Strange Eons .eon project — not yet created (needs card creation + render pass)
`☐` = to do · `✏️` = grammar/spelling · `🔠` = capitalization · `❓` = decision needed

---

## Locations

### Supply Room (#17)
- 📄 ☐ ✏️ Reaction ability prints **"If you evade *and* enemy"** → correct to **"evade *an* enemy"**.

---

## Story Assets (Crew)

### Ellie Rowe (#21a)
- 📄 ☐ ✏️ Ability 2 prints **"Parley. Parley."** (doubled word) → drop one, leave single **"Parley."**

### Elliot Childs (#22a)
- 📄 ☐ 🔠 **"Spend 2 Resources"** → lowercase **"resources"**.

### Wilford Brimley (#25a) — *three on one card*
- 📄 ☐ ✏️ Ability 1 prints the name as **"Wilfird Brimley"** → **"Wilford Brimley"**.
- 📄 ☐ ✏️ **"succceed"** (triple c) → **"succeed"**.
- 📄 ☐ 🔠 Subtitle **"Doesn't trust Anyone"** → lowercase **"anyone"**.

### R.J. MacReady (#24a)
- 📄 ☐ ❓ **Spelling decision:** card/file use **"MaCready"**; film character is **"MacReady"**. Decision made: use **"MacReady"** — apply across card art + filename.

---

## Treachery / Role

### Infected (D) (#29)
- 📄 ☐ 🔠 Last line prints **"not *Required* to reveal"** (capital R) → lowercase **"required"** to match the Human role cards.

---

## Story / Reference Cards

### Repair Protocols (#31)
- 📄 ☐ ✏️ "Helicopter Pad" → "Ice Runway" reference fix.
- 📄 ☐ 🔠 Two mid-sentence **"Remove"** → lowercase **"remove"**.

### Station Protocol: Suspicion (#30)
- 📄 ☐ 🔠 Final action paragraph prints **"with *Suspicion* on them"** (capital S) → lowercase **"suspicion"** to match the rest of the card.

---

## Treachery & Enemy

### REQUIRED — location rename cross-refs (Helicopter Pad → Ice Runway)
- 📄 ☐ ✏️ **Paranoid Crew Member (A, #32)** — Spawn line: "Helicopter Pad" → "Ice Runway".
- 📄 ☐ ✏️ **The Thing (#18)** — Forced 2: "Helicopter Pad or Radio Room" → "Ice Runway or Radio Room".

### Title typos
- 📄 ☐ ✏️ **Losing Humnanity** (#52/53) → **Losing Humanity** (+ filename).
- 📄 ☐ ✏️ **Outside Interferance** (#54/55) → **Outside Interference** (+ filename).

### Capitalization
- 📄 ☐ 🔠 **Cornered** — "If you fail, You must" → "you".
- 📄 ☐ 🔠 **Paranoid Behaviour** — "Add 1 Suspicion" → "suspicion".
- 📄 ☐ 🔠 **Paranoid Crew Member (C)** — "Radio room" → "Radio Room".
- 📄 ☐ 🔠 **Short on Trust** — "crew Members" → "Crew Members".

### Grammar / punctuation / other
- 📄 ☐ ✏️ **Hunted** — "You must choose either (choose one)" is redundant → trim.
- 📄 ☐ ✏️ **Assimilation Nightmare** — Forced 2 missing terminal period.
- 📄 ☐ ✏️ **Terror from Within** — "person stood next to you" → "standing" (optional).
- 📄 ☐ ✏️ **The Thing** — trait "ELite" → "Elite".
- 📄 ☐ 🔠 **Paranoid Crew Member (A/B/C)** — "blood test card" → "Blood Test card".

---

## Number conflicts
- ❓ **Crawling Chaos (#46)** vs **Dwindling Supplies (#46)** — collision; Dwindling A likely should be #48. Verify master list.

---

## Decisions still open
- ❓ **Flamethrower** trait line "Item. Weapon. Firearm." — "Firearm" on a flamethrower is technically odd but was on the original; keep or change to "Item. Weapon."?
- ❓ **Organism** collector numbers — three modes (Creeping Chaos, Crushing Tendrils, Monstrous Growth) showed paired numbers (20b/21b, 22b/23b, 24b/25b). Confirm which physical copy is which.

---

## Card Data .md Status

| Type | Count |
|---|---|
| Card data files with Mod Changes documented | **28/28** — 100% |
| Strange Eons .eon projects created | **0/28** — 0% |
| **Strange Eons render pass remaining** | **28 items** |

## Render Pass Notes
- All 28 fixes are documented in the `## Mod Changes` section of each card's .md file in `Card Data - Original/`
- When creating the .eon project for each card in Strange Eons, apply the corrected text instead of the original verbatim text
- Card numbers match folder names in `Strange Eons - Art/Locations/` for location cards
- Story asset cards (#21a-25a) will go in appropriate character folders under `Strange Eons - Art/Characters/`
