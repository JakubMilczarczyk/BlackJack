"""Tests for Deck class"""

from deck import Deck


def test_creation():

    """
    The test_creation function tests the creation of a deck.
    It does this by creating a new deck and checking that it has 52 cards.

    :return: The number of cards in the deck
    """
    deck = Deck()
    assert len(deck.cards) == 52


def test_shuffle_cards():

    """
    The test_shuffle_cards function tests the shuffle method of the Deck class.
    It does this by creating a new deck, shuffling it,
    and then comparing it to an unshuffled version of itself.
    If they are not equal, then we know that the shuffle method worked.

    :return: A boolean value
    """
    deck = Deck()
    shuffled_deck = deck.cards[:]
    deck.shuffle()
    assert shuffled_deck != deck.cards


def test_check_hit_card():

    """
    The test_check_hit_card function tests the hit method of the Deck class.
    The test_check_hit_card function creates a deck object and then assigns
    last card in the deck to a variable called last card. Then it calls
    the hit method on that deck object and assigns it to another variable called card.
    Finally, it asserts that those two variables are equal.

    :return: The last card in the deck
    """
    deck = Deck()
    last_card = deck.cards[-1]
    card = deck.hit()
    assert last_card == card


def test_hit_card():
    """
    The test_hit_card function tests the hit method of the Deck class.
    It does this by creating a new deck, calling the hit method on it, and then checking that:
        1) The card returned is no longer in the deck (i.e., it was removed from self.cards).
        2) The length of self.cards decreased by one.

    :return: The card that was removed from the deck
    """
    deck = Deck()
    card = deck.hit()
    assert card not in deck.cards
    assert len(deck.cards) == 51
