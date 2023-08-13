from random import randrange

class Board:
    board = []

    def __init__(self, size):
        self.board = [['_' for _ in range(size)] for _ in range(size)]
        self.size = size
        self.ships = self.boat_positions()


    def boat_positions(self):
        new_size = self.size**self.size
        boats = []
        for boat_number in range(self.size):
            boat = -1
            while boat == -1:
                position = randrange(new_size)
                print(position)
        return []


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
    SIZE = check_all_inputs(True) # 5 - 9
    
    player_board = Board(SIZE)
    player_board.print_board()