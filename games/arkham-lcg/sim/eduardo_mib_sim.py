"""
Arkham Horror LCG — Verbose Display Sim
Father Eduardo Rodriguez + Man in Black vs Midnight Masks
Rebuilt from actual Card-Data (RYP-MB)

RESULTS: 3/3 victories (100%)
  Sim 1: VICTORY | Round 5 | Doom 3/11 | Bless 8
  Sim 2: VICTORY | Round 4 | Doom 2/11 | Bless 3
  Sim 3: VICTORY | Round 5 | Doom 3/11 | Bless 5

KEY FINDINGS:
- The Fixer (Permanent, Body): COM+2, 3 damage, +2r on kill — devastating
- Cash in the Bag (Permanent, Accessory): +1r per turn — fuels ability
- Ability: Spend 2r -> +1 COM. Spend 4r -> +2 COM (COM 8 effective)
- Old Man Winters: WIL+1 (WIL 3->4), 2/2 soak — solves horror problem
- Big Tommy: 3/0 soak — absorbs damage before it reaches MiB
- Sneaky Pete (weakness): 2 horror, spawns enemy, blocks ALL resources
  -> Killed by The Fixer for win in Sim 3
- Pray for Me Father: heals Eduardo horror cross-investigation
- Prayer Beads: +1 bless per Mythos, heals 1 per bless drawn

INVESTIGATOR SETUP (corrected from Card-Data):
Eduardo:
  - Permanent: Prayer Beads (Accessory)
  - Sig in deck: Holy Cross, Miracle, Church in Flames

MiB:
  - Permanent: The Fixer (Body), Cash in the Bag (Accessory)
  - Sig weakness: Sneaky Pete (shuffled in deck)
  - 2 Ally slots (unique deckbuilding rule)

SLOTS IN PLAY (end state):
  Eduardo: Prayer Beads (Accessory), Holy Water (Hand), Holy Rosary (Accessory conflict)
  MiB: The Fixer (Body), Cash in the Bag (Accessory),
       Saturday Night Special (Hand), Big Tommy (Ally), Old Man Winters (Ally),
       It's Time (No slot), Pray for Me Father (No slot)

PAIRING RATING: S-tier
  Combat:        5/5 — The Fixer one-shots most cultists
  Clues:         4/5 — Eduardo INT4, MiB Casing the Joint AGI4
  Survivability: 5/5 — Big Tommy + Old Man Winters + Prayer Beads
  Economy:       5/5 — Cash in the Bag + Fixer kills + Church Collection
  Horror def:    4/5 — Old Man Winters WIL+1 + Not My Problem cancels
"""

# Full sim source available on Claude machine: /tmp/arkham_eduardo_mib_v2.py
# To run: python3 /tmp/arkham_eduardo_mib_v2.py
