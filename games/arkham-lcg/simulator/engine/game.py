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
        from .phases import Logger
        Logger.set_log_func(self._log)

        self.game_state.phase = "setup"
        self.game_state.round = 0

        self._log('=' * 60)
        self._log(f'SCENARIO: {self.game_state.scenario_name}')
        self._log(f'DIFFICULTY: {self.difficulty}')
        self._log('=' * 60)

        # Agenda info
        if self.game_state.current_agenda:
            self._log(f'Agenda: {self.game_state.current_agenda.name} (doom threshold: {self.game_state.current_agenda.doom_threshold})')
        if self.game_state.current_act:
            self._log(f'Act: {self.game_state.current_act.name} (clues needed: {self.game_state.current_act.clues_needed})')
        self._log(f'Locations: {", ".join(loc.name for loc in self.game_state.locations)}')

        # Draw opening hands
        self._log('')
        for inv in self.game_state.investigators:
            inv.resources = 5
            self._log(f'--- {inv.name} ({inv.card_class}, WIL{inv.willpower} INT{inv.intellect} COM{inv.combat} AGI{inv.agility}) ---')
            self._log(f'  HP: {inv.health}/{inv.health} | SAN: {inv.sanity}/{inv.sanity} | Resources: {inv.resources}')

            # Draw 5 cards
            drawn = []
            for _ in range(5):
                card = inv.deck.draw()
                if card:
                    drawn.append(card)
                    inv.hand.append(card)

            self._log(f'  Opening hand ({len(inv.hand)} cards):')
            for card in inv.hand:
                self._log(f'    [{card.name}] ({card.type.value}, cost {card.cost}r)', indent=1)

            # Mulligan: discard and redraw any non-signature, non-asset cards
            mulliganed = []
            keep = []
            for card in inv.hand:
                if card.name in [s.name for s in inv.set_aside]:
                    keep.append(card)
                elif card.type.value == "skill":
                    mulliganed.append(card)
                else:
                    keep.append(card)

            if mulliganed:
                self._log(f'  Mulliganing {len(mulliganed)} card(s):')
                for card in mulliganed:
                    self._log(f'    Discard [{card.name}]', indent=1)
                    inv.hand.remove(card)
                    inv.discard.append(card)

                # Draw replacements
                for _ in range(len(mulliganed)):
                    card = inv.deck.draw()
                    if card:
                        inv.hand.append(card)
                        self._log(f'    Draw [{card.name}]', indent=1)

            self._log(f'  Final hand ({len(inv.hand)} cards):')
            for card in inv.hand:
                self._log(f'    [{card.name}] ({card.type.value}, cost {card.cost}r)', indent=1)
            self._log('')

        # Spawn Wendigo if Abel Redcloud is in the game
        for inv in self.game_state.investigators:
            if inv.id == "abel_redcloud":
                self._spawn_wendigo()
                break

    def run(self, max_rounds: int = 50) -> GameResult:
        """Run the full game loop."""
        self.setup()

        while not self.game_over and self.round_count < max_rounds:
            self.round_count += 1
            self.game_state.round = self.round_count
            self._log('')
            self._log('=' * 60)
            self._log(f'ROUND {self.round_count}')
            self._log('=' * 60)

            # Show investigator status
            for inv in self.game_state.investigators:
                status = 'DEFEATED' if inv.is_defeated() else f'HP {inv.current_health}/{inv.health} SAN {inv.current_sanity}/{inv.sanity}'
                engaged = [e.name for e in inv.engaged_enemies]
                engaged_str = f' vs {", ".join(engaged)}' if engaged else ''
                self._log(f'  {inv.name}: {status} | {inv.resources}r | {len(inv.hand)} cards{engaged_str}')

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
            enemy_phase = EnemyPhase()
            enemy_phase.execute(self.game_state)

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

            # Spawn Servant of Flame when Agenda 1 advances
            if agenda_index == 0:
                self._spawn_servant_of_flame()

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
                    self.game_state.clues_gathered = 0
                else:
                    # Last act completed = victory!
                    self.game_over = True
                    self.game_over_reason = "All acts completed — victory!"
                    for inv in self.game_state.investigators:
                        if not inv.is_defeated():
                            inv.victory_points += 5
                    return

        # Check if Act 3 requires defeating Servant of Flame
        if self.game_state.servant_of_flame_defeated:
            self.game_over = True
            self.game_over_reason = "Servant of Flame defeated — victory!"
            for inv in self.game_state.investigators:
                if not inv.is_defeated():
                    inv.victory_points += 5
            return

    def _spawn_servant_of_flame(self):
        """Spawn the Servant of Flame from the victory display."""
        for card in self.game_state.victory_display:
            if card.name == "Servant of Flame":
                enemy = Enemy(
                    id="servant_of_flame",
                    name="Servant of Flame",
                    type=card.type,
                    fight=card.fight,
                    evade=card.evade,
                    health=card.health,
                    current_health=card.health,
                    damage=card.damage,
                    horror=card.horror,
                    victory=card.victory,
                    keywords=card.keywords,
                    traits=card.traits
                )
                # Spawn at first alive investigator's location
                for inv in self.game_state.investigators:
                    if not inv.is_defeated():
                        enemy.engaged_with = inv.id
                        inv.engaged_enemies.append(enemy)
                        self.game_state.enemies.append(enemy)
                break

    def _spawn_wendigo(self):
        """Spawn the Wendigo for Abel Redcloud's signature weakness."""
        # Find the Wendigo in Abel's set-aside cards
        for inv in self.game_state.investigators:
            if inv.id == "abel_redcloud":
                for card in inv.set_aside:
                    if card.name == "Wendigo":
                        # Find the investigator with the lowest combat (excluding Abel)
                        target_inv = None
                        lowest_combat = float('inf')
                        for other_inv in self.game_state.investigators:
                            if other_inv.id != "abel_redcloud" and not other_inv.is_defeated():
                                if other_inv.combat < lowest_combat:
                                    lowest_combat = other_inv.combat
                                    target_inv = other_inv
                        
                        # If no other investigator, spawn with Abel (but he can't attack it)
                        if target_inv is None:
                            target_inv = inv
                        
                        # Create the enemy
                        enemy = Enemy(
                            id="wendigo",
                            name="Wendigo",
                            type=card.type,
                            fight=card.fight,
                            evade=card.evade,
                            health=card.health,
                            current_health=card.health,
                            damage=card.damage,
                            horror=card.horror,
                            keywords=card.keywords,
                            traits=card.traits
                        )
                        enemy.engaged_with = target_inv.id
                        target_inv.engaged_enemies.append(enemy)
                        self.game_state.enemies.append(enemy)
                        
                        self._log(f'  Wendigo spawned engaged with {target_inv.name} (lowest combat: {lowest_combat})')
                        break
                break

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
            victory=self.game_over and "victory" in self.game_over_reason.lower(),
            rounds_played=self.round_count,
            investigators_survived=survived,
            investigators_defeated=defeated,
            agenda_advanced=len(self.game_state.agendas) - 1,
            act_progress=self.game_state.acts.index(self.game_state.current_act) if self.game_state.current_act else 0,
            damage_taken=sum(inv.health - inv.current_health for inv in self.game_state.investigators),
            horror_taken=sum(inv.sanity - inv.current_sanity for inv in self.game_state.investigators),
            log_path=str(log_path)
        )

    def _log(self, message: str, indent: int = 0):
        """Log a message."""
        print(message)
