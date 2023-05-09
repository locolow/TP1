from games.connect4.action import Connect4Action
from games.connect4.player import Connect4Player
from games.connect4.state import Connect4State
import os


class HumanConnect4Player(Connect4Player):
   
    color_dict = {
            1: 'BLUE',
            2: 'BLACK',
            3: 'GREEN',
            4: 'RED',
            5: 'WHITE',
    }

    def __init__(self, name):
        super().__init__(name)

    def show_colors(self, state: Connect4State):
        colors_0 = [HumanConnect4Player.color_dict[num] for num in state.chosen_colors_player_0]
        colors_1 = [HumanConnect4Player.color_dict[num] for num in state.chosen_colors_player_1]
        print(f"Chosen colors by opponent: {colors_0}")
        print(f"Chosen colors by you: {colors_1}")

    def show_score(self, state: Connect4State):
        print(f"Number of piles of opponent:{state.score_player_0}")
        print(f"Your Number of piles :{state.score_player_1}")

    def get_colours(self, state: Connect4State):

        state.display()
        self.show_score(state)
        self.show_colors(state)
        while len(state.chosen_colors_player_1) < 2:
            wantTo = input("Want to choose a color?\n Y - Yes\n N - No")
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
                print("Please enter 'Y' or 'N' only")
    def get_action(self, state: Connect4State):
        self.show_colors(state)
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
