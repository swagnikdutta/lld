from models.Symbol import Symbol
from models.SymbolType import SymbolType


class SymbolX(Symbol):
    def __init__(self):
        super().__init__(SymbolType.X)
