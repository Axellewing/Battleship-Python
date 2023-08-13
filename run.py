class Board:
    board = []
    def __init__(self, size):
        self.board = [[' ' for _ in range(size)] for _ in range(size)]

if __name__ == "__main__":
    SIZE = input()
    player_board = Board(SIZE)
    print(player_board.board)