from random import randrange

class Board:
    board = []


    def __init__(self, size):
        self.size = size
        self.clean_board(size)
        self.ships = self.boat_positions()


    def clean_board(self, size):
        self.board = [['_' for _ in range(size)] for _ in range(size)]


    def actions_on_board(self,row,column):
        if [row,column] in self.ships:
            self.board[row][column] = "X"
            return 1
        else:
            self.board[row][column] = "O"
            return 0


    def where_ships(self):
        for ship in self.ships:
            self.board[ship[0]][ship[1]] = "."
        self.print_board()
        self.clean_board(size = self.size)        


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


    def show_board(self, what_to_see = 0):
        if what_to_see == 0:
            self.board.print_board()
        else:
            self.board.where_ships()


    def show_points(self):
        print(f"{self.name}: {self.points}")


    def check_moves(self,row,column):
        for move in self.moves:
            if row == move[0] and column == move[1]:
                return False
        return True


    def move(self):
        check = False
        prev_points = self.points
        new_move = []
        while check == False:
            print("What row?")
            row = check_all_inputs(size = self.board.size) - 1
            print("And column is?")
            column = check_all_inputs(size = self.board.size) - 1
            if self.check_moves(row,column) is False:
                print("Take some memory pills, it's already been that move.")
                print(self.moves)
            else:
                new_move = [row,column]
                self.moves.append(new_move)
                check = True
        self.points += self.apponent_board.actions_on_board(row,column)
        print(f"{self.name} guessed: {[new_move[0] + 1,new_move[1] + 1]}")
        if prev_points == self.points:
            print(f"{self.name} miss")
        else:
            print(f"{self.name} try to not lose")


class Computer(Player):
    moves = []


    def move(self):
        check = False
        prev_points = self.points
        new_move = []
        while check == False:
            row = randrange(self.board.size)
            column = randrange(self.board.size)
            if self.check_moves(row,column) is False:
                continue
            else:
                new_move = [row,column]
                self.moves.append(new_move)
                check = True
        self.points += self.apponent_board.actions_on_board(row,column)
        print(f"{self.name} guessed: {[new_move[0] + 1,new_move[1] + 1]}")
        if prev_points == self.points:
            print(f"{self.name} miss")
        else:
            print(f"{self.name} got you!")
                   

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
Amd you can tipe only 1 - {SIZE} numbers.
I'm sure you'll lose.
Here is your board:''')
    player = Player(name,SIZE)
    computer = Computer("WINNER-Comp",SIZE)
    computer.add_apponent_board(player.board)
    player.add_apponent_board(computer.board)
    player.show_board(what_to_see = 1)
    print("Computer board:")
    computer.show_board()

    the_end = False
    while the_end == False:
        player.show_points()
        computer.show_points()
        player.move()
        player.show_board()
        if player.points == SIZE:
            print("WHAT??? It's mistake... Okay SEE you next time!!!")
            the_end = True
            break
        computer.move()
        computer.show_board()
        if computer.points == SIZE:
            print("Exactly what I said!!!")
            the_end = True
            break
    


    
    





