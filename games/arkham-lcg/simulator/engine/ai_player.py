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
        enemies_on_board = len(game_state.enemies) > 0

        # Priority 1: Play weapon proactively (combat investigator or enemy engaged)
        if affordable_weapon_in_hand and not weapon_in_play:
            if has_engaged_enemy or investigator.combat >= 3:
                weapon = self._find_affordable_weapon(investigator)
                return PlayCardAction(weapon)

        # Priority 2: Play defensive soak if enemies exist and no soak in play
        if has_engaged_enemy or enemies_on_board:
            soak_in_play = any(
                getattr(c, 'health', None) or getattr(c, 'sanity', None)
                for c in investigator.play_area
            )
            if not soak_in_play:
                card = self._find_affordable_soak(investigator)
                if card:
                    return PlayCardAction(card)

        # Priority 3: Play fast events that are always useful
        fast_event = self._find_useful_fast_event(investigator, game_state)
        if fast_event:
            return PlayCardAction(fast_event)

        # Priority 4: Fight engaged enemies (they attack every round!)
        for enemy in investigator.engaged_enemies:
            if not enemy.exhausted:
                # Abel cannot take actions against the Wendigo
                if investigator.id == "abel_redcloud" and enemy.name == "Wendigo":
                    continue
                # Eleanor Heart cannot fight (COM1) - she should evade instead
                if investigator.id == "eleanor_heart":
                    continue
                weapon = self._find_weapon(investigator)
                return FightAction(enemy, weapon)

        # Priority 4b: Evade engaged enemies if can't fight
        if investigator.id == "eleanor_heart":
            for enemy in investigator.engaged_enemies:
                if not enemy.exhausted:
                    return EvadeAction(enemy)

        # Priority 4c: Use asset action abilities (heal allies, etc.)
        heal_action = self._find_heal_action(investigator, game_state)
        if heal_action:
            return heal_action

        # Priority 5: Investigate if current location has clues
        if game_state.current_location and game_state.current_location.current_clues > 0:
            return InvestigateAction(game_state.current_location)

        # Priority 6: Play resource-generating events if low on resources
        if investigator.resources < 5:
            resource_event = self._find_resource_event(investigator)
            if resource_event:
                return PlayCardAction(resource_event)

        # Priority 7: Play card-draw events if hand is small
        if len(investigator.hand) < 5:
            draw_event = self._find_draw_event(investigator)
            if draw_event:
                return PlayCardAction(draw_event)

        # Priority 8: Move to a connected location with clues
        if game_state.current_location:
            best_loc = self._find_best_location(game_state)
            if best_loc:
                return MoveAction(best_loc)

        # Priority 9: Play remaining useful assets (only affordable, only if slot open)
        card = self._find_affordable_asset_for_open_slot(investigator)
        if card:
            return PlayCardAction(card)

        return None

    def _find_useful_fast_event(self, investigator: Investigator, game_state: GameState) -> Optional[Card]:
        """Find fast events that should be played immediately."""
        # Check if saving for a weapon — skip cost > 0 events
        weapon_save_cost = self._find_weapon_save_cost(investigator)

        for card in investigator.hand:
            if card.type.value != "event":
                continue
            if card.cost > investigator.resources:
                continue
            # If saving for a weapon, skip events that cost resources
            if weapon_save_cost > 0 and card.cost > 0:
                continue
            text = card.text.lower()
            
            # Gain resources free (Cash Flow, Special Allowance)
            if card.cost == 0 and "gain" in text and "resource" in text:
                return card
            
            # Draw cards free (Military Tactics, Up The Sleeve, Informant)
            if card.cost == 0 and "draw" in text and "card" in text:
                return card
            
            # Discover clues fast (Working a Hunch, The Codex Revealed)
            if "fast" in text and "discover" in text and "clue" in text:
                if game_state.current_location and game_state.current_location.current_clues > 0:
                    return card
            
            # Heal horror/damage (Clarity of Mind, Patch Up) — only if someone is hurt
            if "heal" in text and ("horror" in text or "damage" in text):
                for inv in game_state.investigators:
                    if not inv.is_defeated():
                        if inv.current_health < inv.health or inv.current_sanity < inv.sanity:
                            return card
            
            # Gain resources (non-fast) — only if affordable and saving not needed
            if "gain" in text and "resource" in text:
                return card
        
        return None

    def _find_resource_event(self, investigator: Investigator) -> Optional[Card]:
        """Find events that generate resources."""
        for card in investigator.hand:
            if card.type.value != "event":
                continue
            if card.cost > investigator.resources:
                continue
            text = card.text.lower()
            
            # Cash Flow, Special Allowance, Emergency Caches
            if "gain" in text and "resource" in text and "fast" not in text:
                return card
            
            # River of Gold, Grave Robber
            if "gain 3 resource" in text or "gain 4 resource" in text:
                return card
        
        return None

    def _find_draw_event(self, investigator: Investigator) -> Optional[Card]:
        """Find events that draw cards."""
        for card in investigator.hand:
            if card.type.value != "event":
                continue
            if card.cost > investigator.resources:
                continue
            text = card.text.lower()
            
            # Draw cards (non-fast)
            if "draw" in text and "card" in text and "fast" not in text:
                return card
        
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
            text_lower = card.text.lower()
            if "+1 <com>" in text_lower or "+2 <com>" in text_lower or "+1 com" in text_lower or "+2 com" in text_lower:
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
            text_lower = asset.text.lower()
            if "+1 <com>" in text_lower or "+2 <com>" in text_lower or "+1 com" in text_lower or "+2 com" in text_lower:
                return asset
        return None

    def _find_weapon_save_cost(self, investigator: Investigator) -> int:
        """Return the min additional resources needed to afford a weapon in hand (0 if already affordable, -1 if none)."""
        min_shortfall = -1
        for card in investigator.hand:
            if card.type.value != "asset":
                continue
            text_lower = card.text.lower()
            is_weapon = card.has_keyword("weapon") or card.has_keyword("melee")
            has_com_bonus = "+1 <com>" in text_lower or "+2 <com>" in text_lower or "+1 com" in text_lower or "+2 com" in text_lower
            if is_weapon or has_com_bonus:
                shortfall = card.cost - investigator.resources
                if shortfall <= 0:
                    return 0
                if min_shortfall < 0 or shortfall < min_shortfall:
                    min_shortfall = shortfall
        return min_shortfall

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

    def _find_heal_action(self, investigator: Investigator, game_state: GameState) -> Optional['Action']:
        """Find an asset action ability to heal an injured ally."""
        # Priority: heal the most injured ally
        injured_allies = []
        for inv in game_state.investigators:
            if inv.id == investigator.id:
                continue
            if inv.is_defeated():
                continue
            damage = inv.health - inv.current_health
            horror = inv.sanity - inv.current_sanity
            if damage > 0 or horror > 0:
                injured_allies.append((inv, damage + horror, damage, horror))
        if not injured_allies:
            return None
        # Sort by total damage+horror (most injured first)
        injured_allies.sort(key=lambda x: x[1], reverse=True)
        target, _, _, _ = injured_allies[0]

        # Check for Triage (heal 1 damage, 3 charges)
        for asset in investigator.play_area:
            if asset.name == "Triage" and (asset.current_uses or 0) > 0 and not asset.exhausted:
                if target.current_health < target.health:
                    return UseAssetAbility(asset=asset, target=target)

        # Check for Pray for Me Father (heal 1 horror, 4 supplies)
        for asset in investigator.play_area:
            if asset.name == "Pray for Me Father" and (asset.current_uses or 0) > 0 and not asset.exhausted:
                if target.current_sanity < target.sanity:
                    return UseAssetAbility(asset=asset, target=target)

        # Check for Old Habit (heal 2 damage, exhaust + horror cost)
        for asset in investigator.play_area:
            if asset.name == "Old Habit" and not asset.exhausted:
                if target.current_health < target.health:
                    return UseAssetAbility(asset=asset, target=target)

        return None

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

        # Commit relevant cards from hand
        committed_cards = game_state.ai_player.choose_commited_cards(investigator, "combat")
        if committed_cards:
            log(f'      Committed: {", ".join(c.name for c in committed_cards)}')

        result = combat.fight(
            investigator,
            self.enemy,
            game_state.chaos_bag,
            weapon=self.weapon,
            committed_cards=committed_cards
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

        # Commit relevant cards from hand
        committed_cards = game_state.ai_player.choose_commited_cards(investigator, "intellect")
        if committed_cards:
            log(f'      Committed: {", ".join(c.name for c in committed_cards)}')

        result = resolver.resolve(
            investigator,
            "intellect",
            self.location.shroud,
            game_state.chaos_bag,
            committed_cards=committed_cards
        )
        log(f'      Base: {result.base_value} + Token: {result.token} ({result.modifier:+d}) = {result.final_value} vs {result.difficulty} -> {"SUCCESS" if result.success else "FAILURE"}')

        if result.success:
            clues = min(2, self.location.current_clues)
            self.location.current_clues -= clues
            game_state.clues_gathered += clues
            log(f'      Discovered {clues} clue(s) ({self.location.current_clues} remaining at location, {game_state.clues_gathered} total)')
            # Innsmouth Lessons: gain 1 additional clue on successful investigate
            for asset in investigator.play_area:
                if asset.name == "Innsmouth Lessons" and not asset.exhausted:
                    extra = min(1, self.location.current_clues)
                    if extra > 0:
                        self.location.current_clues -= extra
                        game_state.clues_gathered += extra
                        log(f'      Innsmouth Lessons: +1 additional clue ({self.location.current_clues} remaining, {game_state.clues_gathered} total)')
        else:
            log(f'      No clues discovered')


@dataclass
class PlayCardAction:
    card: Card

    def execute(self, investigator: Investigator, game_state: GameState):
        if self.card.cost <= investigator.resources:
            before = investigator.resources
            result = investigator.play_card(self.card)
            if result:
                log(f'    {investigator.name} plays [{self.card.name}] ({self.card.type.value}, cost {self.card.cost}r)')
                log(f'      Resources: {before} -> {investigator.resources}')
                if self.card.is_asset():
                    slot_info = f' [{self.card.slot}]' if self.card.slot else ''
                    log(f'      {self.card.name} enters play{slot_info}')


@dataclass
class UseAssetAbility:
    """Use an action ability on an asset (Triage, Old Habit, Pray for Me Father, etc.)"""
    asset: Card
    target: Optional[Investigator] = None

    def execute(self, investigator: Investigator, game_state: GameState):
        name = self.asset.name
        target = self.target or investigator

        if name == "Triage" and self.asset.current_uses > 0:
            self.asset.spend_use()
            old_hp = target.current_health
            target.heal_damage(1, healer=investigator)
            log(f'    {investigator.name} uses Triage: heals 1 damage from {target.name} (HP {old_hp} -> {target.current_health}) [{self.asset.current_uses} charges left]')
            self.asset.exhausted = True

        elif name == "Old Habit" and not self.asset.exhausted and investigator.trauma_horror >= 0:
            self.asset.exhausted = True
            old_hp = target.current_health
            target.heal_damage(2, healer=investigator)
            log(f'    {investigator.name} uses Old Habit: heals 2 damage from {target.name} (HP {old_hp} -> {target.current_health})')
            # Old Habit costs 1 horror on investigator
            investigator.take_horror(1, source="Old Habit")

        elif name == "Pray for Me Father" and self.asset.current_uses > 0:
            self.asset.spend_use()
            old_san = target.current_sanity
            target.heal_horror(1, healer=investigator)
            log(f'    {investigator.name} uses Pray for Me Father: heals 1 horror from {target.name} (SAN {old_san} -> {target.current_sanity}) [{self.asset.current_uses} supplies left]')
