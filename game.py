"""Enjoy to Black Jack game!"""

from player import Player
from deck import Deck
from exceptions import GameOverException, GameOverPlayerException, GameOverCroupierException


class Game:

    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.player1 = Player()
        self.croupier = Player()

    @staticmethod
    def _print_menu():
        print("\nCo chcesz zrobić?")
        print("0 - pasuję")
        print("1 - dobieram kartę")

    @staticmethod
    def check_hand(player):
        print(player.cards)
        print(player.calculate_points())

    def _player_plays(self):
        self.player1.take_card(self.deck.hit())
        self.player1.take_card(self.deck.hit())

        while True:
            self.check_hand(self.player1)
            self._print_menu()

            player1_choice = input('Twój wybór: ')
            if player1_choice == "0":
                break
            elif player1_choice == "1":
                self.player1.take_card(self.deck.hit())
            else:
                print('Podano zły wybór')

    def _croupier_play(self):
        croupier_points = 0
        self.croupier.take_card(self.deck.hit())
        self.croupier.take_card(self.deck.hit())

        while self.croupier.calculate_points() <= self.player1.calculate_points():
            self.croupier.take_card(self.deck.hit())

            return croupier_points

    def show_croupier_hand(self):
        print('RĘKA KRUPIERA:')
        print(self.croupier.cards)
        print(self.croupier.calculate_points())

    def play(self):
        try:
            self._player_plays()
        except GameOverException as error:
            raise GameOverPlayerException from error

        try:
            self._croupier_play()
        except GameOverException as error:
            raise GameOverCroupierException from error

        self.show_croupier_hand()
        print('Koniec gry! Wygrywa Krupier')

