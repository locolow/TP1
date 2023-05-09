import math
import random
from games.connect4.action import Connect4Action
from games.connect4.player import Connect4Player
from games.connect4.result import Connect4Result
from games.connect4.state import Connect4State
from games.state import State

class MinimaxConnect4Player(Connect4Player):

    best_action = None

    def __init__(self, name):
        super().__init__(name)
        
    # Heuristica de mover: A IA vai optar pelas ações que posicione os workers nos edificios mais altos
    def __move_heuristic(self, state: Connect4State):
        # check if any stack has a height of 4
        for i, row in enumerate(state.grid):
            for j, element in enumerate(row):
                if isinstance(element, tuple) and element[1] == 4:
                    if self.get_current_pos() == 0 and element[0] in state.chosen_colors_player_0:
                        return 1.0
                    elif self.get_current_pos() == 1 and element[0] in state.chosen_colors_player_1:
                        return 1.0
        return 0.0

    """Implementation of minimax search (recursive, with alpha/beta pruning) :param state: the state for which the 
    search should be made :param depth: maximum depth of the search :param alpha: to optimize the search :param beta: 
    to optimize the search :param is_initial_node: if true, the function will return the action with max ev, 
    otherwise it return the max ev (ev = expected value) """

    def minimax(self, state: Connect4State, depth: int, alpha: int = -math.inf, beta: int = math.inf,
            is_initial_node: bool = True):
        # first we check if we are in a terminal node (victory, draw or loose)
        if state.is_game_over():
            return {
                Connect4Result.WIN: 40,
                Connect4Result.DRAW: 0,
                Connect4Result.LOOSE: -40,
            }[state.get_result(State.get_acting_player())]

        # if we reached the maximum depth, we will return the value of the heuristic
        if depth == 0:
            return self.__move_heuristic(state)

        # if we are the acting player
        if state.get_acting_player() == 1:
            selected_actions = []
            highest_value = -math.inf

            for action in state.get_possible_actions():
                action_value = max(highest_value, self.minimax(state.sim_play(
                    action), depth - 1, alpha, beta, False))

                if action_value == highest_value:
                    selected_actions.append(action)
                if action_value > highest_value:
                    selected_actions = [action]
                if highest_value > beta:
                    break
                alpha = max(alpha, highest_value)

            best_action = random.choice(selected_actions)
            best_value = highest_value

            if is_initial_node:
                return (best_action, best_value)
            else:
                return best_value
        if state.get_acting_player() == 0:
            pass
    def get_move(self, state: Connect4State):
        MinimaxConnect4Player.best_action, _ = self.minimax(state, 5)
        return MinimaxConnect4Player.best_action
    
    def get_action(self, state: Connect4State):
        best_action, _ = self.minimax(state, 5)
        return Connect4Action(best_action)


    def get_colours(self, state: Connect4State):
        while len(state.chosen_colors_player_1) < 2:
            chosen = random.choice(state.available_colors)
            chosen = int(chosen)
            state.chosen_colors_player_1.append(chosen)
            state.available_colors.remove(chosen)
            break


    def event_action(self, pos: int, action, new_state: State):
        # ignore
        pass

    def event_end_game(self, final_state: State):
        # ignore
        pass
