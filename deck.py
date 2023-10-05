"""
In this module you see a class named deck
"""

from random import shuffle
from card import Card


class Deck:
    """
    class Deck makes deck from objects named Card,
    can shuffle list of cards and hit one card each time you need
    """
    def __init__(self):
        """
        The __init__ function is called when the object is created.
        It initializes the cards list with all possible combinations of colors and values.

        :param self: Represent the instance of the object itself
        :return: The list of cards
        """
        self.cards = []
        for color in Card.possible_colors:
            for value in Card.possible_values:
                self.cards.append(Card(color=color, value=value))

    def shuffle(self):
        """
        The shuffle function takes the deck of cards and shuffles them.
        It does this by using the shuffle function from random,
        which is imported at the top of this file.

        :param self: Refer to the object itself
        :return: Nothing
        """
        shuffle(self.cards)

    def hit(self):
        """
        The hit function will return a card from the deck.
            It uses pop() to take the last card off of the deck and return it.

        :param self: Keep track of specific instances of a class
        :return: The last card in the deck
        """
        return self.cards.pop()
