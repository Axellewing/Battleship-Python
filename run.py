class Board:
    board = []
    def __init__(self, size):
        self.board = [['_' for _ in range(size)] for _ in range(size)]
        self.size = size
    
    def print_board(self):
        column = "   "
        for x in range(1,self.size+1):
            column += f"{x} "
        print(column)
        for x in range(self.size):
            row = f"{x+1}  "
            for y in range(self.size):
                row += f"{self.board[x][y]} "
            print(row)

if __name__ == "__main__":
    SIZE = int(input())
    # 5 - 9
    player_board = Board(SIZE)
    print(player_board.print_board())