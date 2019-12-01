import abc


def main():
    factory = ConcreteCreator()
    food_1 = factory.factory_method('bread', 'flour')
    food_2 = factory.factory_method('fried_rice', 'rice')

    print(food_1.get_name(), food_1.get_material())

    print("-----")

    print(food_2.get_name(), food_2.get_material())


def create_skewers(factory):
    diagram = factory.make_diagram(30, 7)
    rectangle = factory.make_rectangle(4, 1, 22, 5, "yellow")
    text = factory.make_text(7, 3, "Abstract Factory")
    diagram.add(rectangle)
    diagram.add(text)
    return diagram


class AbstractCreator:
    @abc.abstractmethod
    def factory_method(self, name, material):
        pass


class Food:
    @abc.abstractmethod
    def get_name(self):
        pass

    @abc.abstractmethod
    def get_material(self):
        pass


class ConcreteCreator(AbstractCreator):
    def factory_method(self, name, material):
        return ConcreteFood(name, material)


class ConcreteFood(Food):
    def __init__(self, name, material):
        self.name = name
        self.material = material

    def get_name(self):
        return self.name

    def get_material(self):
        return self.material


if __name__ == "__main__":
    main()
