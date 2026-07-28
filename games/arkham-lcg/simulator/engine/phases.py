from typing import List, Optional
from .models import Investigator, Enemy, Card, Location


class Logger:
    """Shared game logger."""
    _log_func = None

    @classmethod
    def set_log_func(cls, func):
        cls._log_func = func

    @classmethod
    def log(cls, msg, indent=0):
        if cls._log_func:
            cls._log_func(msg, indent)


def log(msg, indent=0):
    Logger.log(msg, indent)


class MythosPhase:
    def execute(self, game_state):
        """Each investigator draws 1 encounter card. Place 1 doom on agenda."""
        log('')
        log('--- MYTHOS PHASE ---')

        # Place doom on agenda
        if game_state.current_agenda:
            old_doom = game_state.current_agenda.current_doom
            game_state.current_agenda.add_doom(1)
            log(f'Doom placed on {game_state.current_agenda.name}: {old_doom} -> {game_state.current_agenda.current_doom}/{game_state.current_agenda.doom_threshold}')

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
                    log(f'  {inv.name} draws encounter: [{card.name}] ({card.type.value})')
                    self._resolve_encounter_card(inv, card, game_state)
                else:
                    log(f'  {inv.name} — encounter deck empty')

    def _resolve_investigator_ability(self, inv: Investigator, game_state):
        """Resolve investigator-specific abilities."""
        if inv.id == "abel_redcloud":
            game_state.chaos_bag.add_bless(1)
            inv.bless_tokens_added += 1
            inv.heal_damage(1, healer=inv)
            log(f'  {inv.name} ability: +1 bless token (total {game_state.chaos_bag.get_size()} in bag), heal 1 damage (HP {inv.current_health}/{inv.health})')

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
            log(f'    Fire! — damaging assets...')
            for asset in list(inv.play_area):
                if asset.health:
                    old_hp = asset.health
                    asset.health -= 1
                    if asset.health <= 0:
                        inv.discard_card(asset)
                        log(f'    {asset.name} destroyed by Fire!')
                    else:
                        log(f'    {asset.name}: {old_hp} -> {asset.health} HP')
            from .skill_test import SkillTestResolver
            resolver = SkillTestResolver()
            result = resolver.resolve(inv, "agility", 3, game_state.chaos_bag)
            log(f'    Agility 3 test: {result}')
            if not result.success:
                inv.take_damage(1, source="Fire!")
                log(f'    {inv.name} takes 1 damage (HP {inv.current_health}/{inv.health})')

        elif name == "cosmic evils":
            log(f'    Cosmic Evils — placing 1 doom on agenda')
            game_state.current_agenda.add_doom(1)

        elif name == "caught in a lie":
            from .skill_test import SkillTestResolver
            resolver = SkillTestResolver()
            result = resolver.resolve(inv, "willpower", 2, game_state.chaos_bag)
            log(f'    Willpower 2 test: {result}')
            if not result.success:
                inv.take_horror(1, source="Caught in a Lie")
                log(f'    {inv.name} takes 1 horror (SAN {inv.current_sanity}/{inv.sanity})')

        elif name == "disorienting fear":
            from .skill_test import SkillTestResolver
            resolver = SkillTestResolver()
            result = resolver.resolve(inv, "willpower", 2, game_state.chaos_bag)
            log(f'    Willpower 2 test: {result}')
            if not result.success:
                inv.take_horror(1, source="Disorienting Fear")
                log(f'    {inv.name} takes 1 horror (SAN {inv.current_sanity}/{inv.sanity})')

        else:
            from .skill_test import SkillTestResolver
            resolver = SkillTestResolver()
            result = resolver.resolve(inv, "willpower", 2, game_state.chaos_bag)
            log(f'    Willpower 2 test: {result}')
            if not result.success:
                inv.take_horror(1, source=card.name)
                log(f'    {inv.name} takes 1 horror (SAN {inv.current_sanity}/{inv.sanity})')

    def _resolve_enemy_encounter(self, inv: Investigator, card: Card, game_state):
        """Resolve an enemy encounter card - spawn enemy engaged."""
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
        kws = ', '.join(enemy.keywords) if enemy.keywords else 'none'
        log(f'    Spawns {enemy.name} (F{enemy.fight} E{enemy.evade} HP{enemy.current_health} Dmg{enemy.damage}/{enemy.horror} [{kws}]) engaged with {inv.name}')


class InvestigationPhase:
    def execute(self, game_state):
        log('')
        log('--- INVESTIGATION PHASE ---')
        for inv in game_state.investigators:
            if inv.is_defeated():
                log(f'  {inv.name}: DEFEATED — skipping')
                continue

            log(f'  {inv.name}: {inv.actions} actions, {inv.resources} resources, {len(inv.hand)} cards in hand')
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
        log('')
        log('--- ENEMY PHASE ---')
        # Enemies attack
        for inv in game_state.investigators:
            if inv.is_defeated():
                continue
            for enemy in list(inv.engaged_enemies):
                if not enemy.exhausted:
                    log(f'  {enemy.name} attacks {inv.name}: {enemy.damage} dmg + {enemy.horror} hor')
                    enemy.attack(inv)
                    log(f'    {inv.name}: HP {inv.current_health}/{inv.health} SAN {inv.current_sanity}/{inv.sanity}')
                    if inv.is_defeated():
                        log(f'    *** {inv.name} DEFEATED ***')

        # Resolve Eleanor Heart's heal ability after damage
        for inv in game_state.investigators:
            if inv.id == "eleanor_heart" and hasattr(inv, '_pending_eleanor_heal') and inv._pending_eleanor_heal:
                heal_amount = inv._pending_eleanor_heal
                inv._pending_eleanor_heal = None
                # Find an investigator at same location to heal
                for target_inv in game_state.investigators:
                    if not target_inv.is_defeated() and target_inv.id != "eleanor_heart":
                        if target_inv.current_health < target_inv.health:
                            old_hp = target_inv.current_health
                            target_inv.heal_damage(heal_amount, healer=inv)
                            log(f'  Eleanor Heart ability: heals {heal_amount} damage from {target_inv.name} (HP {old_hp} -> {target_inv.current_health})')
                            break
                        elif target_inv.current_sanity < target_inv.sanity:
                            old_san = target_inv.current_sanity
                            target_inv.heal_horror(heal_amount, healer=inv)
                            log(f'  Eleanor Heart ability: heals {heal_amount} horror from {target_inv.name} (SAN {old_san} -> {target_inv.current_sanity})')
                            break

        # End-of-round effects from assets
        for inv in game_state.investigators:
            if inv.is_defeated():
                continue
            for asset in list(inv.play_area):
                if asset.name == "It's Time" and not asset.exhausted:
                    if inv.current_sanity < inv.sanity:
                        old_san = inv.current_sanity
                        inv.heal_horror(1, healer=inv)
                        log(f'  {asset.name} end-of-round: heals 1 horror from {inv.name} (SAN {old_san} -> {inv.current_sanity})')

        # Resolve pending bless tokens from Fort Warren Chapel
        for inv in game_state.investigators:
            if inv._pending_bless > 0:
                game_state.chaos_bag.add_bless(inv._pending_bless)
                inv.bless_tokens_added += inv._pending_bless
                log(f'  Fort Warren Chapel: {inv._pending_bless} bless token(s) added to chaos bag (total: {game_state.chaos_bag.get_size()})')
                inv._pending_bless = 0

        # Ready exhausted enemies
        for enemy in game_state.enemies:
            if enemy.exhausted:
                enemy.ready()


class UpkeepPhase:
    def execute(self, game_state):
        log('')
        log('--- UPKEEP PHASE ---')
        for inv in game_state.investigators:
            if inv.is_defeated():
                continue

            inv.ready_all()
            old_resources = inv.resources
            inv.gain_resource()
            drawn = inv.draw_card()
            inv.ability_used_this_round = False
            drawn_name = drawn.name if drawn else 'nothing'
            log(f'  {inv.name}: +1 resource ({old_resources} -> {inv.resources}), draw [{drawn_name}], ready all')
