from deck import Deck


def test_creation():
    deck = Deck()
    assert len(deck.cards) == 52


def test_shuffle_cards():
    deck = Deck()
    shuffled_deck = deck.cards[:]
    deck.shuffle()
    assert shuffled_deck != deck.cards


def test_check_hit_card():
    deck = Deck()
    last_card = deck.cards[-1]
    card = deck.hit()
    assert last_card == card


def test_hit_card():
    deck = Deck()
    card = deck.hit()
    assert card not in deck.cards
    assert len(deck.cards) == 51
