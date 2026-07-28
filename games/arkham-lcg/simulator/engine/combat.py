from dataclasses import dataclass
from typing import Optional, List
from .models import Investigator, Enemy, Card
from .skill_test import SkillTestResolver, SkillTestResult
from .chaos_bag import ChaosBag


@dataclass
class FightResult:
    test_result: SkillTestResult
    damage_dealt: int
    enemy_defeated: bool
    retaliation: bool
    weapon_used: Optional[Card] = None

    def __str__(self):
        return (f"Fight: {self.test_result} | Damage: {self.damage_dealt} "
                f"| Defeated: {self.enemy_defeated} | Retaliation: {self.retaliation}")


@dataclass
class EvadeResult:
    test_result: SkillTestResult
    enemy_exhausted: bool
    enemy_disengaged: bool
    alert_triggered: bool = False

    def __str__(self):
        return (f"Evade: {self.test_result} | Exhausted: {self.enemy_exhausted} "
                f"| Disengaged: {self.enemy_disengaged}")


class CombatResolver:
    def __init__(self):
        self.skill_resolver = SkillTestResolver()

    def fight(
        self,
        investigator: Investigator,
        enemy: Enemy,
        chaos_bag: ChaosBag,
        weapon: Optional[Card] = None,
        committed_cards: Optional[List[Card]] = None,
        scenario_effects: Optional[dict] = None
    ) -> FightResult:
        """
        Resolve a fight action.

        Args:
            investigator: The investigator fighting
            enemy: The enemy to fight
            chaos_bag: The chaos bag
            weapon: Optional weapon being used
            committed_cards: Cards committed to the test
            scenario_effects: Scenario-specific effects

        Returns:
            FightResult with all details
        """
        if committed_cards is None:
            committed_cards = []

        # Calculate bonuses
        bonuses = {}
        damage_bonus = 0

        if weapon:
            # Weapon fight bonus
            text_lower = weapon.text.lower()
            if "+1 <com>" in text_lower or "+2 <com>" in text_lower or "+1 com" in text_lower or "+2 com" in text_lower:
                bonuses["combat"] = 2 if ("+2 <com>" in text_lower or "+2 com" in text_lower) else 1
            # Weapon damage bonus (check +2 before +1 to avoid double-counting)
            if "+2 damage" in weapon.text or "+2 dmg" in weapon.text:
                damage_bonus += 2
            elif "+1 damage" in weapon.text or "+1 dmg" in weapon.text:
                damage_bonus += 1
            # Check for fixed damage (e.g., "deals 3 damage")
            import re
            fixed_damage = re.search(r'deals? (\d+) damage', weapon.text)
            if fixed_damage:
                damage_bonus = int(fixed_damage.group(1)) - 1  # Subtract base 1
            # Spend weapon ammo/charges
            if weapon.has_uses():
                weapon.spend_use()
                from .phases import Logger
                Logger.log(f'      {weapon.name}: {weapon.current_uses} {weapon.uses_type} remaining')

        # Check for succeed-by-2 bonus (Sacred Spear)
        succeed_by_2_bonus = 0
        if weapon and "succeed by 2 or more" in weapon.text.lower():
            succeed_by_2_bonus = 1  # Extra damage on succeed by 2

        # Resolve skill test
        test_result = self.skill_resolver.resolve(
            investigator=investigator,
            skill="combat",
            difficulty=enemy.fight,
            chaos_bag=chaos_bag,
            committed_cards=committed_cards,
            bonuses=bonuses,
            scenario_effects=scenario_effects
        )

        # Calculate damage
        damage_dealt = 0
        enemy_defeated = False
        retaliation = False

        if test_result.success:
            damage_dealt = 1 + damage_bonus  # Base 1 + weapon bonus

            # Check for succeed-by-2 bonus
            if succeed_by_2_bonus > 0:
                if test_result.final_value - enemy.fight >= 2:
                    damage_dealt += succeed_by_2_bonus

            # Check for Vicious Blow
            for card in committed_cards:
                if "Vicious Blow" in card.name:
                    damage_dealt += 1

            # Apply damage
            enemy_defeated = enemy.take_damage(damage_dealt)

        # Check for retaliation
        if not test_result.success and "Retaliate" in enemy.keywords:
            retaliation = True
            # Enemy attacks investigator
            enemy.attack(investigator)

        return FightResult(
            test_result=test_result,
            damage_dealt=damage_dealt,
            enemy_defeated=enemy_defeated,
            retaliation=retaliation,
            weapon_used=weapon
        )

    def evade(
        self,
        investigator: Investigator,
        enemy: Enemy,
        chaos_bag: ChaosBag,
        committed_cards: Optional[List[Card]] = None,
        scenario_effects: Optional[dict] = None
    ) -> EvadeResult:
        """
        Resolve an evade action.

        Args:
            investigator: The investigator evading
            enemy: The enemy to evade
            chaos_bag: The chaos bag
            committed_cards: Cards committed to the test
            scenario_effects: Scenario-specific effects

        Returns:
            EvadeResult with all details
        """
        if committed_cards is None:
            committed_cards = []

        # Resolve skill test
        test_result = self.skill_resolver.resolve(
            investigator=investigator,
            skill="agility",
            difficulty=enemy.evade,
            chaos_bag=chaos_bag,
            committed_cards=committed_cards,
            scenario_effects=scenario_effects
        )

        enemy_exhausted = False
        enemy_disengaged = False
        alert_triggered = False

        if test_result.success:
            enemy.exhaust()
            enemy.disengage()
            enemy_exhausted = True
            enemy_disengaged = True
        else:
            # Check for Alert keyword
            if "Alert" in enemy.keywords:
                alert_triggered = True
                enemy.attack(investigator)

        return EvadeResult(
            test_result=test_result,
            enemy_exhausted=enemy_exhausted,
            enemy_disengaged=enemy_disengaged,
            alert_triggered=alert_triggered
        )

    def enemy_attack(self, enemy: Enemy, investigator: Investigator):
        """
        Resolve an enemy attack during the Enemy Phase.

        Args:
            enemy: The attacking enemy
            investigator: The investigator being attacked
        """
        if enemy.exhausted:
            return

        # Deal damage and horror
        investigator.take_damage(enemy.damage, source=enemy.name)
        investigator.take_horror(enemy.horror, source=enemy.name)

        # Check for special enemy effects
        if "After attacks" in enemy.text or "after_attack" in enemy.text:
            # Hellhound: discard 1 asset
            if "discard 1 asset" in enemy.text:
                if investigator.play_area:
                    # Discard random asset
                    import random
                    asset = random.choice(investigator.play_area)
                    investigator.discard_card(asset)
