from games.connect4.action import Connect4Action
from games.connect4.player import Connect4Player
from games.connect4.state import Connect4State
import os


class HumanConnect4Player(Connect4Player):

    def __init__(self, name):
        super().__init__(name)


    def show_score(self, state: Connect4State):
        print(f"Number of piles of opponent:{state.score_player_0}")
        print(f"Your Number of piles :{state.score_player_1}")

    def get_colours(self, state: Connect4State):
        state.display()
        self.show_score(state)
        print(f"Chosen colors by opponent: {state.chosen_colors_player_0}")  
        print(f"Chosen colors by you: {state.chosen_colors_player_1}")   
        while len(state.chosen_colors_player_1) < 2:
            wantTo = input("wanna pick a color?\n")
            wantTo = wantTo.upper()
            if wantTo == 'Y':
                print(f"Available Colors:{state.available_colors}\n1-BLUE\n2-BLACK\n3-GREEN\n4-RED\n5-WHITE\n:")
                chosen = input("Choose one of the available colors:\n")
                chosen = int(chosen)
                while chosen not in state.available_colors:
                    os.system('cls')
                    print("That color is invalid or already chosen by opponent\n")
                    print("Choose one of the available colors\n")
                    print(f"Available Colors:{state.available_colors}\n1-BLUE\n2-BLACK\n3-GREEN\n4-RED\n5-WHITE\n:")
                    chosen = input("Choose a color:\n")
                    chosen = int(chosen)   
                state.chosen_colors_player_1.append(chosen)
                state.available_colors.remove(chosen)
                break
            elif wantTo == 'N':
                break    
            else:
                print("Just Y or N pls")
    def get_action(self, state: Connect4State):
        print(f"Chosen colors by opponent: {state.chosen_colors_player_0}")  
        print(f"Chosen colors by you: {state.chosen_colors_player_1}") 
        while True:
            # noinspection PyBroadException
            try:
                return Connect4Action(int(input(f"Player {state.get_acting_player()}, choose the column of the piece you want to move: ")),int(input(f"Player {state.get_acting_player()}, choose the row of the piece you want to move: "))
                ,int(input(f"Player {state.get_acting_player()}, choose the column where you want to move the piece: ")),int(input(f"Player {state.get_acting_player()}, choose the row where you want to move the piece: ")))
            except Exception:
                continue

    def event_action(self, pos: int, action, new_state: Connect4State):
        # ignore
        pass

    def event_end_game(self, final_state: Connect4State):
        # ignore
        pass
