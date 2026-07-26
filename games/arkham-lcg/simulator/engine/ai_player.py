from typing import Optional, List
from dataclasses import dataclass
from .models import Investigator, Card, GameState, Action


class AIPlayer:
    """AI player for automated game simulation with priority-based decision making."""

    def choose_action(self, investigator: Investigator, game_state: GameState) -> Optional[Action]:
        """Choose the best action for the investigator based on priority."""

        # Priority 1: Fight engaged enemies (they attack every round!)
        for enemy in investigator.engaged_enemies:
            if not enemy.exhausted:
                weapon = self._find_weapon(investigator)
                return FightAction(enemy, weapon)

        # Priority 2: Investigate if we need clues
        if game_state.current_act and game_state.current_act.clues_needed > 0:
            if game_state.current_location:
                return InvestigateAction(game_state.current_location)

        # Priority 3: Play assets if we can afford them
        for card in investigator.hand:
            if card.type.value == "asset" and card.cost <= investigator.resources:
                if card.slot:
                    slot_key = card.slot.value if hasattr(card.slot, 'value') else str(card.slot)
                    if investigator.asset_slots.get(slot_key) is None:
                        return PlayCardAction(card)
                else:
                    return PlayCardAction(card)

        # Priority 4: Investigate even if we don't need clues (for resources via cards)
        if game_state.current_location:
            return InvestigateAction(game_state.current_location)

        return None

    def _find_weapon(self, investigator: Investigator) -> Optional[Card]:
        """Find a weapon in play area."""
        for asset in investigator.play_area:
            if hasattr(asset, 'keywords') and any(
                kw.lower() in ["weapon", "melee"]
                for kw in (asset.keywords if isinstance(asset.keywords, list) else [asset.keywords])
            ):
                return asset
        return None

    def choose_commited_cards(self, investigator: Investigator, skill: str) -> List[Card]:
        """Choose cards to commit to a skill test."""
        committed = []
        for card in investigator.hand:
            if len(committed) >= 2:
                break
            if card.type.value == "skill":
                committed.append(card)
            elif hasattr(card, 'icons'):
                if skill == "willpower" and card.icons.willpower > 0:
                    committed.append(card)
                elif skill == "intellect" and card.icons.intellect > 0:
                    committed.append(card)
                elif skill == "combat" and card.icons.combat > 0:
                    committed.append(card)
                elif skill == "agility" and card.icons.agility > 0:
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
        # Remove defeated enemies
        if self.enemy.is_defeated():
            if self.enemy in investigator.engaged_enemies:
                investigator.engaged_enemies.remove(self.enemy)
            if self.enemy in game_state.enemies:
                game_state.enemies.remove(self.enemy)
            investigator.victory_points += getattr(self.enemy, 'victory', 0)


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
            clues = min(2, self.location.current_clues)
            self.location.current_clues -= clues
            game_state.clues_gathered += clues
            game_state.action_log.append(
                f"{investigator.name} investigates {self.location.name}: {result} (+{clues} clues, {self.location.current_clues} remaining)"
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
            game_state.action_log.append(f"{investigator.name} plays {self.card.name}")
