from random import randint
import random
from games.connect4.action import Connect4Action
from games.connect4.player import Connect4Player
from games.connect4.state import Connect4State
from games.state import State


class RandomConnect4Player(Connect4Player):

    def __init__(self, name):
        super().__init__(name)

    def get_colours(self, state: Connect4State):
        state.display()
        while len(state.available_colors) > 1:
            print(state.available_colors)
            chosen = random.choice(state.available_colors)
            chosen = int(chosen)
            state.chosen_colors_player_0.append(chosen)
            state.available_colors.remove(chosen)
            break

    def get_action(self, state: Connect4State):
        return Connect4Action(randint(0, state.get_num_cols()),randint(0, state.get_num_rows()),randint(0, state.get_num_cols()),randint(0, state.get_num_rows()))

    def event_action(self, pos: int, action, new_state: State):
        # ignore
        pass

    def event_end_game(self, final_state: State):
        # ignore
        pass
