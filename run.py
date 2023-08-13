from random import randrange

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
            return 1
        else:
            self.board[row][column] = "O"
            return 0


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

def check_all_inputs(size_check = False, size = 0):
    ok = "n"

    while ok == "n":
        try:
            check = int(input())
            if size_check and check > 4 and check < 10:
                ok = "y"
            elif size_check and check >= 10:
                print("The description says from 5 to 9, GOT IT")
            elif check > 0 and check <= size:
                ok = "y"
            else: 
                print("incorrect number, try again man")
        except:
            print("did you see the description, or not :)")

    return check

class Player:
    moves = []
    apponent_board = []
    points = 0
    def __init__(self, name, size):
        self.name = name
        self.board = Board(size)
    
    def add_apponent_board(self,apponent_board):
        self.apponent_board = apponent_board

    def show_board(self):
        self.board.print_board()

    def show_points(self):
        print(f"{self.name}: {self.points}")

    def move(self):
        check = False
        while check == False:
            print("What row?")
            row = check_all_inputs(size=self.board.size) - 1
            print("And column is?")
            column = check_all_inputs(size=self.board.size) - 1
            if [row,column] in self.moves:
                print("Take some memory pills, it's already been that move.")
            else:
                self.moves.append([row,column])
                check = True
        self.points += self.apponent_board.actions_on_board(row,column)

class Computer(Player):
    def move(self):
        check = False
        prev_points = self.points
        while check == False:
            row = randrange(self.board.size)
            column = randrange(self.board.size)
            if [row,column] in self.moves:
                continue
            else:
                self.moves.append([row,column])
                check = True
        self.points += self.apponent_board.actions_on_board(row,column)
        if prev_points == self.points:
            print("Computer miss")
        else:
            print("Computer got you!")
                   


if __name__ == "__main__":
    print('''--------------------------------
  Welcome to my 
  ULTIMATE BATTLESHIPS!!!
  This game isn't made to love you,
  so don't give up !)
--------------------------------
  What size of board do you want from 5 to 9?''')
    SIZE = check_all_inputs(True) # 5 - 9
    print("What is your name LOSER?")
    name = input()
    print(f'''All right, now you and computer have {SIZE} ships.
I'm sure you'll lose.
Here is your board:''')
    player = Player(name,SIZE)
    computer = Computer("WINNER-Comp",SIZE)
    computer.add_apponent_board(player.board)
    player.add_apponent_board(computer.board)
    


    
    





