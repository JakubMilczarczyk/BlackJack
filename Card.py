class Card:

    possible_colors = [
        'Clubs',
        'Spades',
        'Diamonds',
        'Hearts'
    ]

    possible_values = [
        range(2, 11),
        'Ace',
        'King',
        'Queen',
        'Jack'
    ]

    def __init__(self, color, value):
        self.color = self.possible_colors[color]
        self.value = self.possible_values[value]
