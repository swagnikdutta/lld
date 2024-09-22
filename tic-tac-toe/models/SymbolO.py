from models.Symbol import Symbol
from models.SymbolType import SymbolType


class SymbolO(Symbol):
    def __init__(self):
        super().__init__(SymbolType.O)