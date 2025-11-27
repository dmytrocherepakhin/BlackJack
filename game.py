"""
Game module
"""
from deck import Deck
from player import Player, Dealer
from const import BLACKJACK_VALUE, INITIAL_BALANCE, MIN_BET

class Game:
    """
    Game class
    """
    def __init__(self, player_name):
        self.deck = Deck()
        self.player = Player(player_name, INITIAL_BALANCE)
        self.dealer = Dealer()

    def _take_bet(self):
        """
        встановлення ставки
        :return: None
        """
        print("\nВаш баланс:", self.player.balance)
        if self.player.balance < MIN_BET:
            print("Недостатньо коштів для мінімальної ставки. Гра завершена.")
            return False

        while True:
            bet_input = input(
                f"Зробіть ставку (мін. {MIN_BET}, або 'q' для виходу): "
            ).strip().lower()

            if bet_input == "q":
                print("Вихід з гри.")
                return False

            if not bet_input.isdigit():
                print("Введіть число або 'q' для виходу.")
                continue

            bet = int(bet_input)

            if bet < MIN_BET:
                print(f"Мінімальна ставка: {MIN_BET}.")
                continue

            if bet > self.player.balance:
                print(f"У вас недостатньо коштів для цієї ставки. Максимум: {self.player.balance}.")
                continue

            # Списуємо ставку з балансу
            self.player.place_bet(bet)
            print(f"Ви поставили {bet}. Поточний баланс: {self.player.balance}")
            return True

    def _initial_deal(self):
        """
        начальна роздача
        :return: None
        """
        self.player.clear_hand()
        self.dealer.clear_hand()
        for _ in range(2):
            self.player.add_card(self.deck.draw())
            self.dealer.add_card(self.deck.draw())

    def _show_some(self):
        """
        відкриття частини карт
        :return: None
        """
        print("\n=== Карти на столі ===")
        print(self.player)
        dealer_first = str(self.dealer.hand[0])
        print(f"Дилер: {dealer_first} [прихована карта]")

    def _show_all(self):
        """
        відкриття карт
        :return: None
        """
        print("\n=== Відкриття карт ===")
        print(self.player)
        print(self.dealer)

    def _player_turn(self):
        """
        хід гравця
        :return: None
        """
        print("\nХід гравця...")
        while not self.player.stand and not self.player.is_busted():
            self._show_some()
            action = self.player.decide_action()
            if action == "hit":
                self.player.add_card(self.deck.draw())
                print(f"\n{self.player.name} бере карту...")
        self._show_some()
        if self.player.is_busted():
            print(f"\n{self.player.name} перебрав!")

    def _dealer_turn(self):
        """
        хід дилера
        :return: None
        """
        print("\nХід дилера...")
        self._show_all()
        while not self.dealer.stand and not self.dealer.is_busted():
            action = self.dealer.decide_action()
            if action == "hit":
                self.dealer.add_card(self.deck.draw())
                print("Дилер бере карту...")
                self._show_all()

    def _settle_bet(self):
        """
        підбиває підсумок раунду
        :return: None
        """
        self._show_all()

        if self.player.is_busted():
            print("Ви перебрали! Ви програли ставку.")
            self.player.lose_bet()
            return

        if self.dealer.is_busted():
            print("Дилер перебрав! Ви виграли.")
            self.player.win_bet()
            return

        if self.player.total() > self.dealer.total():
            print("Ви ближче до 21! Ви виграли.")
            self.player.win_bet()
        elif self.player.total() < self.dealer.total():
            print("Дилер ближче до 21. Ви програли.")
            self.player.lose_bet()
        else:
            print("Нічия (push). Ставка повертається.")
            self.player.push_bet()

    def play_round(self):
        """
        проведення раунду гри
        :return: Boolean
        """
        if not self._take_bet():
            return False

        self._initial_deal()

        if self.player.total() == BLACKJACK_VALUE and len(self.player.hand) == 2:
            self._show_all()
            if self.dealer.total() == BLACKJACK_VALUE and len(self.dealer.hand) == 2:
                print("У обох блекджек! Нічия.")
                self.player.push_bet()
            else:
                print("Натуральний блекджек! Ви виграли 1.5x.")
                self.player.win_bet(multiplier=2.5)
            return True

        self._player_turn()

        if not self.player.is_busted():
            self._dealer_turn()

        self._settle_bet()
        return True

    def run(self):
        """
        запуск гри
        :return: None
        """
        print("=== Ласкаво просимо до Blackjack! ===")
        while True:
            continue_game = self.play_round()
            if not continue_game:
                break
            if self.player.balance < MIN_BET:
                print("Недостатньо коштів для продовження гри.")
                break

            ans = input("\nЗіграти ще один раунд? (y/n): ").strip().lower()
            if ans != "y":
                break


        print("Гра завершена. Ваш фінальний баланс:", self.player.balance)
