from abc import ABCMeta, abstractmethod


class Entry(metaclass=ABCMeta):
    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_size(self):
        pass

    def add(self, entry):
        raise Exception()

    def print_list(self):
        self._print_list()

    @abstractmethod
    def _print_list(self, prefix=''):
        pass

    def __str__(self):
        return "{0} ({1})".format(self.get_name(), self.get_size())


class File(Entry):
    def __init__(self, name, size):
        self.__name = name
        self.__size = size

    def get_name(self):
        return self.__name

    def get_size(self):
        return self.__size

    def _print_list(self, prefix=''):
        print("{0}/{1}".format(prefix, self))


class Directory(Entry):
    def __init__(self, name):
        self.__name = name
        self.__directory = []

    def get_name(self):
        return self.__name

    def get_size(self):
        size = 0
        for d in self.__directory:
            size += d.get_size()
        return size

    def add(self, entry):
        if not isinstance(entry, Entry):
            raise TypeError()
        entry.path = self.__name
        self.__directory.append(entry)

    def _print_list(self, prefix=''):
        print(prefix + "/" + str(self))
        for e in self.__directory:
            e._print_list(prefix + '/' + self.__name)


def main():
    try:
        print("Making root entries...")
        root_dir = Directory("root")
        bin_dir = Directory("bin")
        tmp_dir = Directory("tmp")
        usr_dir = Directory("usr")

        root_dir.add(bin_dir)
        root_dir.add(tmp_dir)
        root_dir.add(usr_dir)

        bin_dir.add(File("vi", 10000))
        bin_dir.add(File("latex", 20000))
        root_dir.print_list()

        print("")
        print("Making user entries...")
        yuki = Directory("yuki")
        hanako = Directory("hanako")
        tomura = Directory("tomura")

        usr_dir.add(yuki)
        usr_dir.add(hanako)
        usr_dir.add(tomura)

        yuki.add(File("diary.html", 100))
        yuki.add(File("Composite.java", 200))
        hanako.add(File("memo.tex", 300))
        tomura.add(File("game.doc", 400))
        tomura.add(File("junk.mail", 500))
        root_dir.print_list()

    except TypeError as ex:
        print(ex.with_traceback())


if __name__ == '__main__':
    main()
