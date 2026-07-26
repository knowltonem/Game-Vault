# Arkham Horror LCG — Game Simulator Plan

## Objective
Build a Python CLI-based game simulator for Arkham Horror LCG Chapter 2 Core Set (2026) that:
- Simulates single scenarios and full campaigns
- Tests all 9 custom investigators against official content
- Provides deck strength/weakness analysis with recommendations
- Imports official card data from ArkhamDB API + manual custom investigator data
- Handles chaos bag draws, encounter deck draws, card draws, skill tests, combat, and scenario progression

---

## Architecture Overview

```
arkham-simulator/
├── README.md                    ← Project documentation
├── requirements.txt             ← Python dependencies
├── setup.py                     ← Package setup
├── config/
│   ├── settings.yaml            ← Simulation settings (difficulty, player count, etc.)
│   └── chaos_bags.yaml          ← Chaos bag token compositions
├── data/
│   ├── investigators/           ← Custom investigator JSON files
│   │   ├── eleanor_heart.json
│   │   ├── agnes_crane.json
│   │   ├── bjorn_blackcast.json
│   │   ├── ephraim_archer.json
│   │   ├── jonathan_ironhide.json
│   │   ├── alistair_greystoke.json
│   │   ├── nora_warwick.json
│   │   ├── abel_redcloud.json
│   │   └── the_man_in_black.json
│   ├── scenarios/               ← Scenario data (encounter decks, agendas, acts)
│   │   ├── spreading_flames.json
│   │   ├── smoke_and_mirrors.json
│   │   └── queen_of_ash.json
│   ├── encounters/              ← Encounter card definitions
│   │   ├── arcane_lock.json
│   │   ├── ashen_pilgrims.json
│   │   ├── bad_weather.json
│   │   ├── fire.json
│   │   └── ... (16 sets)
│   ├── cards/                   ← Official card data (from ArkhamDB)
│   │   ├── player/              ← Player cards by class
│   │   └── encounter/           ← Encounter cards
│   └── locations/               ← Location data per scenario
├── engine/
│   ├── __init__.py
│   ├── game.py                  ← Main game loop and state management
│   ├── investigator.py          ← Investigator class (stats, deck, hand, play area)
│   ├── card.py                  ← Card class (base for all card types)
│   ├── skill_test.py            ← Skill test resolution engine
│   ├── chaos_bag.py             ← Chaos bag token draw and resolution
│   ├── encounter.py             ← Encounter deck draw and resolution
│   ├── combat.py                ← Combat/evade mechanics
│   ├── phases.py                ← Phase implementations (Mythos, Investigation, Enemy, Upkeep)
│   ├── agenda.py                ← Agenda/Act deck management
│   ├── location.py              ← Location management and clue tracking
│   ├── campaign.py              ← Campaign mode (trauma, XP, progression)
│   ├── effects.py               ← Card effect resolution system
│   └── multiplayer.py           ← Multiplayer coordination (2-4 investigators)
├── data_import/
│   ├── __init__.py
│   ├── arkhamdb.py              ← ArkhamDB API client
│   ├── json_builder.py          ← Build JSON from API data
│   └── custom_importer.py       ← Import custom investigators from vault
├── analysis/
│   ├── __init__.py
│   ├── deck_analyzer.py         ← Deck strength/weakness analysis
│   ├── probability.py           ← Probability calculations for skill tests
│   ├── simulator.py             ← Run multiple simulations for statistics
│   └── recommendations.py       ← Generate deck improvement recommendations
├── cli/
│   ├── __init__.py
│   ├── main.py                  ← CLI entry point
│   ├── commands.py              ← CLI command implementations
│   ├── display.py               ← Terminal display formatting
│   └── game_view.py             ← Game state visualization
├── logs/                        ← Game simulation logs
│   └── .gitkeep
└── tests/
    ├── test_skill_test.py
    ├── test_chaos_bag.py
    ├── test_combat.py
    └── test_phases.py
```

---

## Tech Stack

| Component | Technology | Purpose |
|---|---|---|
| Language | Python 3.10+ | Core language |
| CLI Framework | Click | Command structure and argument parsing |
| Display | Rich | Terminal formatting, tables, colors, panels |
| Data | JSON | Card and scenario storage |
| HTTP | Requests | ArkhamDB API calls |
| YAML | PyYAML | Configuration files |
| Testing | Pytest | Unit and integration tests |
| Random | Random (stdlib) | Token draws, card shuffles |

### Dependencies
```
click>=8.0
rich>=13.0
requests>=2.28
pyyaml>=6.0
pytest>=7.0
```

---

## Phase 1: Data Layer (Week 1)

### 1.1 Chaos Bag Configuration
Create `config/chaos_bags.yaml` with token compositions:

```yaml
standard:
  tokens:
    - {symbol: "+1", count: 1, modifier: 1}
    - {symbol: "0", count: 2, modifier: 0}
    - {symbol: "-1", count: 3, modifier: -1}
    - {symbol: "-2", count: 2, modifier: -2}
    - {symbol: "-3", count: 1, modifier: -3}
    - {symbol: "-4", count: 1, modifier: -4}
    - {symbol: "skull", count: 2, modifier: "scenario"}
    - {symbol: "cultist", count: 1, modifier: "scenario"}
    - {symbol: "tablet", count: 1, modifier: "scenario"}
    - {symbol: "elder_thing", count: 1, modifier: "scenario"}
    - {symbol: "elder_sign", count: 1, modifier: "elder_sign"}
    - {symbol: "auto_fail", count: 1, modifier: "auto_fail"}

easy:
  tokens:
    - {symbol: "+1", count: 2, modifier: 1}
    - {symbol: "0", count: 3, modifier: 0}
    - {symbol: "-1", count: 3, modifier: -1}
    - {symbol: "-2", count: 2, modifier: -2}
    - {symbol: "-3", count: 0, modifier: -3}
    - {symbol: "-4", count: 0, modifier: -4}
    - {symbol: "skull", count: 2, modifier: "scenario"}
    - {symbol: "cultist", count: 1, modifier: "scenario"}
    - {symbol: "tablet", count: 1, modifier: "scenario"}
    - {symbol: "elder_thing", count: 1, modifier: "scenario"}
    - {symbol: "elder_sign", count: 1, modifier: "elder_sign"}
    - {symbol: "auto_fail", count: 1, modifier: "auto_fail"}
```

### 1.2 Custom Investigator JSON Schema
Each investigator file follows this schema:

```json
{
  "name": "Eleanor Heart",
  "subtitle": "The Undying",
  "class": "Mystic",
  "traits": ["Medic", "Scholar"],
  "stats": {
    "willpower": 4,
    "intellect": 4,
    "combat": 1,
    "agility": 4
  },
  "health": 10,
  "sanity": 7,
  "elder_sign": "+2. You may heal 2 damage or horror from Eleanor Heart. All investigators at your location draw 1 card.",
  "ability": {
    "text": "After one of your card effects heals damage or horror from an investigator: Heal 1 additional damage or horror for each 3 damage currently on Eleanor Heart.",
    "trigger": "after_heal",
    "scaling": [
      {"damage_on_self": "0-2", "bonus": 0},
      {"damage_on_self": "3-5", "bonus": 1},
      {"damage_on_self": "6-8", "bonus": 2},
      {"damage_on_self": "9", "bonus": 3}
    ]
  },
  "deckbuilding": {
    "mystic": {"min": 0, "max": 3},
    "neutral": {"min": 0, "max": 5},
    "seeker": {"min": 0, "max": 1, "limit": 15},
    "guardian": {"min": 0, "max": 1, "limit": 15},
    "heal_cards": {"min": 0, "max": 5},
    "restricted": ["weapon_1_5"]
  },
  "signatures": ["medical_bag", "innsmouth_codex", "fog_of_innsmouth"],
  "deck_size": 30,
  "pack_code": "RYP-EH"
}
```

### 1.3 ArkhamDB API Import
Create `data_import/arkhamdb.py`:

```python
class ArkhamDBClient:
    BASE_URL = "https://arkhamdb.com/api"
    
    def get_card(self, card_code: str) -> dict:
        """Fetch a single card by code."""
        
    def get_cards_by_pack(self, pack_code: str) -> list:
        """Fetch all cards in a pack."""
    
    def get_investigators(self) -> list:
        """Fetch all investigator cards."""
    
    def get_encounter_sets(self) -> dict:
        """Fetch encounter set compositions."""
    
    def build_local_database(self):
        """Download and cache all official card data locally."""
```

### 1.4 Custom Investigator Import
Create `data_import/custom_importer.py`:

```python
class CustomImporter:
    VAULT_PATH = r"C:\Users\edwar\Documents\games\board-game-vault\games\arkham-lcg\investigators\custom-1"
    
    def import_investigator(self, name: str) -> dict:
        """Read custom investigator data from vault markdown files."""
        
    def import_all(self) -> list:
        """Import all 9 custom investigators."""
```

---

## Phase 2: Game Engine (Week 2)

### 2.1 Card Class Hierarchy
```python
class Card:
    code: str
    name: str
    type: str  # asset, event, skill, treachery, enemy, act, agenda, location
    class: str
    level: int
    cost: int
    icons: dict  # {willpower: 1, combat: 0, ...}
    text: str
    flavor: str
    
class PlayerCard(Card):
    slot: str
    uses: int
    health: int
    sanity: int
    
class EnemyCard(Card):
    fight: int
    evade: int
    damage: int
    horror: int
    health: int
    prey: str
    keywords: list  # hunter, retaliate, alert, elite
    
class LocationCard(Card):
    shroud: int
    clues: int
    connections: list
    
class AgendaCard(Card):
    doom_threshold: int
    text: str
    
class ActCard(Card):
    clue_threshold: int
    text: str
```

### 2.2 Chaos Bag Engine
```python
class ChaosBag:
    def __init__(self, difficulty: str, scenario: str):
        self.tokens = self._load_tokens(difficulty)
        self.bag = []
        self.reset()
    
    def reset(self):
        """Reset bag to full token pool."""
        self.bag = self.tokens.copy()
        random.shuffle(self.bag)
    
    def draw(self) -> Token:
        """Draw one token from the bag. Reshuffle if empty."""
        
    def apply_modifier(self, token: Token, scenario_effects: dict) -> int:
        """Apply token modifier and scenario-specific effects."""
```

### 2.3 Skill Test Engine
```python
class SkillTest:
    def __init__(self, investigator, skill, difficulty, cards_committed=None):
        self.investigator = investigator
        self.skill = skill
        self.difficulty = difficulty
        self.cards_committed = cards_committed or []
        
    def calculate_base(self) -> int:
        """Sum skill value + committed card icons."""
        
    def resolve(self, chaos_bag) -> TestResult:
        """Draw token, apply modifiers, determine success/failure."""
        base = self.calculate_base()
        token = chaos_bag.draw()
        modifier = chaos_bag.apply_modifier(token, self.scenario_effects)
        final_value = base + modifier
        success = final_value >= self.difficulty
        return TestResult(success, base, token, modifier, final_value)
```

### 2.4 Combat Engine
```python
class CombatResolver:
    def fight(self, investigator, enemy, weapon=None) -> CombatResult:
        """Resolve a fight action."""
        
    def evade(self, investigator, enemy) -> EvadeResult:
        """Resolve an evade action."""
        
    def apply_damage(self, target, amount, source=None):
        """Apply damage to investigator or enemy."""
        
    def apply_horror(self, target, amount, source=None):
        """Apply horror to investigator or asset."""
        
    def enemy_attack(self, enemy, investigator):
        """Resolve enemy attack during Enemy Phase."""
```

### 2.5 Phase Implementations
```python
class MythosPhase:
    def execute(self, game_state):
        """Each investigator draws 1 encounter card. Place 1 doom on agenda."""
        
class InvestigationPhase:
    def execute(self, game_state):
        """Investigators take turns, 3 actions each."""
        
class EnemyPhase:
    def execute(self, game_state):
        """Ready enemies move (Hunter). Engaged enemies attack."""
        
class UpkeepPhase:
    def execute(self, game_state):
        """Ready all cards. Draw 1 card, gain 1 resource. Gain 3 actions."""
```

### 2.6 Game State
```python
class GameState:
    investigators: list
    encounter_deck: list
    encounter_discard: list
    agenda_deck: list
    current_agenda: AgendaCard
    act_deck: list
    current_act: ActCard
    locations: list
    chaos_bag: ChaosBag
    round_number: int
    phase: str
    doom_count: int
    
    def is_over(self) -> bool:
        """Check if scenario is won or lost."""
        
    def advance_agenda(self):
        """Check if agenda should advance (doom >= threshold)."""
        
    def advance_act(self, clues_spent: int):
        """Check if act should advance (clues >= threshold)."""
```

---

## Phase 3: Scenario Data (Week 2-3)

### 3.1 Scenario JSON Schema
```json
{
  "name": "Spreading Flames",
  "number": 1,
  "campaign": "Brethren of Ash",
  "setup": {
    "investigator_count": "1-4",
    "initial_clues": "per investigator",
    "agenda_count": 2,
    "act_count": 2
  },
  "encounter_sets": ["arcane_lock", "fire", "cultists", "bad_weather"],
  "agenda_deck": [
    {
      "name": "The Brethren's Plan",
      "doom_threshold": 8,
      "text": "The Brethren of Ash have begun their ritual...",
      "flavor": "..."
    }
  ],
  "act_deck": [
    {
      "name": "Investigate the Campus",
      "clue_threshold": 4,
      "text": "You must investigate Miskatonic University..."
    }
  ],
  "locations": [
    {
      "name": "Orne Library",
      "shroud": 4,
      "clues": 2,
      "connections": ["Quad"],
      "text": "Initial location."
    }
  ],
  "enemy_pool": ["servant_of_flame", "cultist_1", "cultist_2"],
  "resolution": {
    "R1": "The Brethren escape. Gain 1 trauma.",
    "R2": "You defeat the Servant. Gain 2 XP."
  }
}
```

### 3.2 Encounter Set Data
Each encounter set needs:
- Card list with quantities
- Card text and effects
- Target resolution (token symbol effects)

---

## Phase 4: Analysis Engine (Week 3)

### 4.1 Deck Analyzer
```python
class DeckAnalyzer:
    def analyze(self, investigator) -> DeckReport:
        """Full deck analysis."""
        
    def _count_icons(self, deck) -> dict:
        """Count skill icons by type."""
        
    def _analyze_curve(self, deck) -> CostCurve:
        """Analyze card cost distribution."""
        
    def _analyze_combat(self, deck) -> CombatAnalysis:
        """Analyze damage output, weapon count, fight cards."""
        
    def _analyze_clues(self, deck) -> ClueAnalysis:
        """Analyze clue generation, investigate actions."""
        
    def _analyze_survivability(self, deck) -> SurvivabilityAnalysis:
        """Analyze health/sanity soak, healing, damage prevention."""
        
    def _analyze_card_advantage(self, deck) -> CardAdvantageAnalysis:
        """Analyze card draw, resource generation."""
```

### 4.2 Probability Calculator
```python
class ProbabilityCalculator:
    def skill_test_chance(self, skill_value, difficulty, chaos_bag, 
                          committed_icons=0) -> float:
        """Calculate probability of passing a skill test."""
        
    def combat_chance(self, combat, enemy_fight, weapon_bonus=0, 
                      chaos_bag=None) -> float:
        """Calculate chance of hitting in combat."""
        
    def damage_outcome(self, combat, enemy_fight, weapon_damage, 
                       attacks) -> ExpectedDamage:
        """Calculate expected damage over N attacks."""
        
    def chaos_bag_distribution(self, skill_value, difficulty, 
                                chaos_bag) -> dict:
        """Full distribution of token outcomes."""
```

### 4.3 Monte Carlo Simulator
```python
class MonteCarloSimulator:
    def __init__(self, scenario, investigators, difficulty, num_simulations=1000):
        self.scenario = scenario
        self.investigators = investigators
        self.difficulty = difficulty
        self.num_simulations = num_simulations
        
    def run(self) -> SimulationReport:
        """Run all simulations and compile results."""
        wins = 0
        losses = 0
        avg_xp = 0
        avg_rounds = 0
        
        for i in range(self.num_simulations):
            result = self._run_single_game()
            if result.won:
                wins += 1
            else:
                losses += 1
                
        return SimulationReport(
            win_rate=wins / self.num_simulations,
            avg_xp=avg_xp / self.num_simulations,
            avg_rounds=avg_rounds / self.num_simulations
        )
    
    def _run_single_game(self) -> GameResult:
        """Simulate one complete game."""
```

### 4.4 Recommendations Engine
```python
class RecommendationEngine:
    def generate(self, deck_report, simulation_report) -> list:
        """Generate actionable recommendations."""
        
    def _recommend_additions(self, deck, weaknesses) -> list:
        """Suggest cards to add."""
        
    def _recommend_removals(self, deck, weaknesses) -> list:
        """Suggest cards to remove."""
        
    def _recommend_upgrades(self, deck, xp) -> list:
        """Suggest upgrade priorities based on XP budget."""
```

---

## Phase 5: CLI Interface (Week 3-4)

### 5.1 Command Structure
```
arkham-sim/
├── simulate          Run a single game simulation
│   ├── --investigator, -i    Choose investigator(s), comma-separated for multiplayer
│   ├── --scenario, -s        Choose scenario (1-3)
│   ├── --difficulty, -d      Difficulty (easy/standard)
│   ├── --players, -p         Player count (1-4, defaults to investigator count)
│   ├── --verbose, -v         Show detailed card draws
│   └── --log, -l             Save game log to logs/ directory
├── analyze           Analyze a deck
│   ├── --investigator, -i    Choose investigator
│   └── --report, -r          Report type (full/quick/probability)
├── campaign          Run full campaign simulation
│   ├── --investigator, -i    Choose investigator(s)
│   ├── --difficulty, -d      Difficulty
│   └── --iterations, -n      Number of campaign runs
├── compare           Compare investigators
│   ├── --list, -l            Investigators to compare
│   ├── --scenario, -s        Scenario to test
│   └── --iterations, -n      Simulations per investigator
├── import            Import card data
│   ├── --arkhamdb            Import from ArkhamDB API
│   ├── --custom              Import custom investigators
│   └── --all                 Import everything
└── deck              Deck builder
    ├── --new, -n             Create new deck for investigator
    ├── --load, -l            Load existing deck
    ├── --add, -a             Add card to deck
    ├── --remove, -r          Remove card from deck
    ├── --validate            Validate deck legality
    ├── --stats               Show deck statistics
    └── --export              Export deck to JSON
```

### 5.2 Display Formatting
Use Rich library for:
- Color-coded skill test results (green = success, red = failure)
- Token draw animation
- Card display panels
- Game state tables
- Probability distribution charts
- Campaign progress tracker

---

## Phase 6: Testing & Validation (Week 4)

### 6.1 Unit Tests
- Chaos bag draws match expected distributions
- Skill test resolution follows rules
- Combat damage calculation is correct
- Agenda/Act advancement triggers properly
- Phase transitions work correctly

### 6.2 Integration Tests
- Full scenario simulation completes without errors
- Campaign progression tracks trauma and XP correctly
- All investigator abilities trigger at correct times
- Card interactions resolve in correct order

### 6.3 Balance Testing
- Each custom investigator can survive at least 50% of Standard games
- No single investigator dominates all scenarios
- Each investigator has clear strengths and weaknesses
- Recommendations are actionable and improve win rates

---

## Data Requirements

### Official Cards Needed (from ArkhamDB)
1. All player cards from Chapter 2 Core Set (357 cards)
2. All investigator cards (5 core + 5 investigator decks)
3. All encounter cards from Brethren of Ash campaign
4. All scenario reference cards (token effects)

### Custom Investigator Data (from vault)
1. All 9 custom investigator stats and abilities
2. All signature and deck cards (30-34 per investigator)
3. Card text, icons, costs, slots, and types

---

## Implementation Order

| Step | Task | Est. Time |
|---|---|---|
| 1 | Set up project structure and dependencies | 1 hour |
| 2 | Create chaos bag configuration | 1 hour |
| 3 | Build ArkhamDB API client and import data | 2 hours |
| 4 | Create custom investigator JSON files (9 files) | 3 hours |
| 5 | Build card class hierarchy | 2 hours |
| 6 | Build chaos bag engine | 1 hour |
| 7 | Build skill test engine | 2 hours |
| 8 | Build combat engine | 2 hours |
| 9 | Build phase implementations | 3 hours |
| 10 | Build game state and game loop | 3 hours |
| 11 | Create scenario data (3 scenarios) | 3 hours |
| 12 | Build encounter deck system | 2 hours |
| 13 | Build CLI interface | 2 hours |
| 14 | Build analysis engine | 3 hours |
| 15 | Build Monte Carlo simulator | 2 hours |
| 16 | Build recommendations engine | 2 hours |
| 17 | Testing and validation | 3 hours |
| 18 | Documentation and README | 1 hour |
| **Total** | | **~38 hours** |

---

## Success Criteria

1. **Single Game Simulation**: Run a complete game of Spreading Flames with any custom investigator, showing all card draws, skill tests, and results
2. **Multiplayer Simulation**: Run a 2-player game with coordinated actions, shared clue pool, and multiple encounter draws per round
3. **Campaign Mode**: Run all 3 scenarios with trauma/XP progression across investigators
4. **Monte Carlo**: Run 1000 simulations and report win rates per investigator and scenario
5. **Deck Analysis**: Full breakdown of deck strengths, weaknesses, and recommendations
6. **Probability Calculator**: Exact odds for any skill test given chaos bag composition
7. **All 9 Investigators**: Each one playable and balanced against Chapter 2 content
8. **Full Card Text**: All card abilities implemented and resolving correctly
9. **Game Logs**: Detailed logs saved for every simulation run
10. **Deck Builder**: Create, modify, validate, and export decks via CLI

---

## Standing Rules — NEVER VIOLATE

### Rule 1: Always Verify Investigator Data
**Before implementing any investigator in the simulator, always re-read their card data file from the vault.** Card data may have been updated since last read. Never assume previous data is still current.

| Investigator | Card Data File |
|---|---|
| Abel Redcloud | `investigators/custom-1/Abel Redcloud/Abel-Redcloud-Card-Data.md` |
| Nora Warwick | `investigators/custom-1/Nora Warwick/RYP-NW-Master-Catalogue.md` |
| Eleanor Heart | `investigators/custom-1/Eleanor Heart/Eleanor-Heart-Card-Data.md` |
| Agnes Crane | `investigators/custom-1/Agnes Crane/Agnes-Crane-Card-Data.md` |
| Bjorn Blackcast | `investigators/custom-1/Bjorn Blackcast/` |
| Ephraim Archer | `investigators/custom-1/Ephraim Archer/` |
| Jonathan Ironhide | `investigators/custom-1/Jonathan Ironhide/` |
| Alistair Greystoke | `investigators/custom-1/Alistair Greystoke/` |
| The Man in Black | `investigators/custom-1/The Man in Black/` |

**Process:**
1. Read the data.md file for the investigator
2. Check for any card text changes, stat changes, or new cards
3. Update the JSON data files in `simulator/data/investigators/` if needed
4. Only then proceed with implementation

---

## Open Questions

1. ~~Should the simulator support multiplayer (2-4 investigators) from the start, or single investigator first?~~ → **Multiplayer 1-4, primary use is 2-player**
2. ~~How detailed should card effect resolution be?~~ → **Full card text parsing**
3. ~~Should we store game logs for post-game analysis?~~ → **Yes, save logs**
4. ~~Do you want a deck builder CLI as part of this, or separate tool?~~ → **Include deck builder**

---

## Final Decisions

| Decision | Value |
|---|---|
| Player count | 1-4 investigators, primary use is 2-player |
| Card effects | Full text parsing — implement all card abilities |
| Game logs | Save detailed logs to `logs/` directory for post-game analysis |
| Deck builder | Included as CLI command `arkham-sim deck` |
| Tech stack | Python CLI with Click + Rich |
| Card data source | ArkhamDB API + manual custom investigator data |

---

## Implementation Plan — Phase 1: Abel Redcloud & Nora Warwick

### Scope
Build the core simulator with 2 investigators, 1 scenario (Spreading Flames), and full game loop. This establishes the foundation for adding all 9 investigators and 3 scenarios later.

### Step 1: Project Setup (1 hour)
```
arkham-simulator/
├── README.md
├── requirements.txt
├── setup.py
├── run.py                    ← Entry point: python run.py simulate ...
├── config/
│   ├── chaos_bags.yaml       ← Standard/Easy token pools
│   └── settings.yaml         ← Default simulation settings
├── data/
│   ├── investigators/
│   │   ├── abel_redcloud.json
│   │   └── nora_warwick.json
│   ├── scenarios/
│   │   └── spreading_flames.json
│   ├── encounters/
│   │   ├── fire.json
│   │   ├── ashen_pilgrims.json
│   │   ├── bystanders.json
│   │   ├── cosmic_evils.json
│   │   └── miskatonic_university.json
│   └── cards/
│       └── (from ArkhamDB import)
├── engine/
│   ├── __init__.py
│   ├── models.py             ← Card, Investigator, Enemy, Location dataclasses
│   ├── chaos_bag.py          ← Token pool, draw, resolve
│   ├── skill_test.py         ← Test resolution
│   ├── combat.py             ← Fight/evade/damage
│   ├── phases.py             ← 4 phases
│   ├── game.py               ← Game state + main loop
│   ├── ai_player.py          ← AI decision-making for simulation
│   └── effects.py            ← Card effect resolver
├── cli/
│   ├── __init__.py
│   ├── main.py               ← Click commands
│   └── display.py            ← Rich terminal output
├── logs/
│   └── .gitkeep
└── tests/
    ├── test_chaos_bag.py
    └── test_skill_test.py
```

### Step 2: Data Layer — Investigator JSON Schemas

**Abel Redcloud JSON** (`data/investigators/abel_redcloud.json`):
```json
{
  "id": "abel_redcloud",
  "name": "Abel Redcloud",
  "subtitle": "The Last Keeper",
  "class": "Guardian",
  "traits": ["Warrior", "Mystic", "Tribal"],
  "stats": {"willpower": 4, "intellect": 2, "combat": 4, "agility": 3},
  "health": 8,
  "sanity": 7,
  "deck_size": 30,
  "deckbuilding": {
    "guardian": {"min_level": 0, "max_level": 5},
    "mystic": {"min_level": 0, "max_level": 2},
    "survivor": {"min_level": 0, "max_level": 2},
    "neutral": {"min_level": 0, "max_level": 5}
  },
  "ability": {
    "trigger": "start_of_mythos",
    "text": "Add 1 bless token to the chaos bag. Heal 1 damage.",
    "effects": [
      {"type": "add_bless_token", "count": 1},
      {"type": "heal_damage", "target": "self", "amount": 1}
    ]
  },
  "elder_sign": {
    "modifier": 1,
    "text": "You may play Sacred Bond.",
    "effects": [
      {"type": "conditional", "condition": "player_chose", "option": "play_sacred_bond",
       "then": {"type": "play_set_aside", "card": "sacred_bond"}}
    ]
  },
  "auto_fail_effect": {
    "text": "You may play Sacred Wind.",
    "effects": [
      {"type": "conditional", "condition": "player_chose", "option": "play_sacred_wind",
       "then": {"type": "play_set_aside", "card": "sacred_wind"}}
    ]
  },
  "cultist_effect": {
    "text": "You may play Sacred Strength.",
    "effects": [
      {"type": "conditional", "condition": "player_chose", "option": "play_sacred_strength",
       "then": {"type": "play_set_aside", "card": "sacred_strength"}}
    ]
  },
  "signatures": [
    {"id": "sacred_spear", "required": true},
    {"id": "tribal_oath", "required": true}
  ],
  "set_aside": ["sacred_bond", "sacred_wind", "sacred_strength"],
  "deck": [
    {"id": "teeth_of_deep_ones", "qty": 1},
    {"id": "sacred_fire", "qty": 1},
    {"id": "ritual_knife", "qty": 1},
    {"id": "spirit_coyote", "qty": 2},
    {"id": "sweat_lodge", "qty": 2},
    {"id": "bear_pelt", "qty": 1},
    {"id": "noble_sacrifice", "qty": 2},
    {"id": "tracker", "qty": 2},
    {"id": "on_the_hunt", "qty": 1},
    {"id": "fire_walker", "qty": 1},
    {"id": "back_to_dark", "qty": 2},
    {"id": "rain_dance", "qty": 2},
    {"id": "elder_strength", "qty": 2},
    {"id": "chieftain_wisdom", "qty": 2},
    {"id": "vicious_blow", "qty": 2},
    {"id": "awaken_spirits", "qty": 2},
    {"id": "unexpected_courage", "qty": 2},
    {"id": "river_of_gold", "qty": 2}
  ]
}
```

**Nora Warwick JSON** (`data/investigators/nora_warwick.json`):
```json
{
  "id": "nora_warwick",
  "name": "Professor Nora Warwick",
  "subtitle": "The Warwick Endowment",
  "class": "Rogue",
  "traits": ["Academic", "Archaeologist", "Blessed"],
  "stats": {"willpower": 3, "intellect": 5, "combat": 3, "agility": 2},
  "health": 7,
  "sanity": 8,
  "deck_size": 30,
  "deckbuilding": {
    "rogue": {"min_level": 0, "max_level": 5},
    "seeker": {"min_level": 0, "max_level": 2},
    "guardian": {"min_level": 0, "max_level": 2},
    "mystic": {"min_level": 0, "max_level": 1},
    "neutral": {"min_level": 0, "max_level": 5}
  },
  "ability": {
    "trigger": "once_per_round",
    "cost": {"resources": 1},
    "text": "Add 1 bless token to the chaos bag.",
    "effects": [
      {"type": "add_bless_token", "count": 1}
    ]
  },
  "elder_sign": {
    "modifier": 1,
    "text": "If you succeed, gain resources equal to the shroud value of your location.",
    "effects": [
      {"type": "conditional", "condition": "test_succeeded",
       "then": {"type": "gain_resources", "amount": "location_shroud"}}
    ]
  },
  "signatures": [
    {"id": "warwick_collection", "required": true},
    {"id": "family_debt", "required": true}
  ],
  "deck": [
    {"id": "ra_night_gaunt", "qty": 1},
    {"id": "call_of_anubis", "qty": 1},
    {"id": "horus_heresy", "qty": 1},
    {"id": "kopis", "qty": 1},
    {"id": "khopesh", "qty": 1},
    {"id": "sekhem_sceptre", "qty": 1},
    {"id": "book_of_dead", "qty": 1},
    {"id": "collar_of_sekhmet", "qty": 1},
    {"id": "isfets_fury", "qty": 1},
    {"id": "grave_robber", "qty": 2},
    {"id": "anti_chamber", "qty": 2},
    {"id": "pact_of_kha", "qty": 2},
    {"id": "ancient_intuition", "qty": 2},
    {"id": "ras_wrath", "qty": 2},
    {"id": "sobeks_gift", "qty": 2},
    {"id": "niles_blessing", "qty": 2},
    {"id": "power_ancients", "qty": 2},
    {"id": "oxford_studies", "qty": 2},
    {"id": "pharaohs_chariot", "qty": 2},
    {"id": "oxford_gambit", "qty": 2},
    {"id": "power_thebes", "qty": 2}
  ],
  "soak_cards": [
    {"id": "canopic_wrappings", "qty": 1},
    {"id": "scarab_amulet", "qty": 1},
    {"id": "eye_amulet", "qty": 1}
  ]
}
```

### Step 3: Card JSON Schema

Each card is stored in `data/cards/player/` or `data/cards/encounter/` as individual JSON files:

```json
{
  "id": "sacred_spear",
  "name": "The Sacred Spear",
  "subtitle": "Blessed By The Ancestors",
  "type": "asset",
  "slot": "hand",
  "class": "Guardian",
  "level": 0,
  "cost": 0,
  "traits": ["Item", "Relic", "Blessed", "Weapon"],
  "unique": true,
  "icons": {},
  "health": null,
  "sanity": null,
  "uses": null,
  "text": "Fight. You get +2 COM and +2 damage for this attack. If you succeed by 2 or more: This attack deals +3 damage instead.",
  "flavor": "\"It has tasted the blood of things older than memory. It remembers them all.\"",
  "effects": [
    {
      "trigger": "action_fight",
      "cost": null,
      "skill_test": {
        "skill": "combat",
        "difficulty": "enemy_fight",
        "bonuses": [{"stat": "combat", "amount": 2}]
      },
      "on_success": [
        {"type": "deal_damage", "amount": "base + 2"}
      ],
      "conditional": {
        "condition": "succeed_by_2_or_more",
        "then": [{"type": "deal_damage", "amount": "base + 3"}]
      }
    }
  ]
}
```

### Step 4: Chaos Bag Engine

```python
# engine/chaos_bag.py

@dataclass
class Token:
    symbol: str      # "+1", "0", "-1", "skull", "cultist", etc.
    modifier: int    # numerical modifier, or None for symbols
    
class ChaosBag:
    def __init__(self, difficulty: str = "standard"):
        self.difficulty = difficulty
        self.tokens = self._load_tokens(difficulty)
        self.bag = []
        self.bless_count = 0
        self.curse_count = 0
        self.reset()
    
    def reset(self):
        self.bag = list(self.tokens)
        random.shuffle(self.bag)
    
    def draw(self) -> Token:
        if not self.bag:
            self.bag = list(self.tokens)
            random.shuffle(self.bag)
        return self.bag.pop()
    
    def add_bless(self, count=1):
        self.bless_count += count
        for _ in range(count):
            self.tokens.append(Token("bless", 0))
    
    def add_curse(self, count=1):
        self.curse_count += count
        for _ in range(count):
            self.tokens.append(Token("curse", 0))
```

### Step 5: Skill Test Engine

```python
# engine/skill_test.py

@dataclass
class SkillTestResult:
    success: bool
    base_value: int
    token: Token
    modifier: int
    final_value: int
    difficulty: int
    elder_sign: bool = False
    auto_fail: bool = False
    bless_trigger: bool = False
    curse_trigger: bool = False

class SkillTestResolver:
    def resolve(self, investigator, skill, difficulty, committed_cards=None,
                chaos_bag=None, scenario_effects=None) -> SkillTestResult:
        # 1. Calculate base skill value
        base = investigator.stats[skill]
        for card in (committed_cards or []):
            base += card.icons.get(skill, 0)
        
        # 2. Draw chaos token
        token = chaos_bag.draw()
        
        # 3. Apply token modifier
        modifier = self._get_modifier(token, scenario_effects)
        
        # 4. Check for special tokens
        if token.symbol == "auto_fail":
            return SkillTestResult(False, base, token, modifier, base + modifier,
                                   difficulty, auto_fail=True)
        if token.symbol == "elder_sign":
            # Resolve investigator Elder Sign ability
            return SkillTestResult(True, base, token, modifier, base + modifier,
                                   difficulty, elder_sign=True)
        if token.symbol == "bless":
            modifier = 0  # Bless = auto-success (treat as 0 modifier)
            # Return +1 token to bag
        if token.symbol == "curse":
            modifier = -2  # Curse = -2
            # Return -1 token to bag
        
        # 5. Determine success/failure
        final = base + modifier
        success = final >= difficulty
        
        return SkillTestResult(success, base, token, modifier, final, difficulty)
```

### Step 6: Combat Engine

```python
# engine/combat.py

class CombatResolver:
    def fight(self, investigator, enemy, weapon=None, chaos_bag=None) -> FightResult:
        # Calculate combat value
        combat = investigator.stats["combat"]
        damage = 1
        
        if weapon:
            combat += weapon.fight_bonus
            damage += weapon.damage_bonus
        
        # Skill test
        result = SkillTestResolver().resolve(
            investigator, "combat", enemy.fight, chaos_bag=chaos_bag
        )
        
        # Apply damage on success
        if result.success:
            # Check for succeed-by-2 bonus (e.g., Sacred Spear)
            if result.final_value - enemy.fight >= 2:
                damage += weapon.succeed_by_2_bonus if weapon else 0
            enemy.take_damage(damage)
        
        # Retaliate on failure
        if not result.success and "Retaliate" in enemy.keywords:
            enemy.attack(investigator)
        
        return FightResult(result, damage)
    
    def evade(self, investigator, enemy, chaos_bag=None) -> EvadeResult:
        result = SkillTestResolver().resolve(
            investigator, "agility", enemy.evade, chaos_bag=chaos_bag
        )
        
        if result.success:
            enemy.exhaust()
            enemy.disengage()
        
        # Alert on failure
        if not result.success and "Alert" in enemy.keywords:
            enemy.attack(investigator)
        
        return EvadeResult(result)
```

### Step 7: Phase Implementations

```python
# engine/phases.py

class MythosPhase:
    def execute(self, game):
        for inv in game.investigators:
            # 1. Investigator ability triggers (Abel: add bless + heal)
            inv.resolve_ability("start_of_mythos", game)
            
            # 2. Draw encounter card
            card = game.encounter_deck.draw()
            card.resolve(inv, game)
            
            # 3. Place doom on agenda
            game.place_doom(1)

class InvestigationPhase:
    def execute(self, game):
        for inv in game.investigators:
            for _ in range(3):  # 3 actions
                action = game.ai_player.choose_action(inv, game)
                action.execute(inv, game)

class EnemyPhase:
    def execute(self, game):
        # 1. Ready enemies, move hunters
        for enemy in game.enemies:
            if not enemy.exhausted:
                if "Hunter" in enemy.keywords:
                    enemy.move_toward_prey(game.investigators)
        
        # 2. Engaged enemies attack
        for inv in game.investigators:
            for enemy in inv.engaged_enemies:
                if not enemy.exhausted:
                    enemy.attack(inv)

class UpkeepPhase:
    def execute(self, game):
        # 1. Ready all exhausted cards
        for inv in game.investigators:
            inv.ready_all()
        
        # 2. Draw 1 card, gain 1 resource
        for inv in game.investigators:
            inv.draw_card()
            inv.gain_resource()
        
        # 3. Gain 3 actions
        for inv in game.investigators:
            inv.actions = 3
```

### Step 8: AI Player (for Simulation Mode)

```python
# engine/ai_player.py

class AIPlayer:
    def choose_action(self, investigator, game) -> Action:
        """Simple heuristic-based decision making."""
        
        # Priority 1: Fight enemies engaged with us
        if investigator.engaged_enemies:
            enemy = investigator.engaged_enemies[0]
            if investigator.can_fight(enemy):
                return FightAction(investigator, enemy)
        
        # Priority 2: Investigate if we have high intellect
        if investigator.stats["intellect"] >= 3:
            location = game.get_current_location(investigator)
            if location.clues > 0:
                return InvestigateAction(investigator, location)
        
        # Priority 3: Move to location with clues or enemies
        for loc in game.locations:
            if loc.clues > 0 or loc.enemies:
                if game.is_connected(investigator.location, loc):
                    return MoveAction(investigator, loc)
        
        # Priority 4: Draw card or gain resource
        if len(investigator.hand) < 5:
            return DrawCardAction(investigator)
        else:
            return GainResourceAction(investigator)
```

### Step 9: Game Loop

```python
# engine/game.py

class GameState:
    def __init__(self, investigators, scenario, difficulty="standard"):
        self.investigators = investigators
        self.scenario = scenario
        self.chaos_bag = ChaosBag(difficulty)
        self.encounter_deck = EncounterDeck(scenario)
        self.agenda_deck = scenario.agenda_deck
        self.act_deck = scenario.act_deck
        self.current_agenda = self.agenda_deck[0]
        self.current_act = self.act_deck[0]
        self.locations = scenario.locations
        self.round_number = 0
        self.doom_count = 0
        self.clues_spent = 0
        self.game_over = False
        self.result = None
    
    def run(self, max_rounds=50):
        """Run the game until win/loss or max rounds."""
        # Setup
        self.setup()
        
        # Main loop (skip Mythos on round 1)
        while not self.game_over and self.round_number < max_rounds:
            self.round_number += 1
            
            # Mythos Phase (skip round 1)
            if self.round_number > 1:
                MythosPhase().execute(self)
            
            # Investigation Phase
            InvestigationPhase().execute(self)
            
            # Enemy Phase
            EnemyPhase().execute(self)
            
            # Upkeep Phase
            UpkeepPhase().execute(self)
            
            # Check win/loss
            self.check_end_condition()
        
        return GameResult(self)
    
    def setup(self):
        """Initial game setup."""
        for inv in self.investigators:
            inv.shuffle_deck()
            inv.draw_hand(5)
            # Place at starting location
            inv.location = self.scenario.starting_location
        
        self.encounter_deck.shuffle()
    
    def check_end_condition(self):
        """Check if game is won or lost."""
        # Loss: all investigators defeated
        if all(inv.defeated for inv in self.investigators):
            self.game_over = True
            self.result = "loss"
        
        # Win: act deck exhausted or scenario-specific condition
        if self.current_act is None:
            self.game_over = True
            self.result = "win"
        
        # Agenda advances = bad stuff
        if self.doom_count >= self.current_agenda.doom_threshold:
            self.advance_agenda()
```

### Step 10: Scenario Data — Spreading Flames

```json
{
  "id": "spreading_flames",
  "name": "Spreading Flames",
  "number": 1,
  "campaign": "Brethren of Ash",
  "chaos_bag_symbols": {
    "skull": "-X (X = current act number)",
    "cultist": "-1, reveal another token, if fail take 1 damage",
    "tablet": "-3, if fail by 2+ draw topmost Fire! from encounter discard",
    "elder_thing": "Draw 1 additional encounter card"
  },
  "setup": {
    "place_doom": 1,
    "starting_location": "your_friends_room"
  },
  "agenda_deck": [
    {
      "name": "Past Curfew",
      "doom_threshold": 3,
      "text": "The campus is strangely quiet. When this agenda advances: Each investigator tests Willpower (3). Each investigator who fails takes 1 horror."
    },
    {
      "name": "Lit Up",
      "doom_threshold": 4,
      "text": "When this agenda advances: Each investigator takes 1 damage and 1 horror."
    },
    {
      "name": "Wild Flames",
      "doom_threshold": 5,
      "text": "When this agenda advances: Each investigator is defeated."
    }
  ],
  "act_deck": [
    {
      "name": "Where There's Smoke...",
      "clue_threshold": 2,
      "text": "Objective: At end of round, investigators may spend clues to advance."
    },
    {
      "name": "Escape the Dorms",
      "clue_threshold": 3,
      "text": "Objective: Spend 3 clues to advance."
    },
    {
      "name": "Searching for Dr. Armitage",
      "clue_threshold": 4,
      "text": "Objective: Spend 4 clues to advance."
    },
    {
      "name": "Blaze of Glory",
      "clue_threshold": 0,
      "text": "Final stage."
    }
  ],
  "locations": [
    {"id": "your_friends_room", "name": "Your Friend's Room", "shroud": 2, "clues": 1, "connections": ["miskatonic_quad"]},
    {"id": "miskatonic_quad", "name": "Miskatonic Quad", "shroud": 3, "clues": 2, "connections": ["your_friends_room", "dormitories", "science_hall", "orne_library"]},
    {"id": "dormitories", "name": "Dormitories", "shroud": 2, "clues": 1, "connections": ["miskatonic_quad"]},
    {"id": "science_hall", "name": "Science Hall", "shroud": 3, "clues": 2, "connections": ["miskatonic_quad", "warren_observatory"]},
    {"id": "warren_observatory", "name": "Warren Observatory", "shroud": 4, "clues": 2, "connections": ["science_hall"]},
    {"id": "orne_library", "name": "Orne Library", "shroud": 3, "clues": 1, "connections": ["miskatonic_quad"]}
  ],
  "encounter_sets": ["ashen_pilgrims", "bystanders", "cosmic_evils", "fire"],
  "enemies": [
    {
      "id": "servant_of_flame",
      "name": "Servant of Flame: Raging Fury",
      "fight": 4,
      "evade": 4,
      "health": 5,
      "damage": 2,
      "horror": 2,
      "traits": ["Humanoid", "Elite"],
      "keywords": ["Hunter", "Retaliate"],
      "prey": "lowest_combat",
      "victory": 2
    },
    {
      "id": "cantor_of_flame",
      "name": "Cantor of Flame",
      "fight": 2,
      "evade": 2,
      "health": 2,
      "damage": 1,
      "horror": 0,
      "traits": ["Humanoid", "Cultist"],
      "keywords": ["Retaliate"]
    },
    {
      "id": "bystander",
      "name": "Bystander",
      "fight": 2,
      "evade": 2,
      "health": 2,
      "damage": 1,
      "horror": 1,
      "traits": ["Humanoid", "Civilian"],
      "keywords": ["Aloof"],
      "on_defeat": "each_investigator_at_location_gains_1_doom"
    },
    {
      "id": "hellhound",
      "name": "Hellhound",
      "fight": 2,
      "evade": 4,
      "health": 3,
      "damage": 1,
      "horror": 1,
      "traits": ["Creature", "Monster"],
      "keywords": ["Hunter"],
      "after_attack": "discard_1_asset_you_control"
    }
  ]
}
```

### Step 11: Encounter Card JSON (Fire! example)

```json
{
  "id": "fire",
  "name": "Fire!",
  "type": "treachery",
  "traits": ["Hazard"],
  "text": "Fire deals 1 damage to each card you control with health. Test Agility (3). If you succeed: Discard Fire!. If you fail: Fire! remains in play. At the end of the round: If Fire! is still in play, each investigator at this location takes 1 damage.",
  "effects": [
    {
      "trigger": "reveal",
      "effects": [
        {"type": "deal_damage", "target": "all_cards_with_health_you_control", "amount": 1},
        {"type": "skill_test", "skill": "agility", "difficulty": 3,
         "on_success": [{"type": "discard_self"}],
         "on_fail": [{"type": "attach_to_location"}]}
      ]
    }
  ]
}
```

### Step 12: CLI Commands

```bash
# Run a single game simulation
python run.py simulate --investigator abel_redcloud --scenario spreading_flames --difficulty standard --verbose

# Run 2-player game
python run.py simulate --investigator abel_redcloud,nora_warwick --scenario spreading_flames --difficulty standard

# Run 1000 Monte Carlo simulations
python run.py simulate --investigator abel_redcloud --scenario spreading_flames --iterations 1000

# Analyze a deck
python run.py analyze --investigator abel_redcloud --report full

# Compare investigators
python run.py compare --investigator abel_redcloud,nora_warwick --scenario spreading_flames --iterations 100

# Run campaign
python run.py campaign --investigator abel_redcloud --difficulty standard
```

### Step 13: Display Output Example

```
╔══════════════════════════════════════════════════════════════╗
║  ROUND 3 — INVESTIGATION PHASE                              ║
╠══════════════════════════════════════════════════════════════╣
║  Abel Redcloud (COM 4, HP 8/8, SAN 7/7)                    ║
║  Location: Miskatonic Quad (Shroud 3, Clues: 1)             ║
║  Hand: Sacred Spear, Spirit Coyote, Vicious Blow, Tracker   ║
║  Resources: 5 | Actions: 3                                  ║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
║  ACTION 1: Fight Servant of Flame (Fight 4)                  ║
║  ├─ Committed: Vicious Blow (+1 COM, +1 dmg on success)     ║
║  ├─ Base: 4 + 1 = 5                                         ║
║  ├─ Token drawn: -1                                          ║
║  ├─ Final: 5 - 1 = 4 vs Difficulty 4                        ║
║  └─ SUCCESS! (by 0) — Deal 2 damage (1 base + 1 Vicious)   ║
║                                                              ║
║  ACTION 2: Investigate Miskatonic Quad (Shroud 3)            ║
║  ├─ Base: 2 (INT)                                           ║
║  ├─ Token drawn: 0                                          ║
║  ├─ Final: 2 + 0 = 2 vs Shroud 3                           ║
║  └─ FAILURE — No clue discovered                             ║
║                                                              ║
║  ACTION 3: Gain Resource                                     ║
║  └─ Resources: 5 → 6                                        ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
```

### Implementation Order

| Step | Task | Files | Est. Time |
|---|---|---|---|
| 1 | Project setup + dependencies | run.py, requirements.txt, setup.py | 30 min |
| 2 | Data models (Card, Investigator, Enemy, Location) | engine/models.py | 1 hour |
| 3 | Chaos bag engine | engine/chaos_bag.py, config/chaos_bags.yaml | 1 hour |
| 4 | Skill test resolver | engine/skill_test.py | 1 hour |
| 5 | Combat resolver | engine/combat.py | 1 hour |
| 6 | Phase implementations | engine/phases.py | 2 hours |
| 7 | Game loop + state | engine/game.py | 2 hours |
| 8 | AI player | engine/ai_player.py | 1 hour |
| 9 | Card effect resolver | engine/effects.py | 2 hours |
| 10 | Abel Redcloud data | data/investigators/abel_redcloud.json + card JSONs | 2 hours |
| 11 | Nora Warwick data | data/investigators/nora_warwick.json + card JSONs | 2 hours |
| 12 | Spreading Flames scenario | data/scenarios/spreading_flames.json + encounter JSONs | 2 hours |
| 13 | CLI interface | cli/main.py, cli/display.py | 2 hours |
| 14 | Testing + debugging | tests/ | 2 hours |
| **Total** | | | **~20 hours** |

### First Deliverable
After Step 14, we should be able to run:
```bash
python run.py simulate --investigator abel_redcloud --scenario spreading_flames --difficulty standard --verbose
```
And see a full game simulation with all card draws, skill tests, combat, and results.

---

## Implementation Progress (Updated Jul 2026)

### Completed Steps
| Step | Task | Status |
|---|---|---|
| 1 | Project setup + dependencies | ✅ Done |
| 2 | Data models (Card, Investigator, Enemy, Location, GameState, Deck) | ✅ Done |
| 3 | Chaos bag engine (Standard/Easy, bless/curse) | ✅ Done |
| 4 | Skill test resolver | ✅ Done |
| 5 | Combat resolver (fight, evade, enemy attack) | ✅ Done |
| 6 | Phase implementations (Mythos, Investigation, Enemy, Upkeep) | ✅ Done |
| 7 | Game loop + state + win/loss conditions | ✅ Done |
| 8 | AI player (priority-based: fight > investigate > move > play) | ✅ Done |
| 9 | Card effect resolver (skeleton) | ✅ Done |
| 10 | Abel Redcloud JSON data (36 cards) | ✅ Done |
| 11 | Nora Warwick JSON data (39 cards) | ✅ Done |
| 12 | Spreading Flames scenario (5 locations, encounter deck, 3 agendas/acts) | ✅ Done |
| 13 | CLI interface (simulate, list-investigators, list-scenarios) | ✅ Done |
| 14 | Testing + debugging | ✅ Done |
| 15 | Keywords parsing fix (weapon detection) | ✅ Done |

### Key Results
- **Win Rate:** 100% over 200 games (Abel + Nora vs Spreading Flames, Standard)
- **Average Rounds:** 7.1
- **AI Behavior:** Moves between locations, fights engaged enemies, investigates for clues
- **Weapon Fix:** Keywords parsed from string to list — weapon detection now correctly identifies Sacred Spear/Switchblade in play
- **Sacred Spear Impact:** Abel deals 3 damage/hit (COM4 + 2 weapon), Servant dies in 2 hits

### Remaining Work
| Step | Task | Priority |
|---|---|---|
| 15 | Campaign mode (trauma/XP between scenarios) | High |
| 16 | Additional investigators (Eleanor, Agnes, etc.) | Medium |
| 17 | Additional scenarios (Smoke and Mirrors, Queen of Ash) | Medium |
| 18 | Card effect framework (trigger system, ability resolution) | Medium |
| 19 | Deck builder CLI | Low |
| 20 | Monte Carlo analysis (statistics, probability calculations) | Low |

### CLI Usage
```bash
cd simulator

# Single game
py run.py simulate -i abel_redcloud,nora_warwick -s spreading_flames

# Monte Carlo (100 games)
py run.py simulate -i abel_redcloud,nora_warwick -s spreading_flames -n 100

# List content
py run.py list-investigators
py run.py list-scenarios

# Show investigator details
py run.py show-investigator -i abel_redcloud
```
