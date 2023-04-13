from games.connect4.player import Connect4Player
from games.connect4.state import Connect4State
from games.game_simulator import GameSimulator


class Connect4Simulator(GameSimulator):

    def __init__(self, player1: Connect4Player, player2: Connect4Player):
        super(Connect4Simulator, self).__init__([player1, player2])

    def init_game(self):
        return Connect4State()

    def before_end_game(self, state: Connect4State):
        # ignored for this simulator
        pass

    def end_game(self, state: Connect4State):
        # ignored for this simulator
        pass
