"""Enjoy to Black Jack game!"""

from player import Player
from deck import Deck
from exceptions import GameOverException, GameOverPlayerException


class Game:

    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()

    @staticmethod
    def _print_menu():
        print("Co chcesz zrobić?")
        print("0 - pasuję")
        print("1 - dobieram kartę")

    @staticmethod
    def check_hand(player):
        print(player.cards)
        print(player.calculate_points())

    def _player_plays(self):
        player1 = Player()
        player1.take_card(self.deck.hit())
        player1.take_card(self.deck.hit())

        while True:
            self.check_hand(player1)
            self._print_menu()

            player1_choice = input('Twój wybór: ')
            if player1_choice == "0":
                break
            elif player1_choice == "1":
                player1.take_card(self.deck.hit())
            else:
                print('Podano zły wybór')

    def play(self):
        try:
            self._player_plays()
        except GameOverException as error:
            raise GameOverPlayerException from error


