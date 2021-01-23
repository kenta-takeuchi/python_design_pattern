import os
import pickle
import random


class Money:
    def __init__(self, money):
        self.money = money

    def __str__(self):
        return str(self.money)


if __name__ == '__main__':
    filename = 'money.pickle'
    if os.path.isfile(filename):
        with open(filename, 'rb') as f:
            money = pickle.load(f)
        print(f"前回のお金は{money}円です")

    money = Money(random.randint(1, 10))
    with open(filename, 'wb') as f:
        pickle.dump(money, f)
    print(f"現在のお金は{money}円です")
