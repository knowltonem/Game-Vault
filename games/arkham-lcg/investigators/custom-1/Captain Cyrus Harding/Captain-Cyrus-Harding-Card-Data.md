# Captain Cyrus Harding — Investigator Pack (RYP-CH)

← [[games/arkham-lcg/investigators/custom-1/index|Back to Custom Investigators]]

---

> **DECK LOCKED** — Do not change card order or names without updating all folders and Card-Data simultaneously.

---

## Investigator Card

| Field | Value |
|---|---|
| **Name** | Captain Cyrus Harding |
| **Subtitle** | Lost at Sea |
| **Class** | Survivor |
| **Traits** | Drifter. Sailor. Captain. |
| **Willpower** | 4 |
| **Intellect** | 2 |
| **Combat** | 3 |
| **Agility** | 4 |
| **Health** | 8 |
| **Sanity** | 6 |

### Ability
```
<rea> After an asset you control 
is exhausted: Ready it. 
(Limit once per round.)
```

### Elder Sign
```
<eld> +1. Ready Snips. (This does not
count toward the once per round limit.)
```

### Flavor (front)
```
"The Storm Witch is gone.
Snips is still here.
That'll have to be enough."
```

### Story (back)
```
Cyrus Harding has sailed the North
Atlantic for thirty years. He knows
every current, every weather sign,
every trick the sea plays on men who
think they know her. He did not know
what pulled the Storm Witch off course
that night. He did not know what the
storm was hiding. He washed up on the
Arkham shoreline with nothing but the
clothes on his back and Snips on his
shoulder. He needs to fix his rig and
get back out there. But Arkham has
other ideas. And whatever came out of
that storm followed him ashore.
```

### Deckbuilding
```
Deck size: 30.
Survivor cards (level 0-5).
Neutral cards (level 0-5).
```

### Deckbuilding Restrictions
```
Snipps begins the game in play.
It is permanent.
```

### Deckbuilding Requirements
```
(do not count toward deck size)
Spyglass, Old Friends,
Storm Wraith, 1 random Basic Weakness.
```

---

## Signature Cards (outside deck)

### 001 — Captain Cyrus Harding
*Investigator card — see above.*

---

### 002 — Snipps

| Field | Value |
|---|---|
| **Type** | Asset — Ally — Permanent |
| **Class** | Survivor |
| **Traits** | Ally. Creature. |
| **Slot** | — (no slot) |
| **Unique** | Yes |

```
Captain Cyrus Harding deck only.
Permanent.

You get +1 <int> while Snipps
is in play.

<act> Exhaust Snipps: Investigate.
You investigate with a base skill
of 4. You may move to a connecting
location immediately before
investigating with this effect.

<act> Exhaust Snipps: Fight. You
attack with a base skill of 4.
This attack deals +1 damage.
```
*Flavor: TBD*

---

### 003 — Spyglass

| Field | Value |
|---|---|
| **Type** | Asset — Accessory |
| **Cost** | 2r |
| **Class** | Survivor |
| **Traits** | Item. Relic. Nautical. |
| **Slot** | Accessory |
| **Unique** | Yes |
| **Icons** | 1 x agi |

```
Captain Cyrus Harding deck only.

<act> Exhaust Spyglass: Investigate.
Use <agi> instead of <int> for this
investigation. If successful: Draw 1
card and gain 1 resource.
```
*Flavor: "He sees things coming. He always has."*

---

### 004 — Old Friends

| Field | Value |
|---|---|
| **Type** | Treachery — Weakness |
| **Class** | Neutral |
| **Traits** | Curse. Pact. |
| **Unique** | Yes |

```
Captain Cyrus Harding deck only.

Revelation: Spawn Old Friends at
your location as an enemy.

Old Friends — Enemy
HP: 2 | Fight: 3 | Evade: 2
Damage: 1 | Horror: 0
Hunter.
```
*Flavor: "They followed him ashore."*

---

## Deck (005-034)

| # | Card | × | Cost | Slot | Class |
|---|---|---|---|---|---|
| 005 | Storm Coat | 1 | 0r | Body | Survivor (custom) |
| 006 | Captain's Hat | 1 | 0r | — | Survivor (custom) |
| 007-008 | Blunderbuss | 2 | 3r | Hand | Survivor (custom) |
| 009-010 | All Hands on Deck | 2 | 2r | — | Survivor (custom) |
| 011-012 | Harpoon | 2 | 1r | Hand | Survivor (custom) |
| 013-014 | Boarding Party | 2 | 2r | — | Survivor (custom) |
| 015-016 | Sail Away | 2 | 2r | — | Survivor (custom) |
| 017-018 | Captain's Stash | 2 | 0r | — | Neutral (custom) |
| 019-020 | Sea Bounty | 2 | 2r | — | Survivor (custom) |
| 021-022 | Sea Witch's Revenge | 2 | 1r | Arcane | Survivor (custom) |
| 023-024 | Lucky! | 2 | 0r | — | Neutral (lvl 0) |
| 025-026 | Swab the Deck | 2 | 2r | — | Survivor (custom) |
| 027-028 | Take Heart | 2 | 0r | — | Survivor (lvl 0) |
| 029-030 | The Perfect Storm | 2 | — | — | Survivor (custom) |
| 031 | Guts | 1 | — | — | Neutral (lvl 0) |
| 032 | Perception | 1 | — | — | Neutral (lvl 0) |
| 033-034 | Unexpected Courage | 2 | — | — | Neutral (lvl 0) |

### Custom Cards in Deck

| Card | Effect |
|---|---|
| Storm Coat | Asset, body slot, HP soak 3, cost 0r. Icons `<wld>` |
| Captain's Hat | Asset, no slot, SAN +2, cost 0r. Icons `<wld><wld>` |
| Blunderbuss | Asset, hand slot, cost 3r, uses 3 ammo. Fight +3 COM +2 dmg. Succeed by 2+: deal 1 dmg to each other enemy at location. Icons `<com><com>` |
| Harpoon | Asset, hand slot, cost 1r. Fight +X COM where X = cards in hand. After attack: discard 1 random card from hand. Icons `<com>` |
| The Perfect Storm | Skill, `<wld><wld><wld>`, if successful: draw 1 card and take 1 damage |
| Captain's Stash | Event, cost 0r, fast. Gain 3 resources. Icons `<wld>` |
| All Hands on Deck | Asset, no slot, cost 3r. +1 to all skills while you have 0 resources. Icons `<wld>` |
| Sail Away | Event, cost 2r, fast. Disengage from each enemy. Move up to 2 locations. No attacks of opportunity. Icons `<agi><agi>` |
| Swab the Deck | Event, cost 2r, fast. Play when you fail investigation by 1-2: discover 2 clues at your location. Icons `<int><int>` |
| Boarding Party | Asset, no slot, cost 2r. `<act>` Exhaust: draw 1 chaos token. On skull/cultist/tablet/elder thing/auto-fail: nothing. Otherwise: deal 2 dmg to each enemy at location. You may push your luck to deal 3 dmg instead. Icons `<com><com>` |

---

## Pack Information

| Field | Value |
|---|---|
| **Pack Name** | Captain Cyrus Harding Investigator Pack |
| **Pack Code** | RYP-CH |
| **Investigator** | 001 Captain Cyrus Harding |

---

## Skill Icon Audit (EON-verified 2026-08-23)

Extracted programmatically from the `Skill1`–`Skill6` properties stored inside each card's `.eon` file.

| Metric | Value |
|---|---|
| Deck cards scanned | 32 |
| No icon | 5 |
| Single icon | 11 |
| Double icons | 14 |
| Triple icons | 2 |
| Total icons | 45 |

| Icon type | Uses |
|---|---|
| Wild (WILD) | 19 |
| Willpower (WIL) | 8 |
| Intellect (INT) | 8 |
| Combat (COM) | 6 |
| Agility (AGI) | 4 |

**Multi-icon cards**

| # | Card | Icons |
|---|---|---|
| 003 | Spyglass | WIL/WIL |
| 006 | Captain's Hat | WILD/WILD |
| 009-010 | All Hands on Deck ×2 | WIL/WIL |
| 013-014 | Boarding Party ×2 | COM/COM |
| 015-016 | Sail Away ×2 | AGI/AGI |
| 025-026 | Swab the Deck ×2 | INT/INT |
| 029-030 | The Perfect Storm ×2 | WILD/WILD/WILD |
| 031 | Guts | WIL/WIL |
| 032 | Perception | INT/INT |
| 033-034 | Unexpected Courage ×2 | WILD/WILD |
