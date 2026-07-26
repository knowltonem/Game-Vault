from typing import List, Optional
from .models import Investigator, Enemy, Card, Location
from .combat import CombatResolver
from .chaos_bag import ChaosBag
from .skill_test import SkillTestResolver


class MythosPhase:
    def execute(self, game_state):
        """Each investigator draws 1 encounter card. Place 1 doom on agenda."""
        # Place doom on agenda
        if game_state.current_agenda:
            game_state.current_agenda.add_doom(1)

        # Each investigator draws encounter card
        for inv in game_state.investigators:
            if inv.is_defeated():
                continue

            # Investigator ability triggers (Abel: add bless + heal)
            if inv.ability_trigger == "start_of_mythos" and not inv.ability_used_this_round:
                self._resolve_investigator_ability(inv, game_state)

            # Draw encounter card
            if game_state.encounter_deck:
                card = game_state.encounter_deck.draw()
                if card:
                    self._resolve_encounter_card(inv, card, game_state)

    def _resolve_investigator_ability(self, inv: Investigator, game_state):
        """Resolve investigator-specific abilities."""
        if inv.id == "abel_redcloud":
            game_state.chaos_bag.add_bless(1)
            inv.bless_tokens_added += 1
            inv.heal_damage(1)

    def _resolve_encounter_card(self, inv: Investigator, card: Card, game_state):
        """Resolve an encounter card based on its type and name."""
        if card.type.value == "treachery":
            self._resolve_treachery(inv, card, game_state)
        elif card.type.value == "enemy":
            self._resolve_enemy_encounter(inv, card, game_state)

    def _resolve_treachery(self, inv: Investigator, card: Card, game_state):
        """Resolve a treachery card by name."""
        name = card.name.lower().strip()

        if name == "fire!":
            for asset in list(inv.play_area):
                if asset.health:
                    asset.health -= 1
                    if asset.health <= 0:
                        inv.discard_card(asset)
            resolver = SkillTestResolver()
            result = resolver.resolve(inv, "agility", 3, game_state.chaos_bag)
            if not result.success:
                inv.take_damage(1, source="Fire!")

        elif name == "cosmic evils":
            # AI choice: place doom is better than damage+horror
            game_state.current_agenda.add_doom(1)

        elif name == "caught in a lie":
            resolver = SkillTestResolver()
            result = resolver.resolve(inv, "willpower", 2, game_state.chaos_bag)
            if not result.success:
                inv.take_horror(1, source="Caught in a Lie")

        elif name == "dark machinations":
            resolver = SkillTestResolver()
            result = resolver.resolve(inv, "willpower", 3, game_state.chaos_bag)
            if not result.success:
                inv.take_damage(1, source="Dark Machinations")
                inv.take_horror(1, source="Dark Machinations")

        elif name == "disorienting fear":
            resolver = SkillTestResolver()
            result = resolver.resolve(inv, "willpower", 2, game_state.chaos_bag)
            if not result.success:
                inv.take_horror(1, source="Disorienting Fear")

        else:
            # Unknown treachery: test willpower 2, fail = 1 horror
            resolver = SkillTestResolver()
            result = resolver.resolve(inv, "willpower", 2, game_state.chaos_bag)
            if not result.success:
                inv.take_horror(1, source=card.name)

    def _resolve_enemy_encounter(self, inv: Investigator, card: Card, game_state):
        """Resolve an enemy encounter card - spawn enemy engaged with investigator."""
        enemy = Enemy(
            id=f"{card.id}_{inv.id}_{game_state.round}",
            name=card.name,
            type=card.type,
            fight=card.fight,
            evade=card.evade,
            health=card.health,
            current_health=card.health,
            damage=card.damage,
            horror=card.horror,
            traits=card.traits,
            keywords=card.keywords
        )
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
                if inv.actions <= 0:
                    break
                action = game_state.ai_player.choose_action(inv, game_state)
                if action:
                    action.execute(inv, game_state)
                    inv.actions -= 1
                else:
                    break


class EnemyPhase:
    def execute(self, game_state):
        """Engaged non-exhausted enemies attack investigators."""
        for inv in game_state.investigators:
            if inv.is_defeated():
                continue
            for enemy in list(inv.engaged_enemies):
                if not enemy.exhausted:
                    combat = CombatResolver()
                    combat.enemy_attack(enemy, inv)

        # Ready exhausted enemies
        for enemy in game_state.enemies:
            if enemy.exhausted:
                enemy.ready()


class UpkeepPhase:
    def execute(self, game_state):
        """Ready all cards. Draw 1 card, gain 1 resource."""
        for inv in game_state.investigators:
            if inv.is_defeated():
                continue

            inv.ready_all()
            inv.draw_card()
            inv.gain_resource()
            inv.ability_used_this_round = False
