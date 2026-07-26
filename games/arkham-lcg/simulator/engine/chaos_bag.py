import random
import yaml
from dataclasses import dataclass, field
from typing import List, Optional
from pathlib import Path


@dataclass
class Token:
    symbol: str
    modifier: int  # numerical modifier, or None for symbols

    def is_auto_fail(self) -> bool:
        return self.symbol == "auto_fail"

    def is_elder_sign(self) -> bool:
        return self.symbol == "elder_sign"

    def is_bless(self) -> bool:
        return self.symbol == "bless"

    def is_curse(self) -> bool:
        return self.symbol == "curse"

    def is_symbol(self) -> bool:
        return self.symbol in ["skull", "cultist", "tablet", "elder_thing",
                                "elder_sign", "auto_fail", "bless", "curse"]

    def __str__(self):
        return self.symbol


class ChaosBag:
    def __init__(self, difficulty: str = "standard"):
        self.difficulty = difficulty
        self.tokens = self._load_tokens(difficulty)
        self.bag = []
        self.bless_count = 0
        self.curse_count = 0
        self.reset()

    def _load_tokens(self, difficulty: str) -> List[Token]:
        config_path = Path(__file__).parent.parent / "config" / "chaos_bags.yaml"
        with open(config_path, 'r') as f:
            config = yaml.safe_load(f)

        tokens = []
        bag_config = config.get(difficulty, config.get("standard"))
        for entry in bag_config.get("tokens", []):
            for _ in range(entry.get("count", 1)):
                tokens.append(Token(
                    symbol=entry["symbol"],
                    modifier=entry.get("modifier", 0)
                ))
        return tokens

    def reset(self):
        self.bag = list(self.tokens)
        random.shuffle(self.bag)

    def draw(self) -> Token:
        if not self.bag:
            self.bag = list(self.tokens)
            random.shuffle(self.bag)
        return self.bag.pop()

    def add_bless(self, count: int = 1):
        self.bless_count += count
        for _ in range(count):
            self.tokens.append(Token("bless", 0))
            self.bag.append(Token("bless", 0))

    def add_curse(self, count: int = 1):
        self.curse_count += count
        for _ in range(count):
            self.tokens.append(Token("curse", -2))
            self.bag.append(Token("curse", -2))

    def return_token(self, token: Token):
        """Return a token to the bag (for bless/curse return)."""
        self.bag.append(token)

    def get_size(self) -> int:
        return len(self.bag)

    def get_token_counts(self) -> dict:
        counts = {}
        for token in self.bag:
            counts[token.symbol] = counts.get(token.symbol, 0) + 1
        return counts
