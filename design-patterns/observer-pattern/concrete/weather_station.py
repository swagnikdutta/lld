import random
import time

from interface.observable import Observable
from interface.observer import Observer


class WeatherStation(Observable):
    def __init__(self):
        self.temperature = None
        self.observers = []

    def add(self, o: Observer):
        self.observers.append(o)

    def remove(self, o: Observer):
        if o in self.observers:
            self.observers.remove(o)

    def notify(self):
        for observer in self.observers:
            observer.update()

    def get_temperature(self):
        return self.temperature

    def set_temperature(self, temp):
        self.temperature = temp
        self.notify()

    def activate_sensors(self):
        count = 5
        while count:
            temp = random.uniform(-60, 50)
            self.set_temperature(temp)
            time.sleep(3)
            count -= 1


