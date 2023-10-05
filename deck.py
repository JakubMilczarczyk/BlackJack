"""In this module you see a class named deck"""

from card import Card
from random import shuffle


class Deck:
    def __init__(self):
        self.cards = []
        for color in Card.possible_colors:
            for value in Card.possible_values:
                self.cards.append(Card(color=color, value=value))

    def shuffle(self):
        shuffle(self.cards)

    def hit(self):
        return self.cards.pop()


