from game import Game
from exceptions import GameOverCroupierException, GameOverPlayerException

try:
    game = Game()
    game.play()
except GameOverCroupierException:
    print('Wygrywa Gracz!')
except GameOverPlayerException:
    print('Wygrywa Krupier!')
