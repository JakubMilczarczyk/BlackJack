"""Tests for Card class"""
import pytest
from card import Card, InvalidValue, InvalidColor


def test_creation():
    """
    The test_creation function tests the creation of a Card object.

    :return: The value of the card
    :doc-author: Trelent
    """
    card = Card(9, 'Diamonds')
    print(card.value)       # użyj flagi -s za pytest
    assert card.color == 'Diamonds'
    assert card.value == 9


def test_creation_wrong_color():
    """
    The test_creation_wrong_color function tests the creation of a card with an invalid color.
    It raises an InvalidColor exception.

    :return: 'invalid card color!' when the card class is called with a wrong color
    :doc-author: Trelent
    """
    with pytest.raises(InvalidColor) as message:
        Card('Jack', 'Black')
        assert message == 'Invalid card color!'


def test_creation_wrong_value():
    """
    The test_creation_wrong_value function tests the Card class to
    see if it raises an InvalidValue exception when
    the card value is not a valid one. The test passes if
    the function does raise an InvalidValue exception.

    :return: An error message
    :doc-author: Trelent
    """
    with pytest.raises(InvalidValue) as message:
        Card('J', 'Diamonds')
        assert message == 'Invalid card value!'


def test_represent_card():
    """
    The test_represent_card function tests the __repr__ method of the Card class.
    It does this by creating a card object and comparing it
    to a string representation of what we expect.

    :return: 'card - ace diamonds'
    :doc-author: Trelent
    """
    Card('Ace', 'Diamonds')
    assert repr(Card('Ace', 'Diamonds')) == 'card - Ace Diamonds'
