from abc import ABC, abstractmethod


class FlyStrategy(ABC):
    @abstractmethod
    def fly(self):
        pass

