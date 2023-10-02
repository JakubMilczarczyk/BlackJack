from Card import Card


def test_creation():
    card = Card('Kier', 'A')
    assert card.color == 'Diamonds'
    assert card.value == 'Ace'
