from random import randrange

class Board:
    board = []

    def __init__(self, size):
        self.board = [['_' for _ in range(size)] for _ in range(size)]
        self.size = size
        self.ships = self.boat_positions()


    def boat_positions(self):
        new_size = self.size*self.size
        boats = []
        for boat_number in range(self.size):
            boat_position = -1
            while boat_position == -1:
                boat_position = randrange(new_size)
                if boat_position in boats:
                    boat_position = -1
            boats.append(boat_position)
            # formula of positions (row*10)+column
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
    # board = [1,34,32]
    # row = 0
    # column = 1
    # if (row * 10) + 1 in board:
    #     print(111)

    SIZE = check_all_inputs(True) # 5 - 9
    
    player_board = Board(SIZE)
    player_board.board[0][1] = 'X'
    player_board.print_board()

    original_list = [2]
    digit_list = [int(digit)-1 for digit in str(original_list[0])]
    if len(digit_list) == 1:
        swap = digit_list[0]
        digit_list[0] = 0
        digit_list.append(swap)
    print(digit_list)