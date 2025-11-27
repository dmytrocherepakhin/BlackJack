"""
card module
"""
from const import RANK_VALUES, SUIT_SYMBOLS, RANK_SHORT

class Card:
    """
    Card class
    """
    def __init__(self, suit: str, rank: str) -> None:
        self.suit = suit
        self.rank = rank

    def get_value(self) -> int:
        """
        Повертає числове значення карти для підрахунку.
        """
        return RANK_VALUES[self.rank]

    def __str__(self) -> str:
        """
        Коротке текстове представлення карти.
        """
        rank_display = RANK_SHORT[self.rank]
        return f"{rank_display}{SUIT_SYMBOLS[self.suit]}"
