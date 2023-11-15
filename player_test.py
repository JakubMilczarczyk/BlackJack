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
