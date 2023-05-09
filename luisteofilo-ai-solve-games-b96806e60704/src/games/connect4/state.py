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
    NORMAL_PIECES = [1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,4,4,4,4,4,4,4,4,5,5,5,5,5,5,5,5,6,6,6]          
    my_shuffle(NORMAL_PIECES)

    grid = [ 
            [IC, IC, (EC,0), IC, (EC,0), IC, (EC,0), IC, IC],
            [IC, IC, IC, (EC,0), IC, (EC,0), IC, IC, IC],
            [IC, IC, (EC,0), IC, (EC,0), IC, (EC,0), IC, IC],
            [IC, (EC,0), IC, (EC,0), IC, (EC,0), IC, (EC,0), IC],
            [IC, IC, (EC,0), IC, (EC,0), IC, (EC,0), IC, IC],
            [IC, (EC,0), IC, (EC,0), IC, (EC,0), IC, (EC,0), IC],
            [(EC, 0), IC, (EC,0), IC, (EC,0), IC, (EC,0), IC, (EC,0)],
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
    chosen_colors_player_0 = []
    chosen_colors_player_1 = []
    score_player_0 = 0
    score_player_1 = 0
    possibleTuples = []
    for i in range(1,7):
            for j in range(5):
                possibleTuples.append((i,j))

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


        self.__grid = Connect4State.grid



        """
        counts the number of turns in the current game
        """
        self.__turns_count = 1

        """
        the index of the current acting player
        """
        self.__acting_player = 0
        self.__notActing_player = 1

        """
        determine if a winner was found already 
        """
        self.__has_winner = False


    def __check_winner(self):
        if self.is_game_over():
            return True

        return False

    def get_grid(self):
        return self.__grid

 
    #def checkIfEC()

    def get_num_players(self):
        return 2

    #FUNÇÃO PARA VER SE A PILHA TEM 5 PEÇAS e update no score
    def check_stack(self):
        for i, row in enumerate(self.__grid):
            for j, element in enumerate(row):
                if isinstance(element, tuple) and element[1] >= 5:
                    if self.__acting_player == 0:
                        Connect4State.score_player_0 += 1
                        print(f"Score inside player 0: {Connect4State.score_player_0}")
                    elif self.__acting_player == 1:
                        Connect4State.score_player_1 += 1
                        print(f"Score inside player 1: {Connect4State.score_player_1}")
                    self.__grid[i][j] = -2

        ##                        VALIDAÇÕES                        ##
    def validate_action(self, action: Connect4Action) -> bool:
        colFrom = action.get_colFrom()
        rowFrom = action.get_rowFrom()
        colTo = action.get_colTo()
        rowTo = action.get_rowTo()

        # valid column
        if colFrom < 0 or colTo < 0 or colFrom >= self.__num_cols or colTo >=self.__num_cols:
            if self.__acting_player == 2:
                print("Less than 0 or Bigger than col")
            return False
             
        # valid row
        if rowFrom < 0 or rowTo < 0 or rowFrom >= self.__num_rows or rowTo >= self.__num_rows:
            if self.__acting_player == 2:
                print("Less than 0 or Bigger than rows")
            return False

        # same piece moving
        if self.__grid[rowFrom][colFrom] == self.__grid[rowTo][colTo]:
            if self.__acting_player == 2:
                print("Can't have a piece of the same color on top of each other")
            return False
        
        # moving an opponents color piece
        if self.__acting_player == 0:
            if isinstance(self.__grid[rowFrom][colFrom], tuple):
                if (self.__grid[rowFrom][colFrom][0]) in Connect4State.chosen_colors_player_1:
                    return False

        if self.__acting_player == 1:
            if isinstance(self.__grid[rowFrom][colFrom], tuple):
                if (self.__grid[rowFrom][colFrom][0]) in Connect4State.chosen_colors_player_0:
                   if self.__acting_player == 2:
                        print("Cant move a piece of the opponents color")
                        return False 

        if self.__grid[rowFrom][colFrom] == -1 or self.grid[rowTo][colTo] == -1:
            if self.__acting_player == 2:
                print("Move the piece to a place where there are pieces")
            return False

       
        if abs(rowFrom - rowTo) > 1:
            if self.__acting_player == 2:
                print("You can only move on top of adjacent pieces 1 !")
            return False

        if abs(rowFrom - rowTo) == 0:
            if abs(colFrom - colTo) > 2:
                if self.__acting_player == 2:
                    print("You can only move on top of adjacent pieces 2 !")
                return False    
            
        if isinstance(self.__grid[rowFrom][colFrom], tuple):
            if (self.__grid[rowFrom][colFrom][0]) > 1:
                if self.__acting_player == 2:
                    print("cant move a stack")
                    return False

        return True

    #GAME OVER#
    def is_game_over(self) -> bool:
        num_remaining_pieces = 0
        for row in range(self.__num_rows):
            for col in range(self.__num_cols):
                if self.__grid[row][col] != -1 and self.__grid[row][col] != -2:
                    num_remaining_pieces += 1
        if num_remaining_pieces <= 6:
            return True


    def update(self, action: Connect4Action):
        colFrom = action.get_colFrom()
        rowFrom = action.get_rowFrom()
        colTo = action.get_colTo()
        rowTo = action.get_rowTo()

        if self.__grid[rowTo][colTo] != -2:
            if isinstance(self.__grid[rowFrom][colFrom], tuple) and isinstance(self.__grid[rowTo][colTo], tuple):
                ecFrom, heightFrom = self.__grid[rowFrom][colFrom]
                ecTo, heightTo = self.__grid[rowTo][colTo]
                
                self.__grid[rowTo][colTo] = (ecFrom, heightTo + 1)
                self.__grid[rowFrom][colFrom] = -2
        
        if self.__grid[rowTo][colTo] == -2:
            if rowFrom < rowTo:
                for i in range(rowTo + 1, self.__num_rows):
                    for x in range(0,self.__num_cols):
                        if (self.__grid[i][x]) != -1:
                            if (self.__grid[i][x]) != -2:
                               
                              
                                if (self.__grid[i][x]) in Connect4State.possibleTuples:
                                    
                                    ecFrom, heightFrom = self.__grid[rowFrom][colFrom]
                                    ecTo, heightTo = self.__grid[i][x]
                                    self.__grid[i][x] = (ecFrom, heightTo + 1)
                                    self.__grid[rowFrom][colFrom] = -2
                                    break
                        else:
                            continue
                    break                    
            if rowFrom > rowTo:
                for i in range(rowTo - 1, self.__num_rows):
                    for x in range(0,self.__num_cols):
                        if (self.__grid[i][x]) != -1:
                            if (self.__grid[i][x]) != -2:
                              
                                if (self.__grid[i][x]) in Connect4State.possibleTuples:
                                   
                                    ecFrom, heightFrom = self.__grid[rowFrom][colFrom]
                                    ecTo, heightTo = self.__grid[i][x]
                                    self.__grid[i][x] = (ecFrom, heightTo + 1)
                                    self.__grid[rowFrom][colFrom] = -2
                                    break
                        else:
                            continue
                    break        
            
            
            
            
            #self.__grid[rowTo][colTo] = (self.__grid([rowFrom][colFrom]), 2) ###AQUI PROF###
   
        # determine if there is a winner
        self.__has_winner = self.__check_winner()

        #Check if there are 5 piece stack
        self.check_stack()

        #check if there are move valid moves
        self.is_game_over()
        # switch to next player
        self.__acting_player = 1 if self.__acting_player == 0 else 0

        self.__turns_count += 1
        
     
    def __display_cell(self, row, col):
        piece = self.__grid[row][col]
        stack = [0,1,2,3,4]
        this_pieces = [1,2,3,4,5,6]
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
        for y in this_pieces:
            if piece == (y,5):
                print('X',end="")
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
        return self.is_game_over()
        

    def get_acting_player(self) -> int:
        return self.__acting_player

    def get_not_acting_player(self) -> int:
        return self.__notActing_player

        

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
            score_0, score_1 = self.score_player_0, self.score_player_1
            if score_0 > score_1:
                print("Player 0 wins")
                return Connect4Result.WIN if pos == 0 else Connect4Result.LOOSE
            elif score_1 > score_0:
                print("Player 1 wins")
                return Connect4Result.WIN if pos == 1 else Connect4Result.LOOSE
            else:
                print("Draw")
                return Connect4Result.DRAW
            #return Connect4Result.LOOSE if pos == self.__acting_player else Connect4Result.WIN
        #if self.__is_full():
        #    return Connect4Result.DRAW
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
