from strategies.fly import FlyStrategy


# concrete class
class FlyHigh(FlyStrategy):
    def fly(self):
        print(f"Flying at 9000 meters")


class FlyLow(FlyStrategy):
    def fly(self):
        print("Flying above your head")
