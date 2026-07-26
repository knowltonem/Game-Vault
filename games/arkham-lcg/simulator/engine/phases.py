from typing import List, Optional
from .models import Investigator, Enemy, Card, Location
from .combat import CombatResolver
from .chaos_bag import ChaosBag
from .skill_test import SkillTestResolver


class MythosPhase:
    def execute(self, game_state):
        """Each investigator draws 1 encounter card. Place 1 doom on agenda."""
        # Place doom on agenda
        game_state.current_agenda.add_doom(1)

        # Each investigator draws encounter card
        for inv in game_state.investigators:
            if inv.is_defeated():
                continue

            # Investigator ability triggers (Abel: add bless + heal)
            if inv.ability_trigger == "start_of_mythos" and not inv.ability_used_this_round:
                self._resolve_investigator_ability(inv, game_state)

            # Draw encounter card
            card = game_state.encounter_deck.draw()
            if card:
                self._resolve_encounter_card(inv, card, game_state)

    def _resolve_investigator_ability(self, inv: Investigator, game_state):
        """Resolve investigator-specific ability."""
        if inv.id == "abel_redcloud":
            # Add 1 bless token
            game_state.chaos_bag.add_bless(1)
            inv.bless_tokens_added += 1
            # Heal 1 damage
            inv.heal_damage(1)

    def _resolve_encounter_card(self, inv: Investigator, card: Card, game_state):
        """Resolve an encounter card."""
        # Simple encounter resolution for now
        if card.type.value == "treachery":
            self._resolve_treachery(inv, card, game_state)
        elif card.type.value == "enemy":
            self._resolve_enemy_encounter(inv, card, game_state)

    def _resolve_treachery(self, inv: Investigator, card: Card, game_state):
        """Resolve a treachery card."""
        # Fire! treachery
        if card.name == "Fire!":
            # Deal 1 damage to each card with health
            for asset in inv.play_area:
                if asset.health:
                    asset.health -= 1
                    if asset.health <= 0:
                        inv.discard_card(asset)
            # Test Agility 3
            resolver = SkillTestResolver()
            result = resolver.resolve(inv, "agility", 3, game_state.chaos_bag)
            if not result.success:
                # Fire! stays in play - simplified: take 1 damage
                inv.take_damage(1, source="Fire!")

        # Cosmic Evils
        elif card.name == "Cosmic Evils":
            # Choose: place 1 doom on agenda OR each investigator takes 1 damage, 1 horror
            # AI chooses to place doom on agenda
            game_state.current_agenda.add_doom(1)

        # Default: take 1 damage and 1 horror
        else:
            inv.take_damage(1, source=card.name)
            inv.take_horror(1, source=card.name)

    def _resolve_enemy_encounter(self, inv: Investigator, card: Card, game_state):
        """Resolve an enemy encounter card."""
        # Create enemy instance
        enemy = Enemy(
            id=card.id,
            name=card.name,
            type=card.type,
            fight=card.fight,
            evade=card.evade,
            health=card.health,
            damage=card.damage,
            horror=card.horror,
            traits=card.traits,
            keywords=card.keywords,
            current_health=card.health
        )
        # Spawn at investigator's location
        enemy.engaged_with = inv.id
        inv.engaged_enemies.append(enemy)
        game_state.enemies.append(enemy)


class InvestigationPhase:
    def execute(self, game_state):
        """Investigators take turns, 3 actions each."""
        for inv in game_state.investigators:
            if inv.is_defeated():
                continue

            for _ in range(3):
                action = game_state.ai_player.choose_action(inv, game_state)
                if action:
                    action.execute(inv, game_state)
                else:
                    break  # No more actions available


class EnemyPhase:
    def execute(self, game_state):
        """Ready enemies move toward investigators (Hunter). Engaged enemies attack."""
        # 1. Ready enemies, move hunters
        for enemy in game_state.enemies:
            if not enemy.exhausted:
                if "Hunter" in enemy.keywords:
                    self._move_hunter(enemy, game_state)

        # 2. Engaged enemies attack
        for inv in game_state.investigators:
            if inv.is_defeated():
                continue
            for enemy in list(inv.engaged_enemies):
                if not enemy.exhausted:
                    combat = CombatResolver()
                    combat.enemy_attack(enemy, inv)

    def _move_hunter(self, enemy: Enemy, game_state):
        """Move hunter enemy toward its prey."""
        if not enemy.engaged_with:
            # Find closest investigator
            for inv in game_state.investigators:
                if not inv.is_defeated():
                    enemy.engaged_with = inv.id
                    inv.engaged_enemies.append(enemy)
                    break


class UpkeepPhase:
    def execute(self, game_state):
        """Ready all cards. Draw 1 card, gain 1 resource. Gain 3 actions."""
        for inv in game_state.investigators:
            if inv.is_defeated():
                continue

            # Ready all exhausted cards
            inv.ready_all()

            # Draw 1 card
            inv.draw_card()

            # Gain 1 resource
            inv.gain_resource()

            # Reset ability tracking
            inv.ability_used_this_round = False
