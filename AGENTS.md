# AGENTS.md — Board Game Vault

## Project Overview

Obsidian vault for board game collection management, focused primarily on **Arkham Horror: The Card Game (AHLCG)**. Includes collection tracking, buying guides, substitution tables for legacy content, campaign notes, and fan scenario integration.

Current core: **Chapter Two Core Set (2026)**. Legacy campaigns acquired for story content only (player cards skipped where possible).

---

## Vault Structure

```
board-game-vault/
├── games/
│   └── arkham-lcg/
│       ├── index.md                    — AHLCG master index
│       ├── collection/
│       │   ├── core-set-2026.md        — Chapter Two core details
│       │   └── ...
│       ├── buying/
│       │   ├── guide.md                — purchase order recommendations
│       │   ├── products.md             — price table, best deals
│       │   ├── accessories.md          — sleeves, tokens, playmats, storage, apps
│       │   └── ...
│       ├── notes/
│       │   ├── legacy-content.md       — Chapter 1 buying guide with campaign priorities
│       │   ├── carcosa-guide.md        — DerBK substitution table (Carcosa)
│       │   ├── edge-of-the-earth-guide.md — DerBK substitution table (EotE)
│       │   ├── outpost31.md            — fan scenario guide + period re-flavor notes
│       │   ├── betrayal-at-the-mountains-of-madness.md — literary companion notes
│       │   ├── the-svalbard-event.md   — Arctic scenario notes
│       │   ├── fan-content-catalog.md  — ArkhamCentral scenario rankings
│       │   └── ...
│       ├── decks/
│       │   └── ...
│       ├── edge-of-the-earth/          — CAMPAIGN HUB (single source of truth)
│       │   ├── edge-of-the-earth.md
│       │   ├── Book - At the Mountains of Madness/   — Lovecraft novella (6 chapters)
│       │   ├── Edge of the Earth (Arkham Central)/   — original campaign (when acquired)
│       │   ├── edge-of-the-earth-mod/                — EotE modifications
│       │   ├── outpost31/ + outpost31-mod/           — prologue: Outpost 31
│       │   ├── betrayal-at-the-mountains-of-madness/ + -mod/  — interlude
│       │   └── the-svalbard-event/ + -mod/           — interlude
│       └── ...
├── AGENTS.md                           — this file
├── Home.md                             — vault landing page
├── README.md
└── templates/
```

---

## Tools & Software

| Tool | Purpose | Cost |
|---|---|---|
| **Claude Desktop** | Read card images, extract text/stats, design card mechanics & flavor text, write scripts | $20/mo |
| **Midjourney** | Generate card art in consistent style, inpaint/replace anachronistic art elements | Paid |
| **Strange Eons 3** | Recreate cards with official AHLCG templates, edit text, export print-ready PNGs with bleed | Free |
| **Krea AI** | AI image editor — upload existing cards, describe edits in plain English (e.g. "change helicopter to ski-plane") | Free daily credits |
| **GIMP** | Direct image editing — clone out old text, type new text, batch processing | Free |
| **MakePlayingCards (MPC)** | Print-on-demand: linen finish (matches FFG), no minimum order, ships worldwide | ~$0.30-0.60/card |
| **OpenCode** | Software engineering / automation tasks (batch rename, print sheets, organize files) | Bundled |
| **Obsidian** | Vault management, Dataview queries, note-taking | Paid |

---

## Golden Rule

**Original files are sacred, mod folders are for new work.** Always use original files as source material for verification (card text, stats, layout). All newly created or modified material goes in a `-mod` folder mirroring the original structure. Originals are never touched.

---

## Card Modification Workflow

When modifying a fan scenario (e.g. Outpost 31) to fit into a campaign:

1. **Identify target cards** — grep anachronisms, name mismatches, mechanical issues
2. **Extract card data** — upload card images to Claude Desktop, get full text/stats/traits
3. **Design changes** — decide new name/text/flavor, validate against official card conventions
4. **Create in Strange Eons** — use official AHLCG plugin templates
5. **Generate art** (if needed) — Midjourney with consistent prompt template, or Krea AI for inpainting existing art
6. **Export** PNG with bleed (3mm safe zone)
7. **Place in `outpost31-mod/`** matching original folder structure
8. **Print** via MPC (professional) or DIY (budget)

### Folder Convention for Modded Content

- Keep **original files untouched** in their original folder
- Place **all modified versions** in `[scenario-name]-mod/` mirroring the original structure
- Document every change in the corresponding `.md` note file

---

## Outpost 31 → Edge of Earth Prologue

### Narrative Setting
- **Time:** 1920s (must match Edge of the Earth)
- **Premise:** Investigators are a Miskatonic University rescue team dispatched to Outpost 31 after contact is lost
- **Tone:** The Thing meets Arkham LCG — paranoia, isolation, ancient horror beneath the ice
- Connection: The "organism" is an escaped Elder Thing guardian experiment. Survivors' trails lead into EotE's campaign.

### Cards to Modify

| Original | Changed To | Reason |
|---|---|---|
| Helicopter-Pad (location) | **Ice Runway** / Landing Strip | Helicopters didn't exist in 1920s Antarctica |
| Station-Protocol (treachery) | **Station Procedures** / Standing Orders | "Protocols" is modern jargon |
| Repair-Protocols (story asset) | **Repair Orders** / Maintenance Schedule | Same reason |
| Vehicle-Storage (location) | Keep name, re-flavor text | Flavor as housing ski-plane + dog sleds |
| "Helicopter" in any card text | Replace with "ski-plane" / "aeroplane" | Period accuracy |

### Period-Accurate Details (no change needed)
- Flamethrower (existed since WWI, 1915)
- Radio communication (standard in 1920s)
- Blood tests, medical quarantine, autopsies
- Dog sleds as primary Antarctic transport

---

## Printing & Production

### Professional (Recommended for final versions)
- **MakePlayingCards** — linen air finish (closest to FFG feel), 300gsm or 310gsm French stock
- Upload individual card PNGs with 3mm bleed
- No minimum order — print single decks

### DIY (Budget / prototyping)
- **Setup cost:** ~$100-150 once
  - Printer: any color inkjet (Epson EcoTank ideal for volume)
  - Rotary paper trimmer (~$20)
  - Corner rounder (~$10)
  - Optional: laminator (~$30)
- **Per 100 cards:** ~$20-30
  - 270-300gsm matte cardstock
- **Methods:**
  1. Print on paper + sleeve over bulk MTG/common card (best feel-cost ratio)
  2. Sticker paper on bulk cards
  3. Direct print on 300gsm cardstock

---

## Legacy Campaign Buying Strategy

All buying via `games/arkham-lcg/buying/`:

| Campaign | Status | Priority | Notes |
|---|---|---|---|
| Path to Carcosa | Best deal identified (~$70 Asmodee) | High | Best story, forgiving with shallow card pool, substitution guide done |
| Edge of the Earth | Out of Print from FFG, ~$170 eBay | Medium | Substitution guide + Outpost 31 prologue done, wait for restock or fair price |
| Dunwich Legacy | Not yet researched | Low | |
| Forgotten Age | Not yet researched | Low | |
| Circle Undone | Not yet researched | Low | |

**Rule:** Buy Campaign Expansions only (story). Skip Investigator Expansions unless the player cards are uniquely valuable.

---

## Key Decisions (do not override)

- Starting from Chapter Two Core Set (2026) — 357 cards, 5 investigators
- Not buying legacy player cards unless needed for substitution
- Outpost 31 is a prologue to Edge of the Earth (NOT standalone)
- All modifications must preserve 1920s period accuracy
- **Golden Rule:** Original files are sacred, used only for source/verification. All new/modified material goes in `-mod` folders. Originals are never touched.
