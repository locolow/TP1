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
    EC = 0
    IC = -1
    PLAYED_CELL= -2
    BLUE = 1
    BLACK = 2
    GREEN = 3
    RED = 4
    WHITE = 5
    SPECIAL = 6
    #NORMAL_PIECES = [
    #        Piece(1), Piece(1), Piece(1), Piece(1), Piece(1), Piece(1), Piece(1), Piece(1),
    #        Piece(2), Piece(2), Piece(2), Piece(2), Piece(2), Piece(2), Piece(2), Piece(2),
    #        Piece(3), Piece(3), Piece(3), Piece(3), Piece(3), Piece(3), Piece(3), Piece(3),
    #        Piece(4), Piece(4), Piece(4), Piece(4), Piece(4), Piece(4), Piece(4), Piece(4),
    #        Piece(5), Piece(5), Piece(5), Piece(5), Piece(5), Piece(5), Piece(5), Piece(5),
    #        Piece(6), Piece(6), Piece(6)
    #    ]
    NORMAL_PIECES = [1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,4,4,4,4,4,4,4,4,5,5,5,5,5,5,5,5,6,6,6]          
    my_shuffle(NORMAL_PIECES)

    grid = [ 
            [IC, IC, (EC,0), IC, (EC,0), IC, (EC,0), IC, IC],
            [IC, IC, IC, (EC,0), IC, (EC,0), IC, IC, IC],
            [IC, IC, (EC,0), IC, (EC,0), IC, (EC,0), IC, IC],
            [IC, (EC,0), IC, (EC,0), IC, (EC,0), IC, (EC,0), IC],
            [IC, IC, (EC,0), IC, (EC,0), IC, (EC,0), IC, IC],
            [IC, (EC,0), IC, (EC,0), IC, (EC,0), IC, (EC,0), IC],
            [(EC,0), IC, (EC,0), IC, (EC,0), IC, (EC,0), IC, (EC,0)],
            [IC, (EC,0), IC, (EC,0), IC, (EC,0), IC, (EC,0), IC],
            [IC, IC, (EC,0), IC, (EC,0), IC, (EC,0), IC, IC],
            [IC, (EC,0), IC, (EC,0), IC, (EC,0), IC, (EC,0), IC],
            [IC, IC, (EC,0), IC, (EC,0), IC, (EC,0), IC, IC],
            [IC, IC, IC, (EC,0), IC, (EC,0), IC, IC, IC],
            [IC, IC, (EC,0), IC, (EC,0), IC, (EC,0), IC, IC]
        ]
    num_rows = 13    
    num_cols = 9
    for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == (EC,0):
                    grid[i][j] = (NORMAL_PIECES.pop(0),0)

    available_colors = [1,2,3,4,5]
    chosen_colors = []
    

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
        for x in [0,1,2,3,4]:
            self.__singlePiece = [(1,x),(2,x),(3,x),(4,x),(5,x),(6,x)]


        self.__grid = Connect4State.grid

        self.__chosenColors = Connect4State.chosen_colors
        

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

 


    def get_num_players(self):
        return 2

    def validate_action(self, action: Connect4Action) -> bool:
        colFrom = action.get_colFrom()
        rowFrom = action.get_rowFrom()
        colTo = action.get_colTo()
        rowTo = action.get_rowTo()

        # valid column
        if colFrom < 0 or colTo < 0 or colFrom >= self.__num_cols or colTo >=self.__num_cols:
            if self.__acting_player == 1:
                print("Less than 0 or Bigger than col")
            return False
             

        if rowFrom < 0 or rowTo < 0 or rowFrom >= self.__num_rows or rowTo >= self.__num_rows:
            if self.__acting_player == 1:
                print("Less than 0 or Bigger than rows")
            return False

        # full column
        if self.__grid[rowFrom][colFrom] == self.__grid[rowTo][colTo]:
            if self.__acting_player == 1:
                print("Can't have a piece of the same color on top of each other")
            return False
        
        if self.__grid[rowFrom][colFrom] == Connect4State.IC or self.grid[rowTo][colTo] == Connect4State.IC:
            if self.__acting_player == 1:
                print("Move the piece to a place where there are pieces")
            return False

       
        if abs(rowFrom - rowTo) > 1:
            if self.__acting_player == 1:
                print("You can only move on top of adjacent pieces 1 !")
            return False

        if abs(rowFrom - rowTo) == 0:
            if abs(colFrom - colTo) > 2:
                if self.__acting_player == 1:
                    print("You can only move on top of adjacent pieces 2 !")
                return False    

        if self.__grid[rowTo][colTo] == Connect4State.PLAYED_CELL:
            if rowFrom < rowTo:
                # move made from above, check nearest empty cell below
                for i in range(rowTo+1, self.__num_rows): ##PEGAS NISTO E FAZES FOR RANGE DAS ROWS ANDA UMA PARA BAIXO ATÉ ENCONTRAR UMA EC
                    if self.__grid[i][colTo + 1] == Connect4State.EC or self.__grid[i][colTo - 1] == Connect4State.EC:
                        return True
                    elif i == self.__num_rows-1:
                        if self.__acting_player == 1:    
                            print("No pieces below that to be played")
                        return False

            elif rowFrom > rowTo:
                # move made from below, check nearest empty cell above
                for i in range(rowTo-1, -1, -1):
                    if self.__grid[i][colTo + 1] == Connect4State.EC or self.__grid[i][colTo -1 ] == Connect4State.EC:
                        return True
                    elif i == 0:
                        if self.__acting_player == 1:    
                            print("No pieces above that to be played") 
                        return False
            
        print(f"Col From: {colFrom} Row From:{rowFrom}")
        print(f"Col To: {colTo} Row To: {rowTo}")
        return True

    def update(self, action: Connect4Action):
        colFrom = action.get_colFrom()
        rowFrom = action.get_rowFrom()
        colTo = action.get_colTo()
        rowTo = action.get_rowTo()

        if isinstance(self.__grid[rowFrom][colFrom], tuple) and isinstance(self.__grid[rowTo][colTo], tuple):
            ecFrom, heightFrom = self.__grid[rowFrom][colFrom]
            ecTo, heightTo = self.__grid[rowTo][colTo]
            
            if ecFrom != ecTo:
                # move is between two different ECs
                # move is valid and height of stack can be increased
                self.__grid[rowTo][colTo] = (ecFrom, heightTo + 1)
                self.__grid[rowFrom][colFrom] = -2
            #self.__grid[rowTo][colTo] = (self.__grid([rowFrom][colFrom]), 2) ###AQUI PROF###
        
                        
                
                
        

        # determine if there is a winner
        #self.__has_winner = self.__check_winner(self.__acting_player)

        # switch to next player
        self.__acting_player = 1 if self.__acting_player == 0 else 0

        self.__turns_count += 1
        
     
    def __display_cell(self, row, col):
        piece = self.__grid[row][col]
        stack = [0,1,2,3,4]
        for x in stack:
            if piece == (1,x):
                print(f'BL{x}', end="")  
            if piece == (2,x):
                print(f'BK{x}', end="")
            if piece == (3,x):
                print(f'GR{x}', end="")
            if piece == (4,x):
                print(f'RE{x}', end="")
            if piece == (5,x):
                print(f'WH{x}', end="")
            if piece == (6,x):
                print(f'SP{x}', end="")                  
        if piece == -1:
            print(' ', end="")       
        if piece == -2:
            print('X', end="")
        #print(piece,end="")
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
        #return self.__turns_count > (self.__num_cols * self.__num_rows)
        pass

    def is_finished(self) -> bool:
        #return self.__has_winner or self.__is_full()
        pass

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
