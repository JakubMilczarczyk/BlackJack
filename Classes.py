# from random import random
import json
with open("Deck.json") as file:
    deck_blueprint = json.load(file)


class Card:
    def __init__(self, color: str, typing: str):
        self.color = color
        self.typing = typing

    def power(self):
        if self.typing == 'A':
            as_card = self.typing
            return as_card
        elif self.typing in ('J', 'Q', 'K'):
            return 10
        else:
            return int(self.typing)

# Plan jest taki: Paramatry kart są w pilku json który jest pobierany przy tworzeniu kart,
# przez przeliterowanie po tym pilku w metodzie deck kasy Deck.
# tasowanie zrobimy w klasie gra i tam też robimy naliczanie punktów z rozwiązaniem problemu asa włącznie
# rozdawanie kart z biblioteki random robimy w klasie gra
# gracza i krupiera jako osobne klasy robimy w klasie gra


class Deck(Card):

    def __init__(self, color, typing):
        super().__init__(color, typing)
        # self.suit = suit
        # self.cards = cards(Card)

    @staticmethod
    def make_deck():
        deck = []


card1 = Card("pik", "Q")
print(type(card1), card1.power(), card1.color)
