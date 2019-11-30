def main():
    chicken_factory = AbstractSkewersFactory(ChickenSkewersFactory())
    chicken_factory.make_skewers()
    chicken_factory.check_skewers()

    print("-----")

    pork_factory = AbstractSkewersFactory(PorkSkewersFactory())
    pork_factory.make_skewers()
    pork_factory.check_skewers()


def create_skewers(factory):
    diagram = factory.make_diagram(30, 7)
    rectangle = factory.make_rectangle(4, 1, 22, 5, "yellow")
    text = factory.make_text(7, 3, "Abstract Factory")
    diagram.add(rectangle)
    diagram.add(text)
    return diagram


class AbstractSkewersFactory:
    def __init__(self, skewers_factory):
        self.factory = skewers_factory
        self.skewers_materials = []

    def make_skewers(self):

        self.skewers_materials.append(self.factory.add_food_stuff())
        self.skewers_materials.append(self.factory.add_part())
        self.skewers_materials.append(self.factory.add_taste())

    def check_skewers(self):
        for skewers_material in self.skewers_materials:
            skewers_material.check()

    def add_food_stuff(self):
        pass

    def add_part(self):
        pass

    def add_taste(self):
        pass


class ChickenSkewersFactory(AbstractSkewersFactory):
    def __init__(self):
        super().__init__(self)

    def check_skewers(self):
        for chicken_skewers_material in self.skewers_materials:
            chicken_skewers_material.check()

    @classmethod
    def add_food_stuff(Class):
        return Class.ChickenFoodStuff()

    @classmethod
    def add_part(Class):
        return Class.BreastMeat()

    @classmethod
    def add_taste(Class):
        return Class.SaltTaste()

    class ChickenFoodStuff:
        def __init__(self):
            self.food_stuff = 'chicken'

        def check(self):
            print("food_stuff: {}".format(self.food_stuff))

    class BreastMeat:
        def __init__(self):
            self.part = 'breast_meat'

        def check(self):
            print("part: {}".format(self.part))

    class SaltTaste:
        def __init__(self):
            self.taste = 'salt'

        def check(self):
            print("taste: {}".format(self.taste))


class PorkSkewersFactory(AbstractSkewersFactory):
    def __init__(self):
        super().__init__(self)

    def check_skewers(self):
        for chicken_skewers_material in self.skewers_materials:
            chicken_skewers_material.check()

    @classmethod
    def add_food_stuff(Class):
        return Class.PorkFoodStuff()

    @classmethod
    def add_part(Class):
        return Class.Loin()

    @classmethod
    def add_taste(Class):
        return Class.SauceTaste()

    class PorkFoodStuff:
        def __init__(self):
            self.food_stuff = 'pork'

        def check(self):
            print("food_stuff: {}".format(self.food_stuff))

    class Loin:
        def __init__(self):
            self.part = 'loin'

        def check(self):
            print("part: {}".format(self.part))

    class SauceTaste:
        def __init__(self):
            self.taste = 'sauce'

        def check(self):
            print("taste: {}".format(self.taste))


if __name__ == "__main__":
    main()
