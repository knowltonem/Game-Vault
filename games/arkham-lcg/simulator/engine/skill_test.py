from dataclasses import dataclass, field
from typing import List, Optional, Dict
from .models import Investigator, Card, Skill, Icons
from .chaos_bag import ChaosBag, Token


@dataclass
class SkillTestResult:
    success: bool
    base_value: int
    token: Token
    modifier: int
    final_value: int
    difficulty: int
    elder_sign: bool = False
    auto_fail: bool = False
    bless_returned: bool = False
    curse_returned: bool = False
    committed_cards: List[Card] = field(default_factory=list)
    skill_tested: str = ""

    def __str__(self):
        status = "SUCCESS" if self.success else "FAILURE"
        return (f"{status} | Base: {self.base_value} | Token: {self.token} "
                f"({self.modifier:+d}) | Final: {self.final_value} "
                f"vs Difficulty: {self.difficulty}")


class SkillTestResolver:
    def resolve(
        self,
        investigator: Investigator,
        skill: str,
        difficulty: int,
        chaos_bag: ChaosBag,
        committed_cards: Optional[List[Card]] = None,
        bonuses: Optional[Dict[str, int]] = None,
        scenario_effects: Optional[dict] = None
    ) -> SkillTestResult:
        """
        Resolve a skill test.

        Args:
            investigator: The investigator making the test
            skill: The skill being tested (willpower, intellect, combat, agility)
            difficulty: The difficulty value to beat
            chaos_bag: The chaos bag to draw from
            committed_cards: Cards committed to the test
            bonuses: Additional bonuses to the skill value
            scenario_effects: Scenario-specific token effects

        Returns:
            SkillTestResult with all test details
        """
        if committed_cards is None:
            committed_cards = []
        if bonuses is None:
            bonuses = {}
        if scenario_effects is None:
            scenario_effects = {}

        # Calculate base skill value
        base_value = investigator.get_stat(skill)

        # Add committed card icons
        for card in committed_cards:
            icons = card.icons
            if skill == "willpower":
                base_value += icons.willpower
            elif skill == "intellect":
                base_value += icons.intellect
            elif skill == "combat":
                base_value += icons.combat
            elif skill == "agility":
                base_value += icons.agility
            # Wild icons add to any skill
            base_value += icons.wild

        # Add any bonuses
        base_value += bonuses.get(skill, 0)

        # Draw chaos token
        token = chaos_bag.draw()

        # Apply token modifier
        modifier = self._get_modifier(token, scenario_effects)

        # Check for special tokens
        if token.is_auto_fail():
            return SkillTestResult(
                success=False,
                base_value=base_value,
                token=token,
                modifier=modifier,
                final_value=base_value + modifier,
                difficulty=difficulty,
                auto_fail=True,
                committed_cards=committed_cards,
                skill_tested=skill
            )

        if token.is_elder_sign():
            return SkillTestResult(
                success=True,
                base_value=base_value,
                token=token,
                modifier=modifier,
                final_value=base_value + modifier,
                difficulty=difficulty,
                elder_sign=True,
                committed_cards=committed_cards,
                skill_tested=skill
            )

        if token.is_bless():
            # Bless = treat as +2 modifier (auto-success essentially)
            modifier = 2
            # Return +1 token to bag
            chaos_bag.return_token(Token("+1", 1))
            bless_returned = True

        if token.is_curse():
            # Curse = -2 modifier
            modifier = -2
            # Return -1 token to bag
            chaos_bag.return_token(Token("-1", -1))
            curse_returned = True

        # Determine success/failure
        final_value = base_value + modifier
        success = final_value >= difficulty

        return SkillTestResult(
            success=success,
            base_value=base_value,
            token=token,
            modifier=modifier,
            final_value=final_value,
            difficulty=difficulty,
            committed_cards=committed_cards,
            skill_tested=skill,
            bless_returned=bless_returned if token.is_bless() else False,
            curse_returned=curse_returned if token.is_curse() else False
        )

    def _get_modifier(self, token: Token, scenario_effects: dict) -> int:
        """Get the modifier for a chaos token."""
        if token.is_symbol():
            # Symbol tokens use scenario-specific effects
            # For now, return a default modifier
            symbol_modifiers = {
                "skull": -2,
                "cultist": -1,
                "tablet": -3,
                "elder_thing": -2,
            }
            return symbol_modifiers.get(token.symbol, 0)
        return token.modifier
