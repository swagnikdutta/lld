from strategies.fly import FlyStrategy
from strategies.quack import QuackStrategy


class Duck:
    def __init__(self, qs: QuackStrategy, fs: FlyStrategy):
        self.quack_strategy = qs
        self.fly_strategy = fs

    def quack(self):
        self.quack_strategy.quack()

    def fly(self):
        self.fly_strategy.fly()
