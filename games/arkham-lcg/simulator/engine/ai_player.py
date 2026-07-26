from typing import Optional, List
from dataclasses import dataclass
from .models import Investigator, Card, GameState, Action


class AIPlayer:
    """AI player for automated game simulation."""

    def choose_action(self, investigator: Investigator, game_state: GameState) -> Optional[Action]:
        """Choose the best action for the investigator."""
        # Priority-based decision making

        # 1. Fight engaged enemies if low health
        if investigator.health <= investigator.health_max // 2:
            for enemy in investigator.engaged_enemies:
                if not enemy.exhausted:
                    return FightAction(enemy)

        # 2. Investigate for clues if no enemies and we need them
        if not investigator.engaged_enemies:
            # Check if we need clues
            if game_state.current_act:
                clues_needed = game_state.current_act.clues_needed
                if clues_needed > 0:
                    return InvestigateAction(game_state.current_location)

        # 3. Play assets from hand if we have resources
        for card in investigator.hand:
            if card.type.value == "asset" and card.cost <= investigator.resources:
                if card.slot:
                    # Check if slot is available
                    if card.slot not in investigator.asset_slots or investigator.asset_slots[card.slot] is None:
                        return PlayCardAction(card)
                else:
                    return PlayCardAction(card)

        # 4. Fight enemies if we have a weapon
        for enemy in investigator.engaged_enemies:
            if not enemy.exhausted:
                weapon = self._find_weapon(investigator)
                if weapon:
                    return FightAction(enemy, weapon)

        # 5. Evade if we're exhausted
        if investigator.engaged_enemies:
            return EvadeAction(investigator.engaged_enemies[0])

        # 6. Fight basic attack
        for enemy in investigator.engaged_enemies:
            if not enemy.exhausted:
                return FightAction(enemy)

        # 7. Investigate
        return InvestigateAction(game_state.current_location)

    def _find_weapon(self, investigator: Investigator) -> Optional[Card]:
        """Find a weapon in play area."""
        for asset in investigator.play_area:
            if "weapon" in asset.traits.lower():
                return asset
        return None

    def choose_commited_cards(self, investigator: Investigator, skill: str) -> List[Card]:
        """Choose cards to commit to a skill test."""
        committed = []
        for card in investigator.hand:
            if len(committed) >= 2:  # Max 2 cards committed
                break
            if card.type.value == "skill":
                committed.append(card)
            elif card.icons.has_icon(skill):
                committed.append(card)
        return committed


@dataclass
class FightAction:
    enemy: Card
    weapon: Optional[Card] = None

    def execute(self, investigator: Investigator, game_state: GameState):
        from .combat import CombatResolver
        combat = CombatResolver()
        result = combat.fight(
            investigator,
            self.enemy,
            game_state.chaos_bag,
            weapon=self.weapon
        )
        game_state.action_log.append(f"{investigator.name} fights {self.enemy.name}: {result}")


@dataclass
class EvadeAction:
    enemy: Card

    def execute(self, investigator: Investigator, game_state: GameState):
        from .combat import CombatResolver
        combat = CombatResolver()
        result = combat.evade(
            investigator,
            self.enemy,
            game_state.chaos_bag
        )
        game_state.action_log.append(f"{investigator.name} evades {self.enemy.name}: {result}")


@dataclass
class InvestigateAction:
    location: 'Location'

    def execute(self, investigator: Investigator, game_state: GameState):
        from .skill_test import SkillTestResolver
        resolver = SkillTestResolver()
        result = resolver.resolve(
            investigator,
            "intellect",
            self.location.shroud,
            game_state.chaos_bag
        )
        if result.success:
            clues = min(2, self.location.clues)
            self.location.clues -= clues
            game_state.clues_gathered += clues
            game_state.action_log.append(
                f"{investigator.name} investigates {self.location.name}: {result} "
                f"(+{clues} clues)"
            )
        else:
            game_state.action_log.append(
                f"{investigator.name} investigates {self.location.name}: {result}"
            )


@dataclass
class PlayCardAction:
    card: Card

    def execute(self, investigator: Investigator, game_state: GameState):
        if self.card.cost <= investigator.resources:
            investigator.spend_resource(self.card.cost)
            investigator.play_card(self.card)
            game_state.action_log.append(
                f"{investigator.name} plays {self.card.name}"
            )
