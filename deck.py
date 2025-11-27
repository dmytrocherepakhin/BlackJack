"""
Deck module
"""
import random
from card import Card
from const import SUITS, RANKS

class Deck:
    """
    Deck class
    """
    def __init__(self):
        self.cards = []
        self._build()
        self.shuffle()

    def _build(self):
        """
        створення Deck
        :return: None
        """
        self.cards = []
        for suit in SUITS:
            for rank in RANKS:
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        """
        перемішування колоди
        :return: None
        """
        random.shuffle(self.cards)

    def draw(self):
        """
        отримання верхньої карти
        :return: Card()
        """
        if not self.cards:
            self._build()
            self.shuffle()
        return self.cards.pop()
