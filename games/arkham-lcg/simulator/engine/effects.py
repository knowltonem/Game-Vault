from typing import Dict, List, Optional
from dataclasses import dataclass
from .models import Card, Investigator, GameState


@dataclass
class CardEffect:
    """Represents a card effect."""
    trigger: str  # "on_play", "on_fight", "on_investigate", "forced", "reaction"
    condition: Optional[str] = None
    cost: Optional[str] = None
    effect_type: str = ""  # "damage", "heal", "draw", "gain_resource", "add_bless"
    value: int = 0
    target: str = ""  # "self", "enemy", "location", "each_investigator"
    text: str = ""


class EffectsEngine:
    """Processes card effects and triggers."""

    def __init__(self):
        self.effects_db: Dict[str, List[CardEffect]] = {}

    def load_card_effects(self, card_id: str, effects: List[CardEffect]):
        """Load effects for a card."""
        self.effects_db[card_id] = effects

    def process_trigger(self, trigger: str, investigator: Investigator,
                       game_state: GameState, **kwargs) -> List[str]:
        """
        Process all effects triggered by an event.

        Args:
            trigger: The trigger type
            investigator: The investigator involved
            game_state: Current game state
            **kwargs: Additional context

        Returns:
            List of effect descriptions
        """
        results = []

        # Check investigator ability
        if investigator.ability_trigger == trigger:
            result = self._process_investigator_ability(investigator, game_state)
            if result:
                results.append(result)

        # Check hand cards
        for card in investigator.hand:
            if card.id in self.effects_db:
                for effect in self.effects_db[card.id]:
                    if effect.trigger == trigger:
                        result = self._process_effect(effect, investigator, game_state, **kwargs)
                        if result:
                            results.append(result)

        # Check play area cards
        for card in investigator.play_area:
            if card.id in self.effects_db:
                for effect in self.effects_db[card.id]:
                    if effect.trigger == trigger:
                        result = self._process_effect(effect, investigator, game_state, **kwargs)
                        if result:
                            results.append(result)

        return results

    def _process_investigator_ability(self, investigator: Investigator,
                                      game_state: GameState) -> Optional[str]:
        """Process investigator-specific abilities."""
        if investigator.id == "abel_redcloud":
            if investigator.ability_trigger == "start_of_mythos":
                # Add 1 bless token
                game_state.chaos_bag.add_bless(1)
                # Heal 1 damage
                investigator.heal_damage(1)
                return f"{investigator.name}: Added 1 bless token and healed 1 damage"

        elif investigator.id == "nora_warwick":
            if investigator.ability_trigger == "action":
                if investigator.resources >= 1:
                    investigator.spend_resource(1)
                    game_state.chaos_bag.add_bless(1)
                    return f"{investigator.name}: Spent 1 resource to add 1 bless token"

        return None

    def _process_effect(self, effect: CardEffect, investigator: Investigator,
                       game_state: GameState, **kwargs) -> Optional[str]:
        """Process a single card effect."""
        # Check condition
        if effect.condition:
            if not self._check_condition(effect.condition, investigator, game_state, **kwargs):
                return None

        # Check cost
        if effect.cost:
            if not self._pay_cost(effect.cost, investigator, game_state):
                return None

        # Apply effect
        if effect.effect_type == "damage":
            target = kwargs.get("target")
            if target:
                target.take_damage(effect.value, source="card_effect")
                return f"Dealt {effect.value} damage to {target.name}"

        elif effect.effect_type == "heal":
            investigator.heal_damage(effect.value)
            return f"Healed {effect.value} damage"

        elif effect.effect_type == "draw":
            for _ in range(effect.value):
                investigator.draw_card()
            return f"Drew {effect.value} cards"

        elif effect.effect_type == "gain_resource":
            investigator.gain_resource(effect.value)
            return f"Gained {effect.value} resources"

        elif effect.effect_type == "add_bless":
            game_state.chaos_bag.add_bless(effect.value)
            return f"Added {effect.value} bless tokens"

        elif effect.effect_type == "add_curse":
            game_state.chaos_bag.add_curse(effect.value)
            return f"Added {effect.value} curse tokens"

        return None

    def _check_condition(self, condition: str, investigator: Investigator,
                        game_state: GameState, **kwargs) -> bool:
        """Check if a condition is met."""
        if condition == "has_weapon":
            return any("weapon" in card.traits.lower() for card in investigator.play_area)
        elif condition == "engaged_with_enemy":
            return len(investigator.engaged_enemies) > 0
        elif condition == "health_low":
            return investigator.health <= investigator.health_max // 2
        return True

    def _pay_cost(self, cost: str, investigator: Investigator,
                  game_state: GameState) -> bool:
        """Pay a cost. Returns True if cost was paid."""
        if cost.startswith("resource_"):
            amount = int(cost.split("_")[1])
            if investigator.resources >= amount:
                investigator.spend_resource(amount)
                return True
            return False
        elif cost == "damage":
            if investigator.health > 0:
                investigator.take_damage(1, source="cost")
                return True
            return False
        return True
