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
    sanity: Optional[int] = None
    uses: Optional[int] = None
    uses_type: str = ""  # charges, ammo, supplies
    keywords: List[str] = field(default_factory=list)

    def is_asset(self) -> bool:
        return self.type == CardType.ASSET

    def is_event(self) -> bool:
        return self.type == CardType.EVENT

    def is_skill(self) -> bool:
        return self.type == CardType.SKILL

    def has_uses(self) -> bool:
        return self.uses is not None and self.uses > 0

    def spend_use(self) -> bool:
        if self.has_uses():
            self.uses -= 1
            return True
        return False


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

    def spend_clues(self, amount: int) -> bool:
        if self.clues_spent + amount >= self.clue_threshold:
            return True
        self.clues_spent += amount
        return False


@dataclass
class Investigator:
    id: str
    name: str
    subtitle: str
    card_class: str
    traits: List[str]
    stats: Dict[str, int]  # willpower, intellect, combat, agility
    health: int
    sanity: int
    deck_size: int
    ability_text: str = ""
    ability_trigger: str = ""  # start_of_mythos, once_per_round, etc.
    elder_sign_text: str = ""
    elder_sign_modifier: int = 1
    auto_fail_text: str = ""
    cultist_text: str = ""

    # Game state
    current_health: int = 0
    current_sanity: int = 0
    resources: int = 0
    actions: int = 3
    hand: List[Card] = field(default_factory=list)
    deck: List[Card] = field(default_factory=list)
    discard: List[Card] = field(default_factory=list)
    play_area: List[Card] = field(default_factory=list)
    engaged_enemies: List[Enemy] = field(default_factory=list)
    location: Optional[str] = None
    defeated: bool = False
    resigned: bool = False
    clues: int = 0
    trauma_damage: int = 0
    trauma_horror: int = 0

    # Slot tracking
    slots: Dict[Slot, Optional[Card]] = field(default_factory=dict)

    # Signature cards
    signatures: List[str] = field(default_factory=list)
    set_aside: List[str] = field(default_factory=list)

    # Ability tracking
    ability_used_this_round: bool = False
    bless_tokens_added: int = 0

    def __post_init__(self):
        if self.current_health == 0:
            self.current_health = self.health
        if self.current_sanity == 0:
            self.current_sanity = self.sanity
        # Initialize slots
        if not self.slots:
            self.slots = {slot: None for slot in Slot}

    def get_stat(self, skill: str) -> int:
        base = self.stats.get(skill, 0)
        # Add bonuses from assets in play
        for card in self.play_area:
            if card.is_asset():
                if skill == "willpower" and "+1 <wil>" in card.text:
                    base += 1
                elif skill == "intellect" and "+1 <int>" in card.text:
                    base += 1
                elif skill == "combat" and "+1 <com>" in card.text:
                    base += 1
                elif skill == "agility" and "+1 <agi>" in card.text:
                    base += 1
        return base

    def draw_card(self) -> Optional[Card]:
        if not self.deck:
            # Shuffle discard into deck
            if self.discard:
                self.deck = self.discard.copy()
                self.discard.clear()
                random.shuffle(self.deck)
            else:
                return None
        if self.deck:
            card = self.deck.pop(0)
            self.hand.append(card)
            return card
        return None

    def draw_hand(self, count: int):
        for _ in range(count):
            self.draw_card()

    def gain_resource(self, amount: int = 1):
        self.resources += amount

    def spend_resource(self, amount: int) -> bool:
        if self.resources >= amount:
            self.resources -= amount
            return True
        return False

    def take_damage(self, amount: int, source: str = "") -> bool:
        self.current_health -= amount
        if self.current_health <= 0:
            self.current_health = 0
            self.defeated = True
        return self.defeated

    def take_horror(self, amount: int, source: str = "") -> bool:
        self.current_sanity -= amount
        if self.current_sanity <= 0:
            self.current_sanity = 0
            self.defeated = True
        return self.defeated

    def heal_damage(self, amount: int):
        self.current_health = min(self.current_health + amount, self.health)

    def heal_horror(self, amount: int):
        self.current_sanity = min(self.current_sanity + amount, self.sanity)

    def is_defeated(self) -> bool:
        return self.defeated or self.current_health <= 0 or self.current_sanity <= 0

    def ready_all(self):
        self.actions = 3
        self.ability_used_this_round = False
        for card in self.play_area:
            if hasattr(card, 'exhausted'):
                card.exhausted = False

    def play_card(self, card: Card) -> bool:
        if card.cost > self.resources:
            return False
        self.spend_resource(card.cost)
        self.hand.remove(card)
        if card.is_asset():
            self.play_area.append(card)
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
