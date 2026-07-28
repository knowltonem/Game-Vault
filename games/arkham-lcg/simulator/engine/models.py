from dataclasses import dataclass, field
from typing import Optional, List, Dict, Any
from enum import Enum
import random


class CardType(Enum):
    INVESTIGATOR = "investigator"
    ASSET = "asset"
    EVENT = "event"
    SKILL = "skill"
    TREACHERY = "treachery"
    ENEMY = "enemy"
    ACT = "act"
    AGENDA = "agenda"
    LOCATION = "location"


class Slot(Enum):
    HAND = "hand"
    ARCANE = "arcane"
    ACCESSORY = "accessory"
    BODY = "body"
    ALLY = "ally"
    NONE = None


class Skill(Enum):
    WILLPOWER = "willpower"
    INTELLECT = "intellect"
    COMBAT = "combat"
    AGILITY = "agility"


@dataclass
class Icons:
    willpower: int = 0
    intellect: int = 0
    combat: int = 0
    agility: int = 0
    wild: int = 0

    def get(self, skill: Skill) -> int:
        return getattr(self, skill.value, 0)

    def total_icons(self) -> int:
        return self.willpower + self.intellect + self.combat + self.agility + self.wild


@dataclass
class Card:
    id: str
    name: str
    type: CardType
    subtitle: str = ""
    card_class: str = ""
    level: int = 0
    cost: int = 0
    traits: List[str] = field(default_factory=list)
    unique: bool = False
    icons: Icons = field(default_factory=Icons)
    text: str = ""
    flavor: str = ""
    slot: Optional[Slot] = None
    health: Optional[int] = None
    current_health: Optional[int] = None
    sanity: Optional[int] = None
    current_sanity: Optional[int] = None
    uses: Optional[int] = None
    current_uses: Optional[int] = None
    uses_type: str = ""  # charges, ammo, supplies
    soak_health: int = 0
    soak_sanity: int = 0
    exhausted: bool = False
    keywords: List[str] = field(default_factory=list)
    ability_text: str = ""

    # Additional attributes for compatibility with game.py
    fight: int = 0
    evade: int = 0
    damage: int = 0
    horror: int = 0
    victory: int = 0
    quantity: int = 1  # For deck building

    # Icons as individual attributes for compatibility
    willpower: int = 0
    intellect: int = 0
    combat: int = 0
    agility: int = 0
    wild: int = 0

    @staticmethod
    def _parse_keywords(kw):
        """Parse keywords from string or list format into a list of stripped strings."""
        if isinstance(kw, list):
            return [k.strip() for k in kw if k.strip()]
        if isinstance(kw, str) and kw.strip():
            return [k.strip() for k in kw.split(".") if k.strip()]
        return []

    def has_keyword(self, keyword: str) -> bool:
        """Check if card has a keyword (case-insensitive, handles string or list)."""
        return keyword.lower() in [k.lower() for k in self._parse_keywords(self.keywords)]

    def __post_init__(self):
        # Normalize keywords to list
        self.keywords = self._parse_keywords(self.keywords)
        # Sync individual icon attributes with Icons object
        if self.willpower or self.intellect or self.combat or self.agility or self.wild:
            self.icons = Icons(
                willpower=self.willpower,
                intellect=self.intellect,
                combat=self.combat,
                agility=self.agility,
                wild=self.wild
            )

    def is_asset(self) -> bool:
        return self.type == CardType.ASSET

    def is_event(self) -> bool:
        return self.type == CardType.EVENT

    def is_skill(self) -> bool:
        return self.type == CardType.SKILL

    def has_uses(self) -> bool:
        return self.current_uses is not None and self.current_uses > 0

    def spend_use(self) -> bool:
        if self.has_uses():
            self.current_uses -= 1
            return True
        return False

    @staticmethod
    def _type(type_str: str) -> 'CardType':
        """Convert a string to CardType enum."""
        type_map = {
            "investigator": CardType.INVESTIGATOR,
            "asset": CardType.ASSET,
            "event": CardType.EVENT,
            "skill": CardType.SKILL,
            "treachery": CardType.TREACHERY,
            "enemy": CardType.ENEMY,
            "act": CardType.ACT,
            "agenda": CardType.AGENDA,
            "location": CardType.LOCATION
        }
        return type_map.get(type_str.lower(), CardType.ASSET)


@dataclass
class Enemy(Card):
    fight: int = 0
    evade: int = 0
    damage: int = 0
    horror: int = 0
    prey: str = ""
    victory: int = 0
    current_health: int = 0
    engaged_with: Optional[str] = None  # investigator id
    exhausted: bool = False

    def __post_init__(self):
        if self.current_health == 0 and self.health:
            self.current_health = self.health

    def take_damage(self, amount: int) -> bool:
        self.current_health -= amount
        return self.current_health <= 0

    def is_defeated(self) -> bool:
        return self.current_health <= 0

    def exhaust(self):
        self.exhausted = True

    def ready(self):
        self.exhausted = False

    def disengage(self):
        self.engaged_with = None

    def attack(self, investigator: 'Investigator'):
        """Attack an investigator."""
        investigator.take_damage(self.damage, source=self.name)
        investigator.take_horror(self.horror, source=self.name)


@dataclass
class Location(Card):
    shroud: int = 0
    clues: int = 0
    current_clues: int = 0
    connections: List[str] = field(default_factory=list)

    def __post_init__(self):
        if self.current_clues == 0:
            self.current_clues = self.clues

    def take_clue(self) -> bool:
        if self.current_clues > 0:
            self.current_clues -= 1
            return True
        return False


@dataclass
class Agenda(Card):
    doom_threshold: int = 0
    current_doom: int = 0

    def add_doom(self, amount: int = 1):
        self.current_doom += amount

    def should_advance(self) -> bool:
        return self.current_doom >= self.doom_threshold


@dataclass
class Act(Card):
    clue_threshold: int = 0
    clues_spent: int = 0
    clues_needed: int = 0  # Added for compatibility with game.py

    def spend_clues(self, amount: int) -> bool:
        if self.clues_spent + amount >= self.clue_threshold:
            return True
        self.clues_spent += amount
        return False


@dataclass
class Investigator:
    id: str
    name: str
    subtitle: str = ""
    card_class: str = "neutral"
    traits: List[str] = field(default_factory=list)
    stats: Dict[str, int] = field(default_factory=dict)  # willpower, intellect, combat, agility
    health: int = 0
    sanity: int = 0
    deck_size: int = 0
    ability_text: str = ""
    ability_trigger: str = ""  # start_of_mythos, once_per_round, etc.
    elder_sign_text: str = ""
    elder_sign_modifier: int = 1
    auto_fail_text: str = ""
    cultist_text: str = ""

    # Additional stats for compatibility
    willpower: int = 0
    intellect: int = 0
    combat: int = 0
    agility: int = 0
    health_max: int = 0
    sanity_max: int = 0

    # Game state
    current_health: int = 0
    current_sanity: int = 0
    resources: int = 0
    actions: int = 3
    hand: List[Card] = field(default_factory=list)
    deck: 'Deck' = None
    discard: List[Card] = field(default_factory=list)
    play_area: List[Card] = field(default_factory=list)
    engaged_enemies: List[Enemy] = field(default_factory=list)
    location: Optional[str] = None
    defeated: bool = False
    resigned: bool = False
    clues: int = 0
    trauma_damage: int = 0
    trauma_horror: int = 0
    victory_points: int = 0

    # Slot tracking
    slots: Dict[Slot, Optional[Card]] = field(default_factory=dict)
    asset_slots: Dict[str, Optional[Card]] = field(default_factory=dict)

    # Signature cards
    signatures: List[Card] = field(default_factory=list)
    set_aside: List[Card] = field(default_factory=list)

    # Ability tracking
    ability_used_this_round: bool = False
    bless_tokens_added: int = 0
    _pending_eleanor_heal: Optional[int] = None
    _pending_bless: int = 0

    # Temporary stat boosts
    temp_combat: int = 0
    temp_willpower: int = 0
    temp_intellect: int = 0
    temp_agility: int = 0

    # Scenario tracking
    servant_of_flame_defeated: bool = False

    def __post_init__(self):
        if self.current_health == 0:
            self.current_health = self.health
        if self.current_sanity == 0:
            self.current_sanity = self.sanity
        if self.health_max == 0:
            self.health_max = self.health
        if self.sanity_max == 0:
            self.sanity_max = self.sanity
        # Initialize slots
        if not self.slots:
            self.slots = {slot: None for slot in Slot}
        # Initialize asset slots
        if not self.asset_slots:
            self.asset_slots = {"hand": None, "arcane": None, "accessory": None, "body": None, "ally": None}

    def get_stat(self, skill: str) -> int:
        base = self.stats.get(skill, 0)
        # Also check individual attributes set directly
        if base == 0:
            base = getattr(self, skill, 0)
        # Add bonuses from assets in play
        for card in self.play_area:
            if card.is_asset() and not card.exhausted:
                if skill == "willpower" and "+1 <wil>" in card.text:
                    base += 1
                elif skill == "intellect" and "+1 <int>" in card.text:
                    base += 1
                elif skill == "combat" and "+1 <com>" in card.text:
                    base += 1
                elif skill == "agility" and "+1 <agi>" in card.text:
                    base += 1
                # Handle "You get +N <skill>" pattern
                import re
                m = re.search(r'\+(\d+)\s+<' + skill[:3] + '>', card.text)
                if m:
                    base += int(m.group(1))
        # Add temporary boosts (Man in Black ability)
        if skill == "combat":
            base += self.temp_combat
        elif skill == "willpower":
            base += self.temp_willpower
        elif skill == "intellect":
            base += self.temp_intellect
        elif skill == "agility":
            base += self.temp_agility
        return base

    def draw_card(self) -> Optional[Card]:
        if self.deck is None:
            return None
        card = self.deck.draw()
        if card:
            self.hand.append(card)
            return card
        return None

    def draw_hand(self, count: int):
        for _ in range(count):
            self.draw_card()

    def gain_resource(self, amount: int = 1):
        # Check if Sneaky Pete is in play (cannot gain resources)
        for enemy in self.engaged_enemies:
            if enemy.name == "Sneaky Pete":
                return  # Cannot gain resources while Sneaky Pete is engaged
        self.resources += amount

    def spend_resource(self, amount: int) -> bool:
        if self.resources >= amount:
            self.resources -= amount
            return True
        return False

    def take_damage(self, amount: int, source: str = "") -> bool:
        old_health = self.current_health

        # Check for soak assets (Big Tommy, Old Man Winters, etc.)
        for asset in list(self.play_area):
            if asset.soak_health > 0 and not asset.exhausted and amount > 0:
                soaked = min(amount, asset.soak_health)
                asset.soak_health -= soaked
                amount -= soaked
                asset.exhausted = True
                from .phases import Logger
                Logger.log(f'    {asset.name} soaks {soaked} damage (remaining soak: {asset.soak_health})')
                if asset.soak_health <= 0:
                    self.discard_card(asset)
                    Logger.log(f'    {asset.name} destroyed!')

        self.current_health -= amount
        if self.current_health <= 0:
            self.current_health = 0
            self.defeated = True
        
        # Eleanor Heart's ability: after taking damage, heal from any investigator
        if self.id == "eleanor_heart" and not self.ability_used_this_round:
            damage_taken = old_health - self.current_health
            if damage_taken > 0:
                # Determine heal amount based on damage on Eleanor
                damage_on_eleanor = self.health - self.current_health
                if damage_on_eleanor >= 7:
                    heal_amount = 4
                elif damage_on_eleanor >= 6:
                    heal_amount = 3
                elif damage_on_eleanor >= 3:
                    heal_amount = 2
                else:
                    heal_amount = 1
                # Store for resolution in phases.py (needs game_state for other investigators)
                self._pending_eleanor_heal = heal_amount
                self.ability_used_this_round = True
        
        return self.defeated

    def take_horror(self, amount: int, source: str = "") -> bool:
        # Check for soak assets (Old Man Winters, etc.)
        for asset in list(self.play_area):
            if asset.soak_sanity > 0 and not asset.exhausted and amount > 0:
                soaked = min(amount, asset.soak_sanity)
                asset.soak_sanity -= soaked
                amount -= soaked
                asset.exhausted = True
                from .phases import Logger
                Logger.log(f'    {asset.name} soaks {soaked} horror (remaining soak: {asset.soak_sanity})')
                if asset.soak_sanity <= 0:
                    self.discard_card(asset)
                    Logger.log(f'    {asset.name} destroyed!')

        self.current_sanity -= amount
        if self.current_sanity <= 0:
            self.current_sanity = 0
            self.defeated = True
        return self.defeated

    def heal_damage(self, amount: int, healer=None):
        old_health = self.current_health
        self.current_health = min(self.current_health + amount, self.health)
        actual_healed = self.current_health - old_health
        if actual_healed > 0:
            self._check_heal_triggers(actual_healed, healer)

    def heal_horror(self, amount: int, healer=None):
        old_sanity = self.current_sanity
        self.current_sanity = min(self.current_sanity + amount, self.sanity)
        actual_healed = self.current_sanity - old_sanity
        if actual_healed > 0:
            self._check_heal_triggers(actual_healed, healer)

    def _check_heal_triggers(self, amount: int, healer=None):
        """Check for heal triggers from assets: Fort Warren Chapel, Private Parker."""
        trigger_owner = healer if healer else self
        for asset in list(trigger_owner.play_area):
            if asset.name == "Fort Warren Chapel":
                self._pending_bless += 1
                from .phases import Logger
                Logger.log(f'    Fort Warren Chapel: +1 bless token ({self._pending_bless} pending)')
            elif asset.name == "Private Parker":
                drawn = trigger_owner.draw_card()
                if drawn:
                    from .phases import Logger
                    Logger.log(f'    Private Parker: draws [{drawn.name}]')

    def is_defeated(self) -> bool:
        return self.defeated or self.current_health <= 0 or self.current_sanity <= 0

    def ready_all(self):
        self.actions = 3
        self.ability_used_this_round = False
        # Reset temporary stat boosts
        self.temp_combat = 0
        self.temp_willpower = 0
        self.temp_intellect = 0
        self.temp_agility = 0
        for card in self.play_area:
            if hasattr(card, 'exhausted'):
                card.exhausted = False

    def get_effective_combat(self):
        """Get combat value including temporary boosts."""
        return self.combat + self.temp_combat

    def play_card(self, card: Card) -> bool:
        if card.cost > self.resources:
            return False
        self.spend_resource(card.cost)
        self.hand.remove(card)
        if card.is_asset():
            self.play_area.append(card)
        else:
            self.discard.append(card)
        return True

    def discard_card(self, card: Card):
        if card in self.hand:
            self.hand.remove(card)
        if card in self.play_area:
            self.play_area.remove(card)
        self.discard.append(card)

    def get_playable_cards(self) -> List[Card]:
        return [c for c in self.hand if c.cost <= self.resources]

    def get_assets_in_slot(self, slot: Slot) -> List[Card]:
        return [c for c in self.play_area if c.slot == slot]


class Deck:
    """A deck of cards."""
    def __init__(self, name: str = "", cards: List[Card] = None):
        self.name = name
        self.cards = cards if cards else []
        self.original_cards = list(self.cards)
        self.shuffle()

    def shuffle(self):
        """Shuffle the deck."""
        random.shuffle(self.cards)

    def draw(self) -> Optional[Card]:
        """Draw a card from the deck."""
        if not self.cards:
            return None
        return self.cards.pop(0)

    def add_card(self, card: Card):
        """Add a card to the deck."""
        self.cards.append(card)

    def remove_card(self, card: Card):
        """Remove a card from the deck."""
        if card in self.cards:
            self.cards.remove(card)
        if card in self.original_cards:
            self.original_cards.remove(card)

    def get_size(self) -> int:
        """Get the current size of the deck."""
        return len(self.cards)

    def is_empty(self) -> bool:
        """Check if the deck is empty."""
        return len(self.cards) == 0


class Action:
    """Base class for actions."""
    def execute(self, investigator: 'Investigator', game_state: 'GameState'):
        pass


class GameState:
    """Represents the current state of the game."""
    def __init__(self):
        self.investigators: List[Investigator] = []
        self.enemies: List[Enemy] = []
        self.locations: List[Location] = []
        self.agendas: List[Agenda] = []
        self.acts: List[Act] = []
        self.current_agenda: Optional[Agenda] = None
        self.current_act: Optional[Act] = None
        self.current_location: Optional[Location] = None
        self.encounter_deck: Optional[Deck] = None
        self.victory_display: List[Card] = []
        self.chaos_bag = None
        self.ai_player = None
        self.phase: str = ""
        self.round: int = 0
        self.clues_gathered: int = 0
        self.scenario_name: str = ""
        self.scenario_id: str = ""
        self.action_log: List[str] = []
        self.servant_of_flame_defeated: bool = False

    def add_investigator(self, investigator: Investigator):
        """Add an investigator to the game."""
        self.investigators.append(investigator)

    def get_investigator(self, investigator_id: str) -> Optional[Investigator]:
        """Get an investigator by ID."""
        for inv in self.investigators:
            if inv.id == investigator_id:
                return inv
        return None

    def get_all_investigators(self) -> List[Investigator]:
        """Get all investigators."""
        return self.investigators
