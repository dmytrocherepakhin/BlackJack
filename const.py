"""
constants module
"""
BLACKJACK_VALUE = 21
DEALER_STAND_VALUE = 17
INITIAL_BALANCE = 100
MIN_BET = 10

SUITS = ['heart', 'diamond', 'club', 'spade']
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

RANK_VALUES = {
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'Jack': 10,
    'Queen': 10,
    'King': 10,
    'Ace': 11,
}

SUIT_SYMBOLS = {
    'heart': '♥',
    'diamond': '♦',
    'club': '♣',
    'spade': '♠',
}

RANK_SHORT = {
    '2': '2',
    '3': '3',
    '4': '4',
    '5': '5',
    '6': '6',
    '7': '7',
    '8': '8',
    '9': '9',
    '10': '10',
    'Jack': 'J',
    'Queen': 'Q',
    'King': 'K',
    'Ace': 'A',
}
