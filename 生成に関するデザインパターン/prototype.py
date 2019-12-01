import copy


class Point:

    __slots__ = ("x", "y")

    def __str__(self):
        return "x: {}, y: {}".format(self.x, self.y)

    def __init__(self, x, y):
        self.x = x
        self.y = y


def main():
    point_original = Point(10, 20)

    point_clone = copy.deepcopy(point_original)
    print(point_clone)
    point_clone.x = 4
    point_clone.y = 8
    print(point_clone)

    point_clone = point_original.__class__(5, 10)
    print(point_clone)


if __name__ == "__main__":
    main()
