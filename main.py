"""
BlackJack Game
"""
from game import Game

def main():
    """
    main function
    :return: None
    """
    name = input("Введіть ваше ім'я: ").strip() or "Гравець"
    game = Game(name)
    game.run()

if __name__ == "__main__":
    main()
