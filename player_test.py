from player import Player
from card import Card


def test_calculate_players_points():
    # given
    card1 = Card(2, 'Spades')
    card2 = Card('King', 'Hearts')

    # when
    player = Player()
    player.take_card(card1)
    player.take_card(card2)

    assert player.calculate_points() == 12

def test_calculate_players_points_two_aces():
    # given
    card1 = Card('Ace', 'Spades')
    card2 = Card('Ace', 'Hearts')

    # when
    player = Player()
    player.take_card(card1)
    player.take_card(card2)

    assert player.calculate_points() == 21

def test_calculate_players_points_ace_two_cards():
    # given
    card1 = Card(2, 'Spades')
    card2 = Card('Ace', 'Hearts')

    # when
    player = Player()
    player.take_card(card1)
    player.take_card(card2)

    assert player.calculate_points() == 13
def test_calculate_players_points_ace_three_cards():
    # given
    card1 = Card(2, 'Spades')
    card2 = Card('King', 'Hearts')
    card3 = Card('Ace', 'Clubs')

    # when
    player = Player()
    player.take_card(card1)
    player.take_card(card2)
    player.take_card(card3)

    assert player.calculate_points() == 13

