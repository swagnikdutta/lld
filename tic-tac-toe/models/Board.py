from models.Symbol import Symbol


class Board:
    def __init__(self, size: int):
        self.size = size
        # board is a grid consisting of Symbol. Symbol is the parent class, base classes are SymbolX and SymbolO
        self.board = [[None for _ in range(size)] for _ in range(size)]

    def is_full(self):
        count = 0
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] is not None:
                    count += 1
        return count == (self.size * self.size)

    def has_winner(self, x, y, symbol: Symbol):
        # check row wise
        count = 0
        for i in range(self.size):
            if self.board[x][i] == symbol:
                count += 1

        if count == self.size:
            return True

        # check column wise
        count = 0
        for i in range(self.size):
            if self.board[i][y] == symbol:
                count += 1

        if count == self.size:
            return True

        # check diagonal
        i, j, count = 0, 0, 0
        lies_on_diagonal = False
        while i < self.size and j < self.size:
            if i == x and j == y:
                lies_on_diagonal = True
            if self.board[i][j] == symbol:
                count += 1
            i, j = i+1, j+1

        if count == self.size and lies_on_diagonal:
            return True

        # check anti-diagonal. Bottom-left to top-right
        i, j, count = self.size - 1, 0, 0
        lies_on_anti_diagonal = False
        while i >= 0 and j < self.size:
            if i == x and j == y:
                lies_on_anti_diagonal = True
            if self.board[i][j] == symbol:
                count += 1
            i, j = i-1, j+1

        if count == self.size and lies_on_anti_diagonal:
            return True

        return False

    def add_symbol(self, x, y, symbol: Symbol) -> bool:
        if self.board[x][y] is not None:
            return False
        self.board[x][y] = symbol
        return True

    def print_board(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] is None:
                    print("   |", end="")
                else:
                    # printing enum here. java has
                    temp = self.board[i][j].symbol_type.value  # has .name() here?
                    print(f" {temp} |", end="")
            print()


