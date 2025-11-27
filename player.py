"""
Player module
"""
from abc import ABC, abstractmethod
from const import BLACKJACK_VALUE, DEALER_STAND_VALUE

class BasePlayer(ABC):
    """
    BasePlayer abstract class
    """
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.stand = False

    def add_card(self, card):
        """
        додавання карт
        :param card:
        :return: None
        """
        self.hand.append(card)

    def clear_hand(self):
        """
        очистка карт на руках
        :return: None
        """
        self.hand = []
        self.stand = False

    def total(self):
        """
        підрахунок результату
        :return: int
        """
        total = 0
        aces = 0

        for card in self.hand:
            total += card.get_value()
            if card.rank == 'Ace':
                aces += 1

        while total > BLACKJACK_VALUE and aces > 0:
            total -= 10
            aces -= 1

        return total

    def is_busted(self):
        """
        фіксація перебору
        :return: boolean
        """
        return self.total() > BLACKJACK_VALUE

    @abstractmethod
    def decide_action(self):
        pass

    def __str__(self):
        cards_str = " ".join(str(c) for c in self.hand)
        return f"{self.name}: {cards_str} (total={self.total()})"


class Player(BasePlayer):
    def __init__(self, name, balance):
        super().__init__(name)
        self.balance = balance
        self.current_bet = 0

    def place_bet(self, amount):
        if amount > self.balance:
            raise ValueError("Ставка більша за баланс.")
        self.current_bet = amount
        self.balance -= amount

    def win_bet(self, multiplier=2.0):
        self.balance += int(self.current_bet * multiplier)
        self.current_bet = 0

    def push_bet(self):
        self.balance += self.current_bet
        self.current_bet = 0

    def lose_bet(self):
        self.current_bet = 0

    def decide_action(self):
        while True:
            choice = input("Ваш хід (h – взяти карту / s – зупинитись): ").strip().lower()
            if choice in ("h", "hit"):
                return "hit"
            if choice in ("s", "stand"):
                self.stand = True
                return "stand"
            print("Невірний вибір. Спробуйте ще раз.")


class Dealer(BasePlayer):
    def __init__(self):
        super().__init__("Дилер")
        self.stand_value = DEALER_STAND_VALUE

    def decide_action(self):
        if self.total() < self.stand_value:
            return "hit"
        self.stand = True
        return "stand"
