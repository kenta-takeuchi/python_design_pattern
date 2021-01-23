class Presidents:
    __names = ("George", "John", "Thomas")

    def __init__(self, first=None):
        self.index = (-1 if first is None else Presidents.__names.index(first) - 1)

    def __call__(self):
        self.index += 1
        if self.index < len(Presidents.__names):
            return Presidents.__names[self.index]
        raise StopIteration()


for president in iter(Presidents(), None):
    print(president, end="")


class Bag:
    def __init__(self, items=None):
        self.__bag = {}
        if items is not None:
            for item in items:
                self.add(item)

    def add(self, item):
        self.__bag[item] = self.__bag.get(item, 0) + 1

    def __delitem__(self, item):
        if self.__bag.get(item) is not None:
            self.__bag[item] -= 1
            if self.__bag[item] <= 0:
                del self.__bag[item]
        else:
            raise KeyError(str(item))

    def count(self, item):
        return self.__bag.get(item, 0)

    def __len__(self):
        return sum(count for count in self.__bag.values())

    def __contains__(self, item):
        return item in self.__bag

    def __iter__(self):
        for item, count in self.__bag.items():
            for _ in range(count):
                yield item
