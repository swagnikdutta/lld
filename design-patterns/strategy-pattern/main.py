from concrete.fly_strategy import FlyLow, FlyHigh
from concrete.quack_strategy import NormalQuack, LoudQuack
from duck import Duck

if __name__ == '__main__':
    normal_quack = NormalQuack()
    loud_quack = LoudQuack()

    low_fly = FlyLow()
    high_fly = FlyHigh()

    # duck with normal quack and low flying capability
    duck1 = Duck(normal_quack, low_fly)
    duck1.quack()
    duck1.fly()
    print()

    # duck with loud quack and low flying capability
    duck2 = Duck(loud_quack, low_fly)
    duck2.quack()
    duck2.fly()
    print()

    # duck with loud quack and high-flying capability
    duck3 = Duck(loud_quack, high_fly)
    duck3.quack()
    duck3.fly()



