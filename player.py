from card import Card


class Player:
    def __init__(self):
        self.cards = []

    def take_card(self, card: Card):
        self.cards.append(card)

    def calculate_points(self):

        points = 0
        # TODO AS!!!
        for card in self.cards:
            if card.value in ['Ace', 'King', 'Queen', 'Jack']:
                points += 10
            else:
                points += card.value

        return points
