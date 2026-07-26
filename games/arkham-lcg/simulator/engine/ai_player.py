from typing import Optional, List
from dataclasses import dataclass
from .models import Investigator, Card, GameState, Action, Location
from .phases import log


class AIPlayer:
    """AI player for automated game simulation with priority-based decision making."""

    def choose_action(self, investigator: Investigator, game_state: GameState) -> Optional[Action]:
        """Choose the best action for the investigator based on priority."""

        has_engaged_enemy = any(not e.exhausted for e in investigator.engaged_enemies)
        weapon_in_play = self._find_weapon(investigator) is not None
        affordable_weapon_in_hand = self._find_affordable_weapon(investigator) is not None

        # Priority 1: Play weapon if enemy engaged and no weapon in play yet
        if has_engaged_enemy and affordable_weapon_in_hand and not weapon_in_play:
            weapon = self._find_affordable_weapon(investigator)
            return PlayCardAction(weapon)

        # Priority 2: Play defensive assets if enemy engaged and no soak in play
        if has_engaged_enemy:
            soak_in_play = any(
                getattr(c, 'health', None) or getattr(c, 'sanity', None)
                for c in investigator.play_area
            )
            if not soak_in_play:
                card = self._find_affordable_soak(investigator)
                if card:
                    return PlayCardAction(card)

        # Priority 3: Fight engaged enemies (they attack every round!)
        for enemy in investigator.engaged_enemies:
            if not enemy.exhausted:
                weapon = self._find_weapon(investigator)
                return FightAction(enemy, weapon)

        # Priority 4: Investigate if current location has clues
        if game_state.current_location and game_state.current_location.current_clues > 0:
            return InvestigateAction(game_state.current_location)

        # Priority 5: Move to a connected location with clues
        if game_state.current_location:
            best_loc = self._find_best_location(game_state)
            if best_loc:
                return MoveAction(best_loc)

        # Priority 6: Play remaining useful assets (only affordable, only if slot open)
        card = self._find_affordable_asset_for_open_slot(investigator)
        if card:
            return PlayCardAction(card)

        return None

    def _find_affordable_weapon(self, investigator: Investigator) -> Optional[Card]:
        """Find an affordable weapon card in hand."""
        for card in investigator.hand:
            if card.type.value != "asset":
                continue
            if card.cost > investigator.resources:
                continue
            if card.has_keyword("weapon") or card.has_keyword("melee"):
                return card
            if "+1 <com>" in card.text or "+2 <com>" in card.text:
                return card
        return None

    def _find_affordable_soak(self, investigator: Investigator) -> Optional[Card]:
        """Find an affordable soak asset in hand."""
        for card in investigator.hand:
            if card.type.value != "asset":
                continue
            if card.cost > investigator.resources:
                continue
            if getattr(card, 'health', None) or getattr(card, 'sanity', None):
                return card
        return None

    def _find_affordable_asset_for_open_slot(self, investigator: Investigator) -> Optional[Card]:
        """Find an affordable asset that fits an open slot."""
        for card in investigator.hand:
            if card.type.value != "asset":
                continue
            if card.cost > investigator.resources:
                continue
            if card.slot:
                slot_key = card.slot.value if hasattr(card.slot, 'value') else str(card.slot)
                if investigator.asset_slots.get(slot_key) is None:
                    return card
            else:
                return card
        return None

    def _find_weapon(self, investigator: Investigator) -> Optional[Card]:
        for asset in investigator.play_area:
            if asset.has_keyword("weapon") or asset.has_keyword("melee"):
                return asset
            if "+1 <com>" in asset.text or "+2 <com>" in asset.text:
                return asset
        return None

    def _find_best_location(self, game_state: GameState) -> Optional[Location]:
        current = game_state.current_location
        if not current:
            return None
        best = None
        best_clues = 0
        for loc in game_state.locations:
            if loc.id in current.connections and loc.current_clues > best_clues:
                best = loc
                best_clues = loc.current_clues
        return best

    def choose_commited_cards(self, investigator: Investigator, skill: str) -> List[Card]:
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
        weapon_name = self.weapon.name if self.weapon else 'bare hands'
        log(f'    {investigator.name} fights {self.enemy.name} (F{self.enemy.fight} HP{self.enemy.current_health}) with {weapon_name}')

        result = combat.fight(
            investigator,
            self.enemy,
            game_state.chaos_bag,
            weapon=self.weapon
        )
        log(f'      Base: {result.test_result.base_value} + Token: {result.test_result.token} ({result.test_result.modifier:+d}) = {result.test_result.final_value} vs {result.test_result.difficulty} -> {"HIT" if result.test_result.success else "MISS"}')
        if result.test_result.success:
            log(f'      {self.enemy.name} takes {result.damage_dealt} damage (HP {self.enemy.current_health}/{getattr(self.enemy, "health", "?")})')
        if result.enemy_defeated:
            log(f'      *** {self.enemy.name} DEFEATED ***')
            if self.enemy in investigator.engaged_enemies:
                investigator.engaged_enemies.remove(self.enemy)
            if self.enemy in game_state.enemies:
                game_state.enemies.remove(self.enemy)
            investigator.victory_points += getattr(self.enemy, 'victory', 0)
            if self.enemy.name == "Servant of Flame":
                game_state.servant_of_flame_defeated = True
                log(f'      *** SERVANT OF FLAME DEFEATED — VICTORY! ***')
        elif result.retaliation:
            log(f'      Retaliation! {self.enemy.name} attacks back')


@dataclass
class EvadeAction:
    enemy: Card

    def execute(self, investigator: Investigator, game_state: GameState):
        from .combat import CombatResolver
        combat = CombatResolver()
        log(f'    {investigator.name} evades {self.enemy.name} (E{self.enemy.evade})')
        result = combat.evade(investigator, self.enemy, game_state.chaos_bag)
        log(f'      Base: {result.test_result.base_value} + Token: {result.test_result.token} ({result.test_result.modifier:+d}) = {result.test_result.final_value} vs {result.test_result.difficulty} -> {"ESCAPED" if result.test_result.success else "CAUGHT"}')
        if result.test_result.success:
            log(f'      {self.enemy.name} exhausted and disengaged')


@dataclass
class MoveAction:
    destination: Location

    def execute(self, investigator: Investigator, game_state: GameState):
        old_location = game_state.current_location
        game_state.current_location = self.destination
        log(f'    {investigator.name} moves: {old_location.name} -> {self.destination.name} (Shroud {self.destination.shroud}, {self.destination.current_clues} clues)')


@dataclass
class InvestigateAction:
    location: 'Location'

    def execute(self, investigator: Investigator, game_state: GameState):
        from .skill_test import SkillTestResolver
        resolver = SkillTestResolver()
        log(f'    {investigator.name} investigates {self.location.name} (Shroud {self.location.shroud}, {self.location.current_clues} clues remaining)')

        result = resolver.resolve(
            investigator,
            "intellect",
            self.location.shroud,
            game_state.chaos_bag
        )
        log(f'      Base: {result.base_value} + Token: {result.token} ({result.modifier:+d}) = {result.final_value} vs {result.difficulty} -> {"SUCCESS" if result.success else "FAILURE"}')

        if result.success:
            clues = min(2, self.location.current_clues)
            self.location.current_clues -= clues
            game_state.clues_gathered += clues
            log(f'      Discovered {clues} clue(s) ({self.location.current_clues} remaining at location, {game_state.clues_gathered} total)')
        else:
            log(f'      No clues discovered')


@dataclass
class PlayCardAction:
    card: Card

    def execute(self, investigator: Investigator, game_state: GameState):
        if self.card.cost <= investigator.resources:
            log(f'    {investigator.name} plays [{self.card.name}] ({self.card.type.value}, cost {self.card.cost}r)')
            investigator.spend_resource(self.card.cost)
            log(f'      Resources: {investigator.resources + self.card.cost} -> {investigator.resources}')
            investigator.play_card(self.card)
            if self.card.is_asset():
                slot_info = f' [{self.card.slot}]' if self.card.slot else ''
                log(f'      {self.card.name} enters play{slot_info}')
