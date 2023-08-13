class Board:
    board = []
    def __init__(self, size):
        self.board = [['_' for _ in range(size)] for _ in range(size)]
        self.size = size
    
    def print_board(self):
        column = "   "
        # row = ""
        for x in range(1,self.size+1):
            column += f"{x} "
        print(column)

if __name__ == "__main__":
    SIZE = int(input())
    player_board = Board(SIZE)
    print(player_board.print_board())