from typing import Optional

from games.connect4.action import Connect4Action
from games.connect4.result import Connect4Result
from games.state import State
from enum import Enum
import random




class Connect4State(State):
    EMPTY_CELL = ' '
    #tem 8 de cada mais 3 wilds, 43 no total
    BLUE = 'B'
    BLACK = 'BK'
    GREEN = 'G'
    RED = 'R'
    WHITE = 'W'
    SPECIAL = 'S'


    def __init__(self, num_rows: int = 13, num_cols: int = 9,is_clone: bool = False):
        super().__init__()

        if num_rows < 4:
            raise Exception("the number of rows must be 4 or over")
        if num_cols < 4:
            raise Exception("the number of cols must be 4 or over")

        """
        the dimensions of the board
        """
        self.__num_rows = num_rows
        self.__num_cols = num_cols

        """
        the grid
        """
        #self.__grid = [[Connect4State.EMPTY_CELL for _i in range(self.__num_cols)] for _j in range(self.__num_rows)]
        self.__grid = [[None for _ in range(self.__num_cols)] for _ in range(self.__num_rows)]
        

        if not is_clone:
            self.place_random_pieces()
        
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

    def place_random_pieces(self):
        colors = [Connect4State.BLUE, Connect4State.BLACK, Connect4State.GREEN, Connect4State.RED, Connect4State.WHITE, Connect4State.SPECIAL]
        
        # initialize counts dictionary with the starting values of the grid
        counts = {}
        for row in range(self.__num_rows):
            for col in range(self.__num_cols):
                cell = self.__grid[row][col]
                if cell in colors:
                    if cell not in counts:
                        counts[cell] = 1
                    else:
                        counts[cell] += 1
                        
        # place up to 5 pieces of each color and 3 of the special ones
        while any(count < 5 for count in counts.values()) or counts.get(Connect4State.SPECIAL, 0) < 3:
            row = random.randint(0, self.__num_rows-1)
            col = random.randint(0, self.__num_cols-1)
            color = random.choice(colors)

            if counts.get(color, 0) < 5 or color == Connect4State.SPECIAL and counts.get(Connect4State.SPECIAL, 0) < 3:
                self.__grid[row][col] = color
                counts[color] = counts.get(color, 0) + 1
            
       
    def __check_winner(self, player):
        # check for 4 across
        for row in range(0, self.__num_rows):
            for col in range(0, self.__num_cols - 3):
                if self.__grid[row][col] == player and \
                        self.__grid[row][col + 1] == player and \
                        self.__grid[row][col + 2] == player and \
                        self.__grid[row][col + 3] == player:
                    return True

        # check for 4 up and down
        for row in range(0, self.__num_rows - 3):
            for col in range(0, self.__num_cols):
                if self.__grid[row][col] == player and \
                        self.__grid[row + 1][col] == player and \
                        self.__grid[row + 2][col] == player and \
                        self.__grid[row + 3][col] == player:
                    return True

        # check upward diagonal
        for row in range(3, self.__num_rows):
            for col in range(0, self.__num_cols - 3):
                if self.__grid[row][col] == player and \
                        self.__grid[row - 1][col + 1] == player and \
                        self.__grid[row - 2][col + 2] == player and \
                        self.__grid[row - 3][col + 3] == player:
                    return True

        # check downward diagonal
        for row in range(0, self.__num_rows - 3):
            for col in range(0, self.__num_cols - 3):
                if self.__grid[row][col] == player and \
                        self.__grid[row + 1][col + 1] == player and \
                        self.__grid[row + 2][col + 2] == player and \
                        self.__grid[row + 3][col + 3] == player:
                    return True

        return False

    def get_grid(self):
        return self.__grid

    def get_num_players(self):
        return 2

    def validate_action(self, action: Connect4Action) -> bool:
        col = action.get_col()

        # valid column
        if col < 0 or col >= self.__num_cols:
            return False

        # full column
        if self.__grid[0][col] != Connect4State.EMPTY_CELL:
            return False

        return True

    def update(self, action: Connect4Action):
        col = action.get_col()

        # drop the checker
        for row in range(self.__num_rows - 1, -1, -1):
            if self.__grid[row][col] < 0:
                self.__grid[row][col] = self.__acting_player
                break

        # determine if there is a winner
        self.__has_winner = self.__check_winner(self.__acting_player)

        # switch to next player
        self.__acting_player = 1 if self.__acting_player == 0 else 0

        self.__turns_count += 1

    def __display_cell(self, row, col):
        print("entered")
        piece = self.__grid[row][col]
        print(f"Piece at ({row}, {col}): {piece}")
        if piece is None:
            print("-", end="")
        else:
            print(piece, end="")

    """ def __display_cell(self, row, col):
        arrayColor = ['I','B','R','G','K','A']
        row1 = [2,4,6]
        row2 = [3,5]
        row4 = [1,3,5,7]
        row5 = [2,4,6]
        row7 = [0,2,4,6,8]

        if row == 0 and col in row1:
            print({
                    Connect4State.EMPTY_CELL: random.choice(arrayColor)
                }[self.__grid[row][col]], end="")
        if row == 1 and col in row2:
            print({
                    Connect4State.EMPTY_CELL: random.choice(arrayColor)
                }[self.__grid[row][col]], end="")
        if row == 2 and col in row1:
            print({
                    Connect4State.EMPTY_CELL: random.choice(arrayColor)
                }[self.__grid[row][col]], end="")
        if row == 3 and col in row4:
            print({
                    Connect4State.EMPTY_CELL: random.choice(arrayColor)
                }[self.__grid[row][col]], end="")                
        if row == 4 and col in row5:
            print({
                    Connect4State.EMPTY_CELL: random.choice(arrayColor)
                }[self.__grid[row][col]], end="")
        if row == 5 and col in row4:
            print({
                    Connect4State.EMPTY_CELL: random.choice(arrayColor)
                }[self.__grid[row][col]], end="")
        if row == 6 and col in row7:
            print({
                    Connect4State.EMPTY_CELL: random.choice(arrayColor)
                }[self.__grid[row][col]], end="")
        if row == 7 and col in row4:
            print({
                    Connect4State.EMPTY_CELL: random.choice(arrayColor)
                }[self.__grid[row][col]], end="")                         
        if row == 8 and col in row5:
            print({
                    Connect4State.EMPTY_CELL: random.choice(arrayColor)
                }[self.__grid[row][col]], end="")
        if row == 9 and col in row4:
            print({
                    Connect4State.EMPTY_CELL: random.choice(arrayColor)
                }[self.__grid[row][col]], end="")
        if row == 10 and col in row1:
            print({
                    Connect4State.EMPTY_CELL: random.choice(arrayColor)
                }[self.__grid[row][col]], end="")
        if row == 11 and col in row2:
            print({
                    Connect4State.EMPTY_CELL: random.choice(arrayColor)
                }[self.__grid[row][col]], end="")                           
        if row == 12 and col in row1:
            print({
                    Connect4State.EMPTY_CELL: random.choice(arrayColor)
                }[self.__grid[row][col]], end="")  """

    def __display_separator(self):
        for col in range(0, self.__num_cols):
            print("--", end="")
        print("-")


    def __display_one_three(self):
        for row in range(0, self.__num_rows):
            if row == 0:
                for col in range(0, 3):
                    self.__display_cell(row, col)
            print("")        
            if row == 1:
                for col in range(0, 2):
                    self.__display_cell(row, col)
                    print(' ',end="")         
          
                
                        
    def __display_all(self):
        for row in range(0, self.__num_rows):
            for col in range(0, self.__num_cols):
                self.__display_cell(row, col)
                print(' ',end="")            
            print("")
   

               
            

    #def display(self):
    #    self.__display_numbers()
    #    self.__display_separator()
#
#        for row in range(0, self.__num_rows):
#            
#            print('|', end="")
#            for col in range(0, self.__num_cols):
#                self.__display_cell(row, col)
##                print('|', end="")    
#            print(" ",row)
#            self.__display_separator()

#        self.__display_numbers()
#        print("")

    def display(self):
        print("Inside display method")
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                self.__display_cell(row, col)
            print()  # print a newline after each row
        


    def __is_full(self):
        return self.__turns_count > (self.__num_cols * self.__num_rows)

    def is_finished(self) -> bool:
        return self.__has_winner or self.__is_full()

    def get_acting_player(self) -> int:
        return self.__acting_player

    def clone(self):
        cloned_state = Connect4State(self.__num_rows, self.__num_cols, True)
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
