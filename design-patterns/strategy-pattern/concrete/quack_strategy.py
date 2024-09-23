# concrete class
from strategies.quack import QuackStrategy


class LoudQuack(QuackStrategy):
    def quack(self):
        print(f"QUACK QUACK QUACK")


# concrete class
class NormalQuack(QuackStrategy):
    def quack(self):
        print(f"quack quack quack")

