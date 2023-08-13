from random import randrange
import random

class Board:
    board = []

    def __init__(self, size):
        self.size = size
        self.clean_board()
        self.ships = self.boat_positions()


    def clean_board(self):
        self.board = [['_' for _ in range(self.size)] for _ in range(self.size)]

    def actions_on_board(self,row,column):
        if [row,column] in self.ships:
            self.board[row][column] = "X"
        else:
            self.board[row][column] = "O"


    def where_ships(self):
        print(self.ships)
        for ship in self.ships:
            self.board[ship[0]][ship[1]] = "."
        self.print_board()
        self.clean_board()
        

    def boat_positions(self):
        boats = []
        for boat_number in range(self.size):
            boat_position = [-1]
            while boat_position[0] == -1:
                random_row = randrange(0, self.size)
                random_column = randrange(0, self.size)
                boat_position = [random_row,random_column]
                if boat_position in boats:
                    boat_position = [-1]
            boats.append(boat_position)
        return boats


    def print_board(self):
        column = "   "
        for x in range(1, self.size + 1):
            column += f"{x} "
        print(column)
        for x in range(self.size):
            row = f"{x + 1}  "
            for y in range(self.size):
                row += f"{self.board[x][y]} "
            print(row)


class Player:
    def __init__(self, name, size):
        self.name = name
        self.board = Board(size)
    
    

        

def check_all_inputs(size_check = False, size = 0):
    ok = "n"

    while ok == "n":
        try:
            check = int(input())
            if size_check and check > 4 and check < 10:
                ok = "y"
            elif size_check and check >= 10:
                print("The description says no more than 10, GOT IT")
            elif check > 0 and check <= size:
                ok = "y"
            else: 
                print("incorrect number, try again man")
        except:
            print("did you see the description, or not :)")

    return check           


if __name__ == "__main__":
    print(random.__version__)
    SIZE = check_all_inputs(True) # 5 - 9
    
    player_board = Board(SIZE)
    player_board.where_ships()





