from typing import Optional

from games.connect4.action import Connect4Action
from games.connect4.result import Connect4Result
from games.connect4.board import Piece,PieceSet
from games.state import State
import random


class Connect4State(State):
    def my_shuffle(array):
        random.shuffle(array)
        return array

    INVALID_CELL = -1
    EMPTY_CELL = 0
    PLAYED_CELL= -2
    BLUE = 1
    BLACK = 2
    GREEN = 3
    RED = 4
    WHITE = 6
    SPECIAL = 7
    NORMAL_PIECES = [
            Piece('BL'), Piece('BL'), Piece('BL'), Piece('BL'), Piece('BL'), Piece('BL'), Piece('BL'), Piece('BL'),
            Piece('BK'), Piece('BK'), Piece('BK'), Piece('BK'), Piece('BK'), Piece('BK'), Piece('BK'), Piece('BK'),
            Piece('GR'), Piece('GR'), Piece('GR'), Piece('GR'), Piece('GR'), Piece('GR'), Piece('GR'), Piece('GR'),
            Piece('RE'), Piece('RE'), Piece('RE'), Piece('RE'), Piece('RE'), Piece('RE'), Piece('RE'), Piece('RE'),
            Piece('WH'), Piece('WH'), Piece('WH'), Piece('WH'), Piece('WH'), Piece('WH'), Piece('WH'), Piece('WH'),
            Piece('SP'), Piece('SP'), Piece('SP')
        ]
    my_shuffle(NORMAL_PIECES)

    def __init__(self):
        super().__init__()
        """
        the dimensions of the board
        """
        self.__num_rows = 13
        self.__num_cols = 9

        """
        the grid
        """
        IC = Connect4State.INVALID_CELL
        EC = Connect4State.EMPTY_CELL
    
        

        self.__grid =[ 
            [IC, IC, EC, IC, EC, IC, EC, IC, IC],
            [IC, IC, IC, EC, IC, EC, IC, IC, IC],
            [IC, IC, EC, IC, EC, IC, EC, IC, IC],
            [IC, EC, IC, EC, IC, EC, IC, EC, IC],
            [IC, IC, EC, IC, EC, IC, EC, IC, IC],
            [IC, EC, IC, EC, IC, EC, IC, EC, IC],
            [EC, IC, EC, IC, EC, IC, EC, IC, EC],
            [IC, EC, IC, EC, IC, EC, IC, EC, IC],
            [IC, IC, EC, IC, EC, IC, EC, IC, IC],
            [IC, EC, IC, EC, IC, EC, IC, EC, IC],
            [IC, IC, EC, IC, EC, IC, EC, IC, IC],
            [IC, IC, IC, EC, IC, EC, IC, IC, IC],
            [IC, IC, EC, IC, EC, IC, EC, IC, IC]
        ]
       
        self.__pieces = Connect4State.NORMAL_PIECES.copy()
       

        """
        counts the number of turns in the current game
        """
        self.__turns_count = 1

        """
        the index of the current acting player
        """
        self.__acting_player = 0

        """
        determine if a winner was found already 
        """
        self.__has_winner = False


    def __check_winner(self, player):
        # check for 3 across
        #count consecutive tree (conta numeros de 3 consecutivos)
        #for row in range(0, self.__num_rows):
        #    for col in range(0, self.__num_cols - 2):
        #        if self.__grid[row][col] == player and \
        #                self.__grid[row][col + 1] == player and \
        #                self.__grid[row][col + 2] == player:
        #            return True

        # check for 4 up and down
        #for row in range(0, self.__num_rows - 2):
        #    for col in range(0, self.__num_cols):
        #        if self.__grid[row][col] == player and \
        #                self.__grid[row + 1][col] == player and \
        #                self.__grid[row + 2][col] == player:
        #            return True

        # check upward diagonal
        #for row in range(3, self.__num_rows):
        #    for col in range(0, self.__num_cols - 2):
        #        if self.__grid[row][col] == player and \
        #                self.__grid[row - 1][col + 1] == player and \
        #                self.__grid[row - 2][col + 2] == player:
        #            return True

        # check downward diagonal
        #for row in range(0, self.__num_rows - 2):
        #    for col in range(0, self.__num_cols - 2):
        #        if self.__grid[row][col] == player and \
        #                self.__grid[row + 1][col + 1] == player and \
        #                self.__grid[row + 2][col + 2] == player:
        #            return True

        return False

    def get_grid(self):
        return self.__grid

    #def place_random_pieces(self):
    #    colors = [Connect4State.BLUE, Connect4State.BLACK, Connect4State.GREEN, Connect4State.RED, Connect4State.WHITE, Connect4State.SPECIAL]
    #    counts = {color: 0 for color in colors}

        # place up to 5 pieces of each color and 3 of the special ones
    #    while any(count < 5 for count in counts.values()) or counts[Connect4State.SPECIAL] < 3:
    #        row = random.randint(0, self.__num_rows-1)
    #        col = random.randint(0, self.__num_cols-1)
    #        color = random.choice(colors)

    #        if counts[color] < 5 or color == Connect4State.SPECIAL and counts[Connect4State.SPECIAL] < 3:
    #            self.__grid[row][col] = color
    #            counts[color] += 1



    def get_num_players(self):
        return 2

    def validate_action(self, action: Connect4Action) -> bool:
        col = action.get_col()
        row = action.get_row()

        # valid column
        if col < 0 or col >= self.__num_cols:
            print("maior que col")
            
            return False

        if row < 0 or row >= self.__num_rows:
            print("maior que row")
            return False

        # full column
        if self.__grid[row][col] != Connect4State.EMPTY_CELL:
            print("not an empty cell")
            print (self.__grid[row][col])
            return False
        #if self.__grid[0][row] != Connect4State.EMPTY_CELL:
        #    print("ta full row")
        #    return False
        
        return True

    def update(self, action: Connect4Action):
        col = action.get_col()
        row = action.get_row()

        # drop the checker
        #if self.__grid[row][col] != -1:    
        #    self.__grid[row][col] = -2
        

        # determine if there is a winner
    #    self.__has_winner = self.__check_winner(self.__acting_player)

        # switch to next player
        self.__acting_player = 1 if self.__acting_player == 0 else 0

        self.__turns_count += 1
        
    def __display_cell(self, row, col):
        piece = self.__grid[row][col]
        if piece == 0:
            print(self.__pieces.pop(), end="")
            
            
        elif piece == -1:
            print(' ', end="")       
        elif piece == -2:
            print('O', end="")

                            #DISPLAY CELL COM CORES
    #def __display_cell(self, row, col):
    #    piece = self.__grid[row][col]
    #    if piece == 0:
    #        # define a list of your own color codes
    #        color_palette = ["\033[97m", "\033[92m", "\033[91m", "\033[95m", "\033[30m", "\033[94m"]
    #        # select a random color code from the color palette
    #        random_color = random.choice(color_palette)
    #        # print the "." character in the random color
    #        print(f"{random_color}.\033[0m", end="")
    #    elif piece == -1:
    #        print(' ', end="")

    def __display_numbers(self):
        for col in range(0, self.__num_cols):
            if col < 10:
                print(' ', end="")
            print(col, end="")
        print("")

    def __display_separator(self):
        for col in range(0, self.__num_cols):
            print("--", end="")
        print("-")

    def display(self):
        for row in range(0, self.__num_rows):
            for col in range(0, self.__num_cols):
                
                self.__display_cell(row,col)
                print('', end="")
            print(" ",row)     
            
            print(" ")
        print("")           

    def __is_full(self):
        return self.__turns_count > (self.__num_cols * self.__num_rows)

    def is_finished(self) -> bool:
        return self.__has_winner or self.__is_full()

    def get_acting_player(self) -> int:
        return self.__acting_player

    def clone(self):
        cloned_state = Connect4State()
        cloned_state.__turns_count = self.__turns_count
        cloned_state.__acting_player = self.__acting_player
        cloned_state.__has_winner = self.__has_winner
        for row in range(0, self.__num_rows):
            for col in range(0, self.__num_cols):
                cloned_state.__grid[row][col] = self.__grid[row][col]      
        return cloned_state

    def get_result(self, pos) -> Optional[Connect4Result]:
        if self.__has_winner:
            return Connect4Result.LOOSE if pos == self.__acting_player else Connect4Result.WIN
        if self.__is_full():
            return Connect4Result.DRAW
        return None

    def get_num_rows(self):
        return self.__num_rows

    def get_num_cols(self):
        return self.__num_cols

    def before_results(self):
        pass

    def get_possible_actions(self):
        return list(filter(
            lambda action: self.validate_action(action),
            map(
                lambda pos: Connect4Action(pos),
                range(0, self.get_num_cols()))
        ))

    def sim_play(self, action):
        new_state = self.clone()
        new_state.play(action)
        return new_state
