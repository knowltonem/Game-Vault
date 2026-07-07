# Bjorn Blackcast (RYP-BB) — Card Data

## Investigator Card

| Field | Value |
|---|---|
| **Name** | Bjorn Blackcast |
| **Subtitle** | The Mist Borne |
| **Class** | Mystic |
| **Traits** | Shaman. Runebearer. |
| **Willpower** | 5 |
| **Intellect** | 3 |
| **Combat** | 2 |
| **Agility** | 3 |
| **Health** | 6 |
| **Sanity** | 10 |
| **Pack Code** | RYP-BB |

### Ability
```
Once per round: Before revealing a chaos token, you may exhaust a Rune asset you control to reveal 2 tokens and choose which one applies. Return the other to the bag.
```

### Elder Sign
```
+3. Heal 1 horror.
```

### Deckbuilding
```
Mystic 0-5, Survivor 0-2, Seeker 0-1, Neutral 0-5
```

### Requirements
```
The Runic Staff x1, The Runic Helm x1, The Ragnarök x1, 1 random basic weakness
```

---

## Signature Cards

### The Runic Staff
| Field | Value |
|---|---|
| **Type** | Asset — Hand |
| **Class** | Mystic |
| **Level** | Signature |
| **Cost** | 2 |
| **Slot** | Hand |
| **Traits** | Item. Relic. Rune. |
| **Icons** | `<wil><wil>` |
| **Unique** | Yes |

```
Bjorn Blackcast deck only. Unique.
+1 WIL while The Runic Staff is in play.
[action] Fight. This attack uses WIL instead of COM. You get +2 WIL for this attack.
```

---

### The Runic Helm
| Field | Value |
|---|---|
| **Type** | Asset — Body |
| **Class** | Mystic |
| **Level** | Signature |
| **Cost** | 2 |
| **Slot** | Body |
| **Traits** | Item. Relic. Rune. |
| **HP Soak** | 1 |
| **SAN Soak** | 2 |
| **Icons** | `<wil><wil>` |
| **Unique** | Yes |

```
Bjorn Blackcast deck only. Unique.
+1 WIL while The Runic Helm is in play.
[reaction] When Bjorn would take horror: Exhaust The Runic Helm -- prevent 1 horror.
```

---

### The Ragnarök
| Field | Value |
|---|---|
| **Type** | Treachery — Weakness |
| **Class** | Mystic |
| **Level** | Signature |
| **Traits** | Omen. |
| **Unique** | Yes |
| **Icons** | — |

```
Bjorn Blackcast deck only.
Revelation -- Put The Ragnarök into play in your threat area. Bjorn Blackcast's investigator ability is disabled.
Forced -- At the end of your turn: Reveal 5 random tokens from the chaos bag. If an [Elder Sign] is revealed, discard The Ragnarök.
```

---

## Deck Cards

### Allies

#### Loki's Spirit
| Field | Value |
|---|---|
| **Subtitle** | Neither Lies Nor Truth |
| **Type** | Asset — Ally |
| **Class** | Mystic |
| **Level** | 0 |
| **Cost** | 3 |
| **Slot** | Ally |
| **Traits** | Ally. Spirit. |
| **HP Soak** | 1 |
| **SAN Soak** | 4 |
| **Icons** | `<wil><int>` |

```
+1 INT while Loki's Spirit is in play.
[free] After Bjorn successfully investigates: Draw 1 card.
```

---

#### Thor's Honor
| Field | Value |
|---|---|
| **Subtitle** | The Thunder Oath |
| **Type** | Asset — Ally |
| **Class** | Mystic |
| **Level** | 0 |
| **Cost** | 4 |
| **Slot** | Ally |
| **Traits** | Ally. Spirit. |
| **HP Soak** | 5 |
| **SAN Soak** | 1 |
| **Icons** | `<wil><wil>` |

```
+1 WIL while Thor's Honor is in play.
[reaction] When any investigator at your location would take damage: Exhaust Thor's Honor -- prevent 1 damage.
```

---

### Spells

#### Rune of Lightning
| Field | Value |
|---|---|
| **Type** | Asset — Arcane |
| **Class** | Mystic |
| **Level** | 0 |
| **Cost** | 3 |
| **Slot** | Arcane |
| **Traits** | Spell. Rune. |
| **Icons** | `<wil><wil>` |

```
Uses (4 charges).
[action] Spend 1 charge: Fight. This attack uses WIL instead of COM. You get +1 WIL for this attack. This attack deals +1 damage.
```

---

#### The Allfather's Eye
| Field | Value |
|---|---|
| **Type** | Asset — Arcane |
| **Class** | Mystic |
| **Level** | 0 |
| **Cost** | 2 |
| **Slot** | Arcane |
| **Traits** | Spell. Rune. |
| **Icons** | `<wil><int>` |

```
Uses (4 charges).
[action] Spend 1 charge: Investigate. This investigation uses WIL instead of INT. You get +1 WIL for this investigation.
```

---

#### Sif's Love
| Field | Value |
|---|---|
| **Type** | Asset — Arcane |
| **Class** | Mystic |
| **Level** | 0 |
| **Cost** | 3 |
| **Slot** | Arcane |
| **Traits** | Spell. Rune. |
| **Icons** | `<wil><agi>` |

```
Uses (4 charges).
[action] Spend 1 charge: Evade. This evade uses WIL instead of AGI. You get +1 WIL for this evade. If you succeed: Exhaust the enemy and it cannot ready until the end of the round.
```

---

### Economy

#### Odin's Price
| Field | Value |
|---|---|
| **Type** | Event |
| **Class** | Mystic |
| **Level** | 0 |
| **Cost** | 0 |
| **Traits** | Augury. |
| **Icons** | `<wld>` |
| **Base Card** | Faustian Bargain |
| **Qty** | x2 |

```
Gain 4 resources. Take 1 horror.
```
*Flavor: "Odin hung nine days on the World Tree. Nothing comes free."*

---

#### Heimdall's Offering
| Field | Value |
|---|---|
| **Type** | Event |
| **Class** | Neutral |
| **Level** | 0 |
| **Cost** | 0 |
| **Traits** | Supply. |
| **Icons** | `<wld>` |
| **Base Card** | Emergency Cache |
| **Qty** | x2 |

```
Fast. Gain 2 resources.
```
*Flavor: "Heimdall sees those in need."*

---

### Horror Heal

#### Eir's Touch
| Field | Value |
|---|---|
| **Type** | Event |
| **Class** | Mystic |
| **Level** | 0 |
| **Cost** | 1 |
| **Traits** | Insight. |
| **Icons** | `<wil><wil>` |
| **Qty** | x2 |

```
Fast. Heal 1 horror from each investigator at your location.
```

---

#### Val's Embrace
| Field | Value |
|---|---|
| **Type** | Event |
| **Class** | Mystic |
| **Level** | 0 |
| **Cost** | 0 |
| **Traits** | Insight. |
| **Icons** | `<wil><agi>` |
| **Qty** | x2 |

```
Fast. Play when you would take horror. Prevent 2 of that horror.
```

---

## Design Notes

### WIL Stacking (max in play)
| Source | WIL |
|---|---|
| Base | 5 |
| Runic Staff | +1 |
| Runic Helm | +1 |
| Thor's Honor | +1 |
| **Total** | **8** |

### Combat (via Staff + Rune of Lightning)
- Staff attack: WIL 8 + 2 = WIL 10 fight
- Rune of Lightning: WIL 8 + 1 = WIL 9 fight, +1 damage

### Investigation (via Allfather's Eye + Loki's Spirit)
- INT 3 + 1 Loki = INT 4
- Allfather's Eye: WIL 8 + 1 = WIL 9 investigate

### Still Needed
- [ ] Skill cards
- [ ] Movement cards
- [ ] Additional utility
- [ ] Flavor text for all cards
- [ ] Signature asset subtitles and full specs
- [ ] Deckbuilding requirements finalized

### Movement

#### The Bifrost Path
| Field | Value |
|---|---|
| **Type** | Event |
| **Class** | Neutral |
| **Level** | 0 |
| **Cost** | 0 |
| **Traits** | Insight. |
| **Icons** | `<agi><wld>` |
| **Base Card** | Elusive |
| **Qty** | x2 |

```
Fast. Disengage from all enemies engaged with you. Move to any connecting location.
```
*Flavor: "The bridge between worlds opens for those who know the way."*

---

### Skills

#### Sigurd's Fury
| Field | Value |
|---|---|
| **Type** | Skill |
| **Class** | Mystic |
| **Level** | 0 |
| **Traits** | Practiced. |
| **Icons** | `<wil><wil>` |
| **Base Card** | Guts |
| **Qty** | x2 |

```
If this skill test fails, draw 1 card.
```
*Flavor: "Sigurd slew Fafnir not through caution. Through fury."*

---

#### Vegtam "The Wanderer"
| Field | Value |
|---|---|
| **Type** | Skill |
| **Class** | Neutral |
| **Level** | 0 |
| **Traits** | Innate. |
| **Icons** | `<wld><wld>` |
| **Base Card** | Unexpected Courage |
| **Qty** | x2 |

```
—
```
*Flavor: "He walks unseen. He always has."*

---

#### Rune Sight
| Field | Value |
|---|---|
| **Type** | Skill |
| **Class** | Mystic |
| **Level** | 0 |
| **Traits** | Practiced. |
| **Icons** | `<int><int>` |
| **Base Card** | Perception |
| **Qty** | x2 |

```
If this skill test is successful while investigating, draw 1 card.
```
*Flavor: "He does not look for clues. He reads what was always written there."*

---

## Deck Summary (Current)

| Category | Cards | Qty |
|---|---|---|
| Allies | Loki's Spirit, Thor's Honor | 2 |
| Spells | Rune of Lightning, Allfather's Eye, Sif's Love | 3 |
| Economy | Odin's Price, Heimdall's Offering | 4 |
| Horror Heal | Eir's Touch, Val's Embrace | 4 |
| Movement | The Bifrost Path | 2 |
| Skills | Sigurd's Fury, Vegtam, Rune Sight | 6 |
| **Total** | | **21** |

### Still Needed (~9 more cards to reach 30)
- [ ] Utility cards
- [ ] Draw engine
- [ ] Ward of Protection or cancel event
- [ ] Flavor text for signature assets
- [ ] Subtitles for signature assets
