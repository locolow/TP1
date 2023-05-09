from random import randint
import random
from games.connect4.action import Connect4Action
from games.connect4.player import Connect4Player
from games.connect4.state import Connect4State
from games.state import State


class RandomConnect4Player2(Connect4Player):

    def __init__(self, name):
        super().__init__(name)

    def show_score(self, state: Connect4State):
        print(f"Number of piles of opponent:{state.score_player_0}")
        print(f"Your Number of piles :{state.score_player_1}")

    def get_colours(self, state: Connect4State):
        while len(state.chosen_colors_player_1) < 2:
            chosen = random.choice(state.available_colors)
            chosen = int(chosen)
            state.chosen_colors_player_1.append(chosen)
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
