"""In this module you can create a class named Card"""


class InvalidColor(Exception):
    """Corrects readability with card_test"""


class InvalidValue(Exception):
    """Corrects readability with card_test"""


class Card:
    """This class take two attributes and make card object """
    possible_colors = [
        'Clubs',
        'Spades',
        'Diamonds',
        'Hearts'
    ]

    possible_values = list(range(2, 11)) + [
        'Ace',
        'King',
        'Queen',
        'Jack'
    ]

    def __init__(self, value, color):
        """    
        The __init__ function is called when the object is created.
        It sets up the initial state of the object.
        
        
        :rtype: object
        :param self: Refer to the current instance of the class
        :param color: Assign the color of the card
        :param value: Set the value of the card
        :return: An object of the class card
        :doc-author: Trelent
        """
        if value not in self.possible_values:
            raise InvalidValue('Invalid card value!')
        self.value = value
        if color not in self.possible_colors:
            raise InvalidColor('Invalid card color!')
        self.color = color

    def __repr__(self):

        """
    The __repr__ function is used to compute the &quot;official&quot;
    string representation of an object.
    This is how you would make an object of the class. The goal of __repr__ is to be unambiguous.

    :param self: Refer to the instance of the class
    :return: A string representation of the object
    :doc-author: Trelent
    """
        return f'card - {self.value + " " + self.color}'


# card = Card('Ace', 'Spades')
# print(card)
