from abc import ABC, abstractmethod

from interface.observer import Observer


class Observable(ABC):
    @abstractmethod
    def add(self, o: Observer):
        pass

    @abstractmethod
    def remove(self, o: Observer):
        pass

    @abstractmethod
    def notify(self):
        pass
