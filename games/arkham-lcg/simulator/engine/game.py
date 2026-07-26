import json
from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any
from pathlib import Path
from .models import Investigator, Enemy, Location, Agenda, Act, Card, GameState, Deck, CardType
from .chaos_bag import ChaosBag
from .phases import MythosPhase, InvestigationPhase, EnemyPhase, UpkeepPhase
from .combat import CombatResolver
from .skill_test import SkillTestResolver
from .ai_player import AIPlayer
import random
import logging
from datetime import datetime

logger = logging.getLogger(__name__)


@dataclass
class GameResult:
    victory: bool
    rounds_played: int
    investigators_survived: List[str]
    investigators_defeated: List[str]
    agenda_advanced: int
    act_progress: int
    damage_taken: int
    horror_taken: int
    log_path: str

    def __str__(self):
        return (
            f"{'VICTORY' if self.victory else 'DEFEAT'} | "
            f"Rounds: {self.rounds_played} | "
            f"Survived: {len(self.investigators_survived)} | "
            f"Defeated: {len(self.investigators_defeated)}"
        )


class Game:
    def __init__(self, investigator_ids: List[str], scenario_id: str,
                 difficulty: str = "standard"):
        self.difficulty = difficulty
        self.chaos_bag = ChaosBag(difficulty)
        self.game_state = GameState()
        self.game_state.chaos_bag = self.chaos_bag
        self.ai_player = AIPlayer()
        self.game_state.ai_player = self.ai_player
        self.round_count = 0
        self.game_over = False
        self.game_over_reason = ""

        # Load scenario data
        self._load_scenario(scenario_id)

        # Load investigator data
        for inv_id in investigator_ids:
            self._load_investigator(inv_id)

    def _load_scenario(self, scenario_id: str):
        """Load scenario data from JSON."""
        data_dir = Path(__file__).parent.parent / "data" / "scenarios"
        filepath = data_dir / f"{scenario_id}.json"

        if not filepath.exists():
            # Use minimal default scenario
            self._create_default_scenario()
            return

        with open(filepath, 'r') as f:
            data = json.load(f)

        self.game_state.scenario_name = data["name"]
        self.game_state.scenario_id = scenario_id

        # Load agendas
        for agenda_data in data.get("agendas", []):
            agenda = Agenda(
                id=agenda_data["id"],
                name=agenda_data["name"],
                type=CardType.AGENDA,
                text=agenda_data.get("text", ""),
                doom_threshold=agenda_data.get("doom_threshold", 8),
                victory=agenda_data.get("victory", 0)
            )
            self.game_state.agendas.append(agenda)
        if self.game_state.agendas:
            self.game_state.current_agenda = self.game_state.agendas[0]

        # Load acts
        for act_data in data.get("acts", []):
            act = Act(
                id=act_data["id"],
                name=act_data["name"],
                type=CardType.ACT,
                text=act_data.get("text", ""),
                victory=act_data.get("victory", 0),
                clues_needed=act_data.get("clues_needed", 0)
            )
            self.game_state.acts.append(act)
        if self.game_state.acts:
            self.game_state.current_act = self.game_state.acts[0]

        # Load locations
        for loc_data in data.get("locations", []):
            location = Location(
                id=loc_data["id"],
                name=loc_data["name"],
                type=CardType.LOCATION,
                shroud=loc_data.get("shroud", 2),
                clues=loc_data.get("clues", 0),
                connections=loc_data.get("connections", [])
            )
            self.game_state.locations.append(location)
        if self.game_state.locations:
            self.game_state.current_location = self.game_state.locations[0]

        # Load encounter deck
        encounter_cards = []
        for card_data in data.get("encounter_cards", []):
            card = Card(
                id=card_data.get("id", card_data["name"].lower().replace(" ", "_")),
                name=card_data["name"],
                type=Card._type(card_data.get("type", "treachery")),
                cost=card_data.get("cost", 0),
                text=card_data.get("text", ""),
                traits=card_data.get("traits", ""),
                keywords=card_data.get("keywords", ""),
                fight=card_data.get("fight", 0),
                evade=card_data.get("evade", 0),
                health=card_data.get("health", 0),
                damage=card_data.get("damage", 0),
                horror=card_data.get("horror", 0)
            )
            encounter_cards.append(card)

        self.game_state.encounter_deck = Deck(
            name="Encounter Deck",
            cards=encounter_cards
        )

        # Load victory display
        victory_data = data.get("victory_display", [])
        for v in victory_data:
            card = Card(
                id=v.get("id", v["name"].lower().replace(" ", "_")),
                name=v["name"],
                type=Card._type(v.get("type", "enemy")),
                fight=v.get("fight", 0),
                evade=v.get("evade", 0),
                health=v.get("health", 0),
                damage=v.get("damage", 0),
                horror=v.get("horror", 0),
                victory=v.get("victory", 0),
                traits=v.get("traits", "")
            )
            self.game_state.victory_display.append(card)

    def _create_default_scenario(self):
        """Create a minimal default scenario for testing."""
        self.game_state.scenario_name = "Default Scenario"
        self.game_state.scenario_id = "default"

        agenda = Agenda(
            id="agenda_1",
            name="The Darkness",
            doom_threshold=8
        )
        self.game_state.agendas.append(agenda)
        self.game_state.current_agenda = agenda

        act = Act(
            id="act_1",
            name="Investigation"
        )
        self.game_state.acts.append(act)
        self.game_state.current_act = act

        location = Location(
            id="loc_1",
            name="Arkham City",
            shroud=3,
            clues=2
        )
        self.game_state.locations.append(location)
        self.game_state.current_location = location

    def _load_investigator(self, inv_id: str):
        """Load investigator data from JSON."""
        data_dir = Path(__file__).parent.parent / "data" / "investigators"
        filepath = data_dir / f"{inv_id}.json"

        if not filepath.exists():
            logger.warning(f"Investigator file not found: {filepath}")
            return

        with open(filepath, 'r') as f:
            data = json.load(f)

        # Create deck
        deck_cards = []
        for card_data in data.get("deck", []):
            card = Card(
                id=card_data.get("id", card_data["name"].lower().replace(" ", "_")),
                name=card_data["name"],
                type=Card._type(card_data.get("type", "asset")),
                level=card_data.get("level", 0),
                cost=card_data.get("cost", 0),
                text=card_data.get("text", ""),
                traits=card_data.get("traits", ""),
                slot=card_data.get("slot", ""),
                willpower=card_data.get("icons", {}).get("willpower", 0),
                intellect=card_data.get("icons", {}).get("intellect", 0),
                combat=card_data.get("icons", {}).get("combat", 0),
                agility=card_data.get("icons", {}).get("agility", 0),
                wild=card_data.get("icons", {}).get("wild", 0),
                fight=card_data.get("fight", 0),
                evade=card_data.get("evade", 0),
                health=card_data.get("health", 0),
                sanity=card_data.get("sanity", 0),
                damage=card_data.get("damage", 0),
                horror=card_data.get("horror", 0),
                keywords=card_data.get("keywords", ""),
                ability_text=card_data.get("ability_text", "")
            )
            deck_cards.append(card)

        # Create signature cards (set-aside)
        signature_cards = []
        for card_data in data.get("signatures", []):
            card = Card(
                id=card_data.get("id", card_data["name"].lower().replace(" ", "_")),
                name=card_data["name"],
                type=Card._type(card_data.get("type", "asset")),
                cost=card_data.get("cost", 0),
                text=card_data.get("text", ""),
                traits=card_data.get("traits", ""),
                slot=card_data.get("slot", ""),
                willpower=card_data.get("icons", {}).get("willpower", 0),
                intellect=card_data.get("icons", {}).get("intellect", 0),
                combat=card_data.get("icons", {}).get("combat", 0),
                agility=card_data.get("icons", {}).get("agility", 0),
                wild=card_data.get("icons", {}).get("wild", 0),
                fight=card_data.get("fight", 0),
                evade=card_data.get("evade", 0),
                health=card_data.get("health", 0),
                sanity=card_data.get("sanity", 0),
                damage=card_data.get("damage", 0),
                horror=card_data.get("horror", 0),
                keywords=card_data.get("keywords", ""),
                ability_text=card_data.get("ability_text", "")
            )
            signature_cards.append(card)

        # Create investigator
        investigator = Investigator(
            id=inv_id,
            name=data["name"],
            subtitle=data.get("title", ""),
            card_class=data.get("class", "neutral"),
            willpower=data["stats"]["willpower"],
            intellect=data["stats"]["intellect"],
            combat=data["stats"]["combat"],
            agility=data["stats"]["agility"],
            health=data["stats"]["health"],
            sanity=data["stats"]["sanity"],
            health_max=data["stats"]["health"],
            sanity_max=data["stats"]["sanity"],
            ability_trigger=data.get("ability", {}).get("trigger", ""),
            ability_text=data.get("ability", {}).get("text", ""),
            elder_sign_text=data.get("elder_sign", {}).get("text", "")
        )

        # Create deck
        investigator.deck = Deck(
            name=f"{inv_id}_deck",
            cards=deck_cards
        )
        investigator.deck.shuffle()

        # Add signature cards to set-aside and hand
        for card in signature_cards:
            investigator.set_aside.append(card)
            investigator.hand.append(card)

        self.game_state.add_investigator(investigator)

    def setup(self):
        """Set up the game."""
        self.game_state.phase = "setup"
        self.game_state.round = 0

        # Draw initial hands (5 cards) and gain 5 resources
        for inv in self.game_state.investigators:
            for _ in range(5):
                card = inv.deck.draw()
                if card:
                    inv.hand.append(card)
            inv.resources = 5  # Starting resources

        self._log("=== GAME SETUP ===")
        self._log(f"Scenario: {self.game_state.scenario_name}")
        self._log(f"Difficulty: {self.difficulty}")
        for inv in self.game_state.investigators:
            self._log(f"  {inv.name} ready to investigate!")

    def run(self, max_rounds: int = 50) -> GameResult:
        """Run the full game loop."""
        self.setup()

        while not self.game_over and self.round_count < max_rounds:
            self.round_count += 1
            self.game_state.round = self.round_count
            self._log(f"\n=== ROUND {self.round_count} ===")

            # Upkeep Phase
            self.game_state.phase = "upkeep"
            upkeep = UpkeepPhase()
            upkeep.execute(self.game_state)

            # Mythos Phase
            self.game_state.phase = "mythos"
            mythos = MythosPhase()
            mythos.execute(self.game_state)

            # Investigation Phase
            self.game_state.phase = "investigation"
            investigation = InvestigationPhase()
            investigation.execute(self.game_state)

            # Enemy Phase
            self.game_state.phase = "enemy"
            enemy = EnemyPhase()
            enemy.execute(self.game_state)

            # Check win/lose conditions
            self._check_conditions()

        return self._create_result()

    def _check_conditions(self):
        """Check for game end conditions."""
        # Check if all investigators are defeated
        all_defeated = all(inv.is_defeated() for inv in self.game_state.investigators)
        if all_defeated:
            self.game_over = True
            self.game_over_reason = "All investigators defeated"
            return

        # Check agenda advancement
        if self.game_state.current_agenda and self.game_state.current_agenda.should_advance():
            agenda_index = self.game_state.agendas.index(self.game_state.current_agenda)
            # Deal damage/horror when agenda advances
            for inv in self.game_state.investigators:
                if not inv.is_defeated():
                    inv.take_damage(1, source="Agenda advance")
                    if agenda_index >= 1:
                        inv.take_horror(1, source="Agenda advance")

            # Advance to next agenda
            if agenda_index < len(self.game_state.agendas) - 1:
                self.game_state.current_agenda = self.game_state.agendas[agenda_index + 1]
            else:
                # Last agenda advanced = defeat (agenda out of time)
                self.game_over = True
                self.game_over_reason = "The agenda has run out of time!"
                return

        # Check act advancement based on clues
        if self.game_state.current_act:
            clues_needed = self.game_state.current_act.clues_needed
            if clues_needed > 0 and self.game_state.clues_gathered >= clues_needed:
                act_index = self.game_state.acts.index(self.game_state.current_act)
                # Advance to next act
                if act_index < len(self.game_state.acts) - 1:
                    self.game_state.current_act = self.game_state.acts[act_index + 1]
                    # Reset clue count for next act
                    self.game_state.clues_gathered = 0
                else:
                    # Last act completed = victory!
                    self.game_over = True
                    self.game_over_reason = "All acts completed — victory!"
                    for inv in self.game_state.investigators:
                        if not inv.is_defeated():
                            inv.victory_points += 5
                    return

    def _create_result(self) -> GameResult:
        """Create the final game result."""
        survived = []
        defeated = []
        for inv in self.game_state.investigators:
            if inv.is_defeated():
                defeated.append(inv.name)
            else:
                survived.append(inv.name)

        log_dir = Path(__file__).parent.parent / "logs"
        log_dir.mkdir(exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        log_path = log_dir / f"game_{timestamp}.txt"

        return GameResult(
            victory=self.game_over and "Victory" in self.game_over_reason,
            rounds_played=self.round_count,
            investigators_survived=survived,
            investigators_defeated=defeated,
            agenda_advanced=len(self.game_state.agendas) - 1,
            act_progress=self.game_state.acts.index(self.game_state.current_act) if self.game_state.current_act else 0,
            damage_taken=sum(inv.health - inv.current_health for inv in self.game_state.investigators),
            horror_taken=sum(inv.sanity - inv.current_sanity for inv in self.game_state.investigators),
            log_path=str(log_path)
        )

    def _log(self, message: str):
        """Log a message."""
        logger.info(message)
