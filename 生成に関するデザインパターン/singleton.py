def main():
    singleton_1 = Singleton()
    print(singleton_1)

    singleton_2 = Singleton()
    print(singleton_2)
    print(singleton_1 == singleton_2)


class Singleton:
    _unique_instance = None

    @classmethod
    def __new__(cls, *args, **kwargs):
        if not cls._unique_instance:
            cls._unique_instance = super(Singleton, cls).__new__(cls)

        return cls._unique_instance


if __name__ == "__main__":
    main()
