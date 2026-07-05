# The R'lyeh Expansion — Upgrade Pack (RYP-UP)

← [[games/arkham-lcg/investigators/custom-1/index|Back to Custom Investigators]]

---

## Pack Information

| Field | Value |
|---|---|
| **Expansion** | The R'lyeh Expansion |
| **Pack Name** | R'lyeh Upgrade Pack |
| **Pack Code** | RYP-UP |
| **Investigators** | Ironhide, Greystoke, Agnes, Abel (scales to 6) |

---

## Naming Convention

| File Type | Convention | Example |
|---|---|---|
| **Folders** | `###-Card-Name-Level` | `001-Father-Thomas-2` |
| **EON files** | `UP-[Investigator]-[Name]-Lv[#].eon` | `UP-Ironhide-Father-Thomas-Lv2.eon` |
| **Exported PNGs** | `RYP-UP-###-[Name]-Lv[#]-[Front/Back].png` | `RYP-UP-001-Father-Thomas-Lv2-Front.png` |

---

## Standing Rules

- Check card-reference.md before printing any official base card
- All upgrade cards use same Strange Eons templates as their base type
- ★ = Signature upgrade — deck restricted text required
- ✦ = New custom card — no official base card reference
- Official reskins use official card text with custom name/traits/flavor only

---

## Folder Structure

```
Upgrade Pack/
├── Guardian/
│   ├── 001-Father-Thomas-Lv2/
│   ├── 002-Father-Thomas-Lv4/
│   ├── 003-Hound-of-the-Deep-Lv2/
│   ├── 004-Hound-of-the-Deep-Lv4/
│   ├── 005-Aquinnah-Lv3/
│   ├── 006-Aquinnah-Lv5/
│   ├── 007-The-Hollow-Warden-Lv3/
│   ├── 008-Rlyeh-Fury-Lv2/
│   ├── 009-Ward-of-Protection-Lv2/
│   ├── 010-Spirit-Coyote-Lv2/
│   ├── 011-Spirit-Coyote-Lv3/
│   ├── 012-Spirit-Coyote-Lv5/
│   ├── 013-The-Sacred-Spear-Lv3/
│   ├── 014-Multi-Shot-Lv2/
│   ├── 015-Fire-Walker-Lv2/
│   ├── 016-Bear-Pelt-Lv2/
│   └── 017-Ancient-Warrior-Lv4/
├── Seeker/
│   ├── 018-The-Unbroken-Codex-Lv2/
│   ├── 019-My-Eyes-and-Ears-Lv2/
│   ├── 020-The-Ancient-Binding-Lv2/
│   ├── 021-The-Ancient-Binding-Lv4/
│   ├── 022-The-Relic-Harvester-Lv2/
│   ├── 023-The-Relic-Harvester-Lv4/
│   ├── 024-Centuries-of-Memory-Lv1/
│   ├── 025-Intellectual-Violence-Lv3/
│   ├── 026-Centuries-of-Knowledge-Lv3/
│   └── 027-The-Immortals-Eye-Lv4/
├── Mystic/
│   ├── 028-The-Night-Gaunt-Lv2/
│   ├── 029-The-Night-Gaunt-Lv4/
│   ├── 030-The-Night-Gaunt-Lv5/
│   ├── 031-Arcane-Athame-Lv3/
│   └── 032-Rain-Dance-Lv2/
├── Survivor/
│   ├── 033-The-Pale-Child-Lv2/
│   ├── 034-The-Pale-Child-Lv3/
│   ├── 035-The-Pale-Child-Lv5/
│   ├── 036-The-Third-Eye-Lv1/
│   ├── 037-Lucky-Lv2/
│   ├── 038-Grotesque-Statue-Lv4/
│   ├── 039-Sweat-Lodge-Lv3/
│   └── 040-Awaken-the-Spirits-Lv3/
├── Neutral/
│   ├── 041-Ancient-Cache-Lv0/
│   ├── 042-Ancient-Cache-Lv2/
│   ├── 043-Charisma-Lv3/
│   └── 044-Relic-Hunter-Lv3/
└── RYP-UP-Upgrade-Pack-Card-Data.md
```

---

## Guardian Upgrades

---

### 001 — Father Thomas (2) ★ Reskin
**Base:** Beat Cop (2) | **Investigator:** Ironhide | **XP:** 4

| Field | Value |
|---|---|
| Type | Asset — Ally |
| Cost | 4r |
| Traits | Ally. Blessed. |
| HP soak | 3 |
| SAN soak | 2 |
| Icons | 1 × `<wil>` + 1 × `<com>` |

```
You get +1 <com> while Father Thomas is in play.
<fre> Exhaust Father Thomas and deal 1 damage to it:
Deal 2 damage to an enemy at your location.
```
*Flavor: "The priest has seen what Ironhide has seen. He stopped flinching first."*

---

### 002 — Father Thomas (4) ✦ Custom
**Investigator:** Ironhide | **XP:** 8 total (4 from Lv 2)

| Field | Value |
|---|---|
| Type | Asset — Ally |
| Cost | 4r |
| Traits | Ally. Blessed. |
| HP soak | 3 |
| SAN soak | 3 |
| Icons | 1 × `<wil>` + 1 × `<com>` |

```
You get +1 <com> while Father Thomas is in play.
<fre> Exhaust Father Thomas and deal 1 damage to it:
Deal 2 damage to an enemy at your location and add
1 bless token to the chaos bag.
```
*Flavor: "Every enemy that falls is one fewer soul the darkness can claim. He makes sure they know it."*

---

### 003 — Hound of the Deep (2) ✦ Custom
**Investigator:** Ironhide | **XP:** 4

| Field | Value |
|---|---|
| Type | Asset — Ally |
| Cost | 3r |
| Traits | Ally. Monster. Cursed. |
| HP soak | 4 |
| SAN soak | 2 |
| Icons | 1 × `<com>` + 1 × `<wil>` |

```
You get +2 <com> while Hound of the Deep is in play.
<rea> When an enemy attack deals damage to you:
Exhaust Hound of the Deep — deal 2 damage to the
attacking enemy. If a <curse> token was revealed
this round: Deal 3 damage instead.
```
*Flavor: "It came back with me. I never asked it to. I stopped complaining."*

---

### 004 — Hound of the Deep (4) ✦ Custom
**Investigator:** Ironhide | **XP:** 8 total (4 from Lv 2)

| Field | Value |
|---|---|
| Type | Asset — Ally |
| Cost | 3r |
| Traits | Ally. Monster. Cursed. |
| HP soak | 5 |
| SAN soak | 2 |
| Icons | 1 × `<com>` + 1 × `<wil>` |

```
You get +2 <com> while Hound of the Deep is in play.
<rea> When an attack of opportunity or enemy attack
deals damage to you: Exhaust Hound of the Deep —
deal 3 damage to the attacking enemy and add 1 curse
token to the chaos bag. If a <curse> token was
revealed this round: Deal 4 damage instead.
```
*Flavor: "The city marked it the same way it marked me. We understand each other."*

---

### 005 — Aquinnah (3) Reskin
**Base:** Aquinnah (3) | **Investigator:** Ironhide | **XP:** 4

| Field | Value |
|---|---|
| Type | Asset — Ally |
| Cost | 4r |
| Traits | Ally. Blessed. |
| HP soak | 1 |
| SAN soak | 4 |
| Icons | 1 × `<wil>` |

```
<rea> When an attack of opportunity or enemy attack
deals damage to you, exhaust Aquinnah and deal 1
horror to her: Deal that damage to any enemy at
your location instead. You still take any horror
dealt by the attack.
```
*Flavor: "Do not be frightened by what you see. Be frightened by what you cannot see."*

---

### 006 — Aquinnah (5) ✦ Custom
**Investigator:** Ironhide | **XP:** 10 total (4 from Lv 3)

| Field | Value |
|---|---|
| Type | Asset — Ally |
| Cost | 5r |
| Traits | Ally. Blessed. |
| HP soak | 2 |
| SAN soak | 4 |
| Icons | 1 × `<wil>` |

```
<rea> When an attack of opportunity or enemy attack
deals damage to you, exhaust Aquinnah and deal 1
horror to her: Deal that damage to ALL enemies at
your location instead. You still take any horror
dealt by the attack.
```
*Flavor: "She stopped redirecting it. Now she shares it with everyone in the room."*

---

### 007 — The Hollow Warden (3) ★ ✦ Custom
**Investigator:** Ironhide only | **XP:** 6

| Field | Value |
|---|---|
| Type | Asset — Hand |
| Cost | 0r |
| Traits | Item. Weapon. Firearm. Relic. |
| Slot | Hand |
| Uses | 4 ammo |
| Icons | 1 × `<com>` |

```
Ironhide deck only.
Uses (4 ammo).
<act> Spend 1 ammo: Fight. You get +2 <com> for this
attack and deal +2 damage. If this attack defeats an
enemy: Draw 1 card and gain 1 resource. If a <curse>
token is revealed during this attack: Deal +2
additional damage instead.
<act> Spend 1 resource: Add 3 ammo to The Hollow Warden.
<fre> At the start of your turn, if The Hollow Warden
has 0 ammo: Add 1 ammo to it.
<fre> If there are no enemies at your location: Draw 1 card.
```
*Flavor: "R'lyeh made it. It was always going to get stronger the longer it stayed with me."*

---

### 008 — R'lyeh's Fury (2) ★ Reskin
**Base:** Vicious Blow (2) | **Investigator:** Ironhide | **XP:** 4

| Field | Value |
|---|---|
| Type | Skill |
| Traits | Practiced. Cursed. |
| Icons | 2 × `<com>` |

```
If this skill test is successful during an attack,
that attack deals +2 damage.
```
*Flavor: "The city taught me how to hit harder. I kept that lesson."*

---

### 009 — Ward of Protection (2) Reskin
**Base:** Ward of Protection (2) | **All investigators** | **XP:** 4

| Field | Value |
|---|---|
| Type | Event |
| Cost | 1r |
| Traits | Spell. Spirit. |
| Icons | 1 × `<wil>` |

```
Fast. Play when you or another investigator at your
location would draw a non-weakness treachery card.
Cancel that card's revelation effect. The affected
investigator takes 1 horror.
```
*Flavor: "Some protections do not ask for permission."*

---

### 010 — Spirit Coyote (2) ✦ Reskin
**Base:** Guard Dog (2) | **Investigator:** Abel | **XP:** 4

| Field | Value |
|---|---|
| Type | Asset — Ally |
| Cost | 3r |
| Traits | Ally. Spirit. Creature. |
| HP soak | 3 |
| SAN soak | 2 |
| Icons | 1 × `<com>` + 1 × `<wil>` |

```
You get +1 <com> while Spirit Coyote is in play.
<rea> When an enemy attack deals damage to you:
Exhaust Spirit Coyote — deal 2 damage to the
attacking enemy.
```
*Flavor: "It remembered what hurt me. It made sure they felt it too."*

---

### 011 — Spirit Coyote (3) ✦ Custom
**Investigator:** Abel | **XP:** 6 total (2 from Lv 2)

| Field | Value |
|---|---|
| Type | Asset — Ally |
| Cost | 3r |
| Traits | Ally. Spirit. Creature. |
| HP soak | 4 |
| SAN soak | 2 |
| Icons | 1 × `<com>` + 1 × `<wil>` |

```
You get +2 <com> while Spirit Coyote is in play.
<rea> When an attack of opportunity or enemy attack
deals damage to you: Exhaust Spirit Coyote — deal
2 damage to the attacking enemy.
```
*Flavor: "It does not wait to be asked anymore. It knows."*

---

### 012 — Spirit Coyote (5) ✦ Custom
**Investigator:** Abel | **XP:** 10 total (4 from Lv 3)

| Field | Value |
|---|---|
| Type | Asset — Ally |
| Cost | 4r |
| Traits | Ally. Spirit. Creature. |
| HP soak | 5 |
| SAN soak | 3 |
| Icons | 1 × `<com>` + 1 × `<wil>` |

```
You get +2 <com> while Spirit Coyote is in play.
<rea> When an attack of opportunity or enemy attack
deals damage to you: Exhaust Spirit Coyote — deal
3 damage to the attacking enemy and add 1 bless
token to the chaos bag.
<fre> After Spirit Coyote's reaction defeats an enemy:
Ready Spirit Coyote.
```
*Flavor: "The coyote does not guard. It hunts. There is a difference."*

---

### 013 — The Sacred Spear (3) ★ ✦ Custom
**Investigator:** Abel only | **XP:** 6

| Field | Value |
|---|---|
| Type | Asset — Hand ×2 |
| Cost | 0r |
| Traits | Item. Weapon. Relic. Blessed. |
| Icons | 1 × `<com>` + 1 × `<wil>` |

```
Abel Redcloud deck only.
<act> Fight. You may target an enemy at a connecting
location. You get +2 <com> for this attack. This
attack deals +2 damage.
<fre> After you defeat an enemy with The Sacred Spear:
Add 2 bless tokens to the chaos bag.
```
*Flavor: "The ancestors made it for this. For all of it."*

---

### 014 — Multi-Shot (2) ✦ Custom
**Investigator:** Abel | **XP:** 4

| Field | Value |
|---|---|
| Type | Event |
| Cost | 2r |
| Traits | Tactic. Spirit. Tribal. |
| Icons | 2 × `<com>` + 1 × `<agi>` |

```
Requires The Sacred Bow in play. Fast.
Spend 2 arrows from The Sacred Bow: Fight. This
attack may target up to 3 enemies at your location
or at connecting locations simultaneously. You get
+1 <com> for this attack. Each defeated enemy
triggers The Sacred Bow's ability separately —
draw 1 card for each enemy defeated.
```
*Flavor: "The ancestors guide each arrow to where it is needed. I simply release."*

---

### 015 — Fire Walker (2) ✦ Custom
**Investigator:** Abel | **XP:** 4

| Field | Value |
|---|---|
| Type | Event |
| Cost | 2r |
| Traits | Spell. Spirit. Tribal. |
| Icons | 1 × `<wil>` + 1 × `<agi>` + 1 × `<com>` |

```
Fast. Move Abel Redcloud to any location on the board.
You must move to a location that has at least 1 clue
or 1 enemy present. Enemies do not make attacks of
opportunity against Abel Redcloud this round.
Immediately after moving: You may perform 1 fight
action without spending an action.
```
*Flavor: "The fire delivers you. What you do when you arrive is your own business."*

---

### 016 — Bear Pelt (2) ✦ Custom
**Investigator:** Abel | **XP:** 4

| Field | Value |
|---|---|
| Type | Asset — Body |
| Cost | 2r |
| Traits | Item. Relic. Blessed. |
| HP soak | 3 |
| SAN soak | 1 |
| Icons | 1 × `<wil>` |

```
You get +1 <wil> while Bear Pelt is in play.
<rea> After you take damage from an enemy attack:
Exhaust Bear Pelt — reduce that damage by 1.
```
*Flavor: "The bear did not give this willingly. Nothing worth having ever does."*

---

### 017 — Ancient Warrior (4) ★ ✦ Custom
**Investigator:** Abel only | **XP:** 8

| Field | Value |
|---|---|
| Type | Event |
| Cost | 2r |
| Traits | Tactic. Spirit. Tribal. |
| Icons | 1 × `<wil>` + 1 × `<com>` |

```
Abel Redcloud deck only. Fast.
Choose an enemy at your location or a connecting
location. That enemy gets -2 fight and -2 evade
until the end of the round. Add 2 bless tokens to
the chaos bag. Heal 1 damage and 1 horror from
Abel Redcloud.
```
*Flavor: "Four generations of keepers showed me how to face this. I remember all of them."*

---

## Seeker Upgrades

---

### 018 — The Unbroken Codex (2) ★ ✦ Custom
**Investigator:** Greystoke only | **XP:** 4

| Field | Value |
|---|---|
| Type | Asset — Arcane |
| Cost | 2r |
| Traits | Item. Tome. Relic. |
| Slot | Arcane |
| Icons | 1 × `<int>` |

```
Alistair Greystoke deck only.
You may use your <int> instead of <agi> when evading
enemies. Each investigator at your location may use
your <int> instead of their own <agi> when evading.
<rea> After you would be dealt horror from an encounter
card or enemy effect: Exhaust The Unbroken Codex —
ignore 1 of that horror.
<rea> After any investigator at your location
successfully investigates: Exhaust The Unbroken Codex
— cancel the next horror that investigator would be
dealt until the end of this round.
```
*Flavor: "Two hundred years of knowing how they move. Now I can show you."*

---

### 019 — My Eyes and Ears (2) ✦ Custom
**Investigator:** Greystoke only | **XP:** 4

| Field | Value |
|---|---|
| Type | Asset — Ally |
| Cost | 3r |
| Traits | Ally. Creature. Swarm. |
| HP soak | 3 |
| SAN soak | 3 |
| Icons | 1 × `<int>` |

```
Alistair Greystoke deck only.
<rea> After you successfully investigate: Discover
1 additional clue at your location.
Forced — When My Eyes and Ears is defeated: Place
1 doom on the current agenda.
```
*Flavor: "There are more of them now. There always are."*

---

### 020 — The Ancient Binding (2) ✦ Custom
**Investigator:** Greystoke only | **XP:** 4

| Field | Value |
|---|---|
| Type | Asset — Ally |
| Cost | 3r |
| Traits | Ally. Monster. Dimensional. |
| HP soak | 4 |
| SAN soak | 4 |
| Icons | 1 × `<wil>` |

```
Alistair Greystoke deck only.
<rea> After you would be dealt damage or horror:
Exhaust The Ancient Binding — prevent 2 of that
damage or horror.
Forced — When The Ancient Binding is defeated:
Take 1 horror and shuffle The Ancient Binding
back into your deck.
```
*Flavor: "It does not age. Neither do I. We have an understanding."*

---

### 021 — The Ancient Binding (4) ✦ Custom
**Investigator:** Greystoke only | **XP:** 8 total (4 from Lv 2)

| Field | Value |
|---|---|
| Type | Asset — Ally |
| Cost | 3r |
| Traits | Ally. Monster. Dimensional. |
| HP soak | 5 |
| SAN soak | 5 |
| Icons | 1 × `<wil>` |

```
Alistair Greystoke deck only.
<rea> After you would be dealt damage or horror:
Exhaust The Ancient Binding — prevent 2 of that
damage or horror. You may deal that amount of
damage to any enemy at your location.
Forced — When The Ancient Binding is defeated:
Take 1 horror, draw 1 card, and shuffle The
Ancient Binding back into your deck.
```
*Flavor: "I have watched it fight for me for two hundred years. I have never seen it tire."*

---

### 022 — The Relic Harvester (2) ✦ Custom
**Investigator:** Greystoke only | **XP:** 4

| Field | Value |
|---|---|
| Type | Asset — Ally |
| Cost | 3r |
| Traits | Ally. Monster. Mi-Go. |
| HP soak | 3 |
| SAN soak | 2 |
| Icons | 1 × `<int>` |

```
Alistair Greystoke deck only.
After you discover 1 or more clues (by any means):
Gain 1 resource.
<act> Exhaust The Relic Harvester: Search the top
5 cards of your deck for an Item asset and draw it.
Shuffle your deck.
```
*Flavor: "The debt compounds. It seems content with the arrangement."*

---

### 023 — The Relic Harvester (4) ✦ Custom
**Investigator:** Greystoke only | **XP:** 8 total (4 from Lv 2)

| Field | Value |
|---|---|
| Type | Asset — Ally |
| Cost | 3r |
| Traits | Ally. Monster. Mi-Go. |
| HP soak | 4 |
| SAN soak | 3 |
| Icons | 1 × `<int>` |

```
Alistair Greystoke deck only.
After any investigator at your location discovers
1 or more clues: Gain 1 resource.
<fre> After you successfully investigate: You may
exhaust The Relic Harvester to search the top 10
cards of your deck for an Item asset and draw it.
Shuffle your deck.
```
*Flavor: "A life spared. Two hundred years repaid. We are almost even."*

---

### 024 — Centuries of Memory (1) ✦ Custom
**Investigator:** Greystoke | **XP:** 2

| Field | Value |
|---|---|
| Type | Skill |
| Traits | Innate. Insight. |
| Icons | 2 × `<int>` |

```
After you commit Centuries of Memory to a skill
test and succeed: Draw 1 card. If you discovered
1 or more clues this round, draw 2 cards instead.
```
*Flavor: "Two hundred years of pattern recognition. The answer was already there."*

---

### 025 — Intellectual Violence (3) ✦ Custom
**Investigator:** Greystoke | **XP:** 6

| Field | Value |
|---|---|
| Type | Event |
| Cost | 2r |
| Traits | Insight. Tactic. |
| Icons | 2 × `<int>` + 1 × `<wil>` |

```
<act> Intellect test (difficulty equal to the enemy's
fight value). If you succeed, deal 2 damage to that
enemy. That enemy cannot retaliate this round.
If you succeed by 2 or more, deal 3 damage instead
and discover 1 clue at your location.
```
*Flavor: "I have studied everything that lives in the dark for two hundred years. I know exactly where it hurts."*

---

### 026 — Centuries of Knowledge (3) ✦ Custom
**Investigator:** Greystoke only | **XP:** 6

| Field | Value |
|---|---|
| Type | Asset — Arcane |
| Cost | 3r |
| Traits | Insight. Relic. Tome. |
| Slot | Arcane |
| Icons | 2 × `<int>` |

```
Alistair Greystoke deck only. Unique.
<fre> At the start of your turn: Look at the top 5
cards of the encounter deck and arrange them in
any order.
<act> Exhaust Centuries of Knowledge: Choose an
investigator at your location. That investigator
does not draw an encounter card this round.
<rea> After any investigator at your location would
draw a treachery card: Exhaust Centuries of Knowledge
— cancel that card's revelation effect. It is
discarded instead.
```
*Flavor: "I have seen every horror this world can produce. None of them surprise me anymore."*

---

### 027 — The Immortal's Eye (4) ✦ Custom
**Investigator:** Greystoke only | **XP:** 8

| Field | Value |
|---|---|
| Type | Asset — Arcane |
| Cost | 3r |
| Traits | Insight. Relic. |
| Slot | Arcane |
| Icons | 2 × `<int>` |

```
Alistair Greystoke deck only. Unique.
<fre> At the start of the enemy phase: Look at the
top card of the encounter deck. You may move it to
the bottom of the deck.
<act> Exhaust The Immortal's Eye: Choose an investigator
at your location. That investigator gets +3 <int>
until the end of the round.
<rea> After any investigator at your location would
draw a treachery: Exhaust The Immortal's Eye — that
investigator may discard it unresolved instead.
Take 1 horror.
```
*Flavor: "I have watched it all for two centuries. Nothing surprises me. Everything horrifies me."*

---

## Mystic Upgrades

---

### 028 — The Night-Gaunt (2) ★ ✦ Custom
**Investigator:** Agnes only | **XP:** 4

| Field | Value |
|---|---|
| Type | Asset — Ally |
| Cost | 3r |
| Traits | Ally. Monster. Night-Gaunt. |
| HP soak | 3 |
| SAN soak | 3 |
| Icons | 1 × `<wil>` |

```
Agnes Crane deck only.
You get +2 <wil> while The Night-Gaunt is in play.
<rea> After you would take horror: Exhaust The
Night-Gaunt — prevent 2 of that horror.
```
*Flavor: "It has learned what I need. It does not ask why."*

---

### 029 — The Night-Gaunt (4) ★ ✦ Custom
**Investigator:** Agnes only | **XP:** 8 total (4 from Lv 2)

| Field | Value |
|---|---|
| Type | Asset — Ally |
| Cost | 3r |
| Traits | Ally. Monster. Night-Gaunt. |
| HP soak | 4 |
| SAN soak | 4 |
| Icons | 1 × `<wil>` |

```
Agnes Crane deck only.
You get +2 <wil> while The Night-Gaunt is in play.
<rea> After you would take horror: Exhaust The
Night-Gaunt — prevent 2 of that horror.
<fre> Once per round, after The Night-Gaunt prevents
horror: Deal 1 damage to any enemy at your location
or a connecting location.
```
*Flavor: "It does not just protect me now. It hunts what hurts me."*

---

### 030 — The Night-Gaunt (5) ★ ✦ Custom
**Investigator:** Agnes only | **XP:** 10 total (2 from Lv 4)

| Field | Value |
|---|---|
| Type | Asset — Ally |
| Cost | 3r |
| Traits | Ally. Monster. Night-Gaunt. |
| HP soak | 5 |
| SAN soak | 4 |
| Icons | 1 × `<wil>` |

```
Agnes Crane deck only.
You get +2 <wil> while The Night-Gaunt is in play.
<rea> After you would take horror: Exhaust The
Night-Gaunt — prevent 3 of that horror.
<fre> Once per round, after The Night-Gaunt prevents
horror: Deal 2 damage to any enemy at your location
or a connecting location.
```
*Flavor: "I stopped running from it. Now nothing runs from us."*

---

### 031 — Arcane Athame (3) ★ ✦ Custom
**Investigator:** Agnes only | **XP:** 6

| Field | Value |
|---|---|
| Type | Asset — Hand |
| Cost | 2r |
| Traits | Item. Weapon. Relic. Cursed. |
| Slot | Hand |
| Icons | 2 × `<wil>` + 1 × `<com>` |

```
Agnes Crane deck only.
<act> Fight. You get +2 <com> for this attack.
<fre> After you defeat an enemy with Arcane Athame:
Heal 2 horror from Agnes Crane.
<fre> After you defeat an enemy with Arcane Athame:
Add 1 bless token to the chaos bag.
```
*Flavor: "Hamunaptra gave it power. I gave it purpose."*

---

### 032 — Rain Dance (2) ✦ Reskin
**Base:** Ward of Protection (2) | **Investigator:** Abel | **XP:** 4

| Field | Value |
|---|---|
| Type | Event |
| Cost | 1r |
| Traits | Spell. Spirit. Tribal. |
| Icons | 1 × `<wil>` |

```
Fast. Play when you or another investigator at your
location would draw a non-weakness treachery card.
Cancel that card's revelation effect. The affected
investigator takes 1 horror.
```
*Flavor: "The rain does not ask permission. Neither does the prayer."*

---

## Survivor Upgrades

---

### 033 — The Pale Child (2) ★ ✦ Custom
**Investigator:** Agnes only | **XP:** 4

| Field | Value |
|---|---|
| Type | Asset — Ally |
| Cost | 3r |
| Traits | Ally. Spirit. |
| HP soak | 0 |
| SAN soak | 3 |
| Icons | 1 × `<wil>` |

```
Agnes Crane deck only.
You get +1 <wil> and +1 <agi> while The Pale Child
is in play.
Forced — At the end of the upkeep phase: Heal 2
horror from Agnes Crane.
```
*Flavor: "She does not speak. She does not need to."*

---

### 034 — The Pale Child (3) ★ ✦ Custom
**Investigator:** Agnes only | **XP:** 6 total (2 from Lv 2)

| Field | Value |
|---|---|
| Type | Asset — Ally |
| Cost | 3r |
| Traits | Ally. Spirit. |
| HP soak | 1 |
| SAN soak | 3 |
| Icons | 1 × `<wil>` |

```
Agnes Crane deck only.
You get +2 <wil> and +1 <agi> while The Pale Child
is in play.
Forced — At the end of the upkeep phase: Heal 2
horror from Agnes Crane.
<rea> After Agnes Crane would take horror from an
enemy attack: Exhaust The Pale Child — cancel 1
of that horror.
```
*Flavor: "She stepped in front of it. She always does."*

---

### 035 — The Pale Child (5) ★ ✦ Custom
**Investigator:** Agnes only | **XP:** 10 total (4 from Lv 3)

| Field | Value |
|---|---|
| Type | Asset — Ally |
| Cost | 3r |
| Traits | Ally. Spirit. |
| HP soak | 2 |
| SAN soak | 4 |
| Icons | 1 × `<wil>` |

```
Agnes Crane deck only.
You get +2 <wil> and +2 <agi> while The Pale Child
is in play.
Forced — At the end of the upkeep phase: Heal 2
horror and 1 damage from Agnes Crane. Draw 1 card.
<rea> After Agnes Crane would take horror from an
enemy attack: Exhaust The Pale Child — cancel 1
of that horror.
```
*Flavor: "She has always been here. I just finally learned to see her."*

---

### 036 — The Third Eye (1) ★ ✦ Custom
**Investigator:** Agnes only | **XP:** 2

| Field | Value |
|---|---|
| Type | Asset — Accessory |
| Cost | 1r |
| Traits | Item. Relic. |
| Slot | Accessory |
| Icons | 1 × `<wil>` |

```
Agnes Crane deck only. Unique.
<fre> At the start of your turn: Look at the top 2
cards of the encounter deck instead of 1. Return
them in any order. If either is a Treachery —
discover 1 clue at your location.
```
*Flavor: "The third eye does not blink. It does not look away. Neither do I."*

---

### 037 — Lucky! (2) Reskin
**Base:** Lucky! (2) | **Investigator:** Agnes | **XP:** 2

| Field | Value |
|---|---|
| Type | Event |
| Cost | 1r |
| Traits | Fortune. |
| Icons | 2 × `<wil>` |

```
Fast. Play when you would reveal a chaos token or
when a treachery card is revealed. Cancel the effects
of that chaos token OR cancel that treachery's
revelation effect. In either case, the card or
token is still considered revealed.
```
*Flavor: "The voices told me. Just this once, I listened."*

---

### 038 — Grotesque Statue (4) Reskin
**Base:** Grotesque Statue (4) | **Investigator:** Agnes | **XP:** 4

| Field | Value |
|---|---|
| Type | Asset — Hand |
| Cost | 4r |
| Traits | Item. Relic. |
| Slot | Hand |
| Uses | 4 charges |
| Icons | 1 × `<wil>` |

```
Uses (4 charges).
<fre> When you would reveal a chaos token: Exhaust
Grotesque Statue and spend 1 charge — reveal 2
chaos tokens and choose which one to apply. Cancel
the other token's effects.
```
*Flavor: "It shows me what the bag wants to give me. Then I choose."*

---

### 039 — Sweat Lodge (3) ✦ Custom
**Investigator:** Abel | **XP:** 6

| Field | Value |
|---|---|
| Type | Asset — Hand |
| Cost | 2r |
| Traits | Item. Relic. Blessed. |
| Slot | Hand |
| Uses | 6 charges |
| Icons | 1 × `<wil>` |

```
Uses (6 charges).
<act> Spend 1 charge: Choose an investigator at your
location. That investigator heals 2 horror.
<act> Spend 2 charges: Add 3 bless tokens to the
chaos bag.
```
*Flavor: "The steam carries the prayers upward. The ancestors are listening now."*

---

### 040 — Awaken the Spirits (3) ✦ Reskin
**Base:** Rise to the Occasion (3) | **Investigator:** Abel | **XP:** 6

| Field | Value |
|---|---|
| Type | Skill |
| Traits | Innate. Blessed. |
| Icons | 3 × `<wld>` (conditional) |

```
Commit only to a skill test you are performing,
and only if the difficulty of that test is at least
2 higher than your base skill value.
```
*Flavor: "When everything else has failed — the ancestors have not."*

---

## Neutral Upgrades

---

### 041 — Ancient Cache (0) ✦ Custom
**All investigators** | **XP:** 0

| Field | Value |
|---|---|
| Type | Event |
| Cost | 0r |
| Traits | Supply. |
| Icons | 1 × `<wld>` |

```
Gain 3 resources.
```
*Flavor: "Some things were left behind deliberately. Others were simply forgotten."*

---

### 042 — Ancient Cache (2) ✦ Custom
**All investigators** | **XP:** 4

| Field | Value |
|---|---|
| Type | Event |
| Cost | 0r |
| Traits | Supply. |
| Icons | 2 × `<wld>` |

```
Fast.
Gain 4 resources.
```
*Flavor: "Both are useful. The difference is knowing when."*

---

### 043 — Charisma (3) Official
**All investigators** | **XP:** 6

| Field | Value |
|---|---|
| Type | Asset |
| Cost | 3r |
| Traits | Talent. |
| Slot | None |

```
You have 1 additional ally slot.
```
*Flavor: "Knowing how to ask is half the battle."*

---

### 044 — Relic Hunter (3) Official
**All investigators** | **XP:** 6

| Field | Value |
|---|---|
| Type | Asset |
| Cost | 2r |
| Traits | Talent. |
| Slot | None |

```
You have 1 additional hand slot.
```
*Flavor: "There is always room for one more."*

---

## Complete Card Count

| Class | Cards | Custom | Reskin | Official |
|---|---|---|---|---|
| Guardian | 17 | 9 | 4 | 4 |
| Seeker | 10 | 10 | 0 | 0 |
| Mystic | 5 | 4 | 1 | 0 |
| Survivor | 8 | 6 | 1 | 1 |
| Neutral | 4 | 2 | 0 | 2 |
| **Total** | **44** | **31** | **6** | **7** |

---

## XP Summary — Full Upgrade Path Costs

### Jonathan Ironhide
| Card | XP cost |
|---|---|
| Father Thomas (2) | 4 |
| Father Thomas (4) | +4 |
| Hound of the Deep (2) | 4 |
| Hound of the Deep (4) | +4 |
| Aquinnah (3) | 4 |
| Aquinnah (5) | +4 |
| The Hollow Warden (3) | 6 |
| R'lyeh's Fury (2) | 4 |
| Ward of Protection (2) | 4 |
| **Full path total** | **38 XP** |

### Alistair Greystoke
| Card | XP cost |
|---|---|
| The Relic Harvester (2) | 4 |
| Deduction (2) | 4 |
| My Eyes and Ears (2) | 4 |
| The Unbroken Codex (2) | 4 |
| The Ancient Binding (2) | 4 |
| Centuries of Memory (1) | 2 |
| Intellectual Violence (3) | 6 |
| The Relic Harvester (4) | +4 |
| Centuries of Knowledge (3) | 6 |
| The Ancient Binding (4) | +4 |
| The Immortal's Eye (4) | 8 |
| **Full path total** | **50 XP** |

### Agnes Crane
| Card | XP cost |
|---|---|
| The Night-Gaunt (2) | 4 |
| The Pale Child (2) | 4 |
| Lucky! (2) | 2 |
| The Pale Child (3) | +2 |
| Arcane Athame (3) | 6 |
| The Night-Gaunt (4) | +4 |
| Grotesque Statue (4) | 4 |
| The Pale Child (5) | +4 |
| The Night-Gaunt (5) | +2 |
| **Full path total** | **32 XP** |

### Abel Redcloud
| Card | XP cost |
|---|---|
| The Sacred Spear (3) | 6 |
| Spirit Coyote (2) | 4 |
| Multi-Shot (2) | 4 |
| Spirit Coyote (3) | +2 |
| Fire Walker (2) | 4 |
| Bear Pelt (2) | 4 |
| Rain Dance (2) | 4 |
| Sweat Lodge (3) | 6 |
| Spirit Coyote (5) | +4 |
| Ancient Warrior (4) | 8 |
| **Full path total** | **46 XP** |
