from abc import ABC, abstractmethod


class QuackStrategy(ABC):
    @abstractmethod
    def quack(self):
        pass

