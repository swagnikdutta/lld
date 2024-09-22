from collections import deque

from models.Player import Player
from models.Symbol import Symbol
from models.SymbolO import SymbolO
from models.SymbolX import SymbolX
from models.Board import Board


class TicTacToeGame:
    def __init__(self):
        self.board = None
        self.players = deque()

    def initialize_game(self):
        player1 = Player("Swagnik", SymbolX())
        player2 = Player("Poku", SymbolO())

        self.players.append(player1)
        self.players.append(player2)

        self.board = Board(3)

    def start(self):
        while True:
            self.board.print_board()
            player = self.players.pop()

            print(f"Player {player.name}'s ({player.symbol.symbol_type.value}) turn. Enter position: x,y\n")
            x, y = map(int, input().split(","))

            if x < 0 or y < 0 or x >= self.board.size or y >= self.board.size:
                print(f"Invalid position. Try again!")
                self.players.append(player)
                continue

            # remember why you're sending the base class Symbol.
            success = self.board.add_symbol(x, y, player.symbol)
            if not success:
                print(f"Position not empty. Try again!")
                self.players.append(player)
                continue

            has_winner = self.board.has_winner(x, y, player.symbol)
            if has_winner:
                self.board.print_board()
                print(f"Player {player.name} wins!")
                break

            is_full = self.board.is_full()
            if is_full:
                self.board.print_board()
                print("Game ends in draw!")
                break

            self.players.appendleft(player)
