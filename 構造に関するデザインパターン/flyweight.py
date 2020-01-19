import sys


def main():
    h1 = Hoge1()
    h2 = Hoge2()

    h1.add_att7()
    print(h1.att7)

    # h2.add_att7()  # => AttributeError
    # print(h2.att7)

    # calc memory size
    print(h1.__dict__)
    memory_size_h1 = sys.getsizeof(h1) + sys.getsizeof(h1.__dict__)

    # print(h2.__dict__)  # => AttributeError
    memory_size_h2 = sys.getsizeof(h2)

    print("h1: {}, h2: {}".format(memory_size_h1, memory_size_h2))


class Hoge1:

    # __slots__ = ("att1", "att2", "att3", "att4", "att5", "att6")

    def __init__(self, att1=0, att2=0, att3=0, att4=0, att5=0, att6=0):
        self.att1 = att1
        self.att2 = att2
        self.att3 = att3
        self.att4 = att4
        self.att5 = att5
        self.att6 = att6

    def add_att7(self):
        self.att7 = 7


class Hoge2:

    __slots__ = ("att1", "att2", "att3", "att4", "att5", "att6")

    def __init__(self, att1=0, att2=0, att3=0, att4=0, att5=0, att6=0):
        self.att1 = att1
        self.att2 = att2
        self.att3 = att3
        self.att4 = att4
        self.att5 = att5
        self.att6 = att6

    def add_att7(self):
        self.att7 = 7


if __name__ == "__main__":
    main()
