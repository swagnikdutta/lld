from models.SymbolType import SymbolType


class Symbol:
    def __init__(self, symbol_type: SymbolType):
        self.symbol_type = symbol_type
