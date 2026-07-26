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
│   └── effects.py               ← Card effect resolution system
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
│   ├── --investigator, -i    Choose investigator
│   ├── --scenario, -s        Choose scenario (1-3)
│   ├── --difficulty, -d      Difficulty (easy/standard)
│   ├── --players, -p         Player count (1-4)
│   └── --verbose, -v         Show detailed card draws
├── analyze           Analyze a deck
│   ├── --investigator, -i    Choose investigator
│   └── --report, -r          Report type (full/quick/probability)
├── campaign          Run full campaign simulation
│   ├── --investigator, -i    Choose investigator
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
    ├── --investigator, -i    Choose investigator
    ├── --add, -a             Add card to deck
    ├── --remove, -r          Remove card from deck
    └── --validate            Validate deck legality
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
2. **Campaign Mode**: Run all 3 scenarios with trauma/XP progression
3. **Monte Carlo**: Run 1000 simulations and report win rates
4. **Deck Analysis**: Full breakdown of deck strengths, weaknesses, and recommendations
5. **Probability Calculator**: Exact odds for any skill test given chaos bag composition
6. **All 9 Investigators**: Each one playable and balanced against Chapter 2 content

---

## Open Questions

1. Should the simulator support multiplayer (2-4 investigators) from the start, or single investigator first?
2. How detailed should card effect resolution be? (Full text parsing vs. simplified keywords)
3. Should we store game logs for post-game analysis?
4. Do you want a deck builder CLI as part of this, or separate tool?
