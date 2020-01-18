from abc import ABCMeta, abstractmethod


class Banner:
    def __init__(self, string):
        self.__string = string

    def show_with_paren(self):
        print('{0} paren'.format(self.__string))

    def show_with_aster(self):
        print('{0} aster'.format(self.__string))


class Printer(metaclass=ABCMeta):
    @abstractmethod
    def print_weak(self):
        pass

    @abstractmethod
    def print_strong(self):
        pass


class BannerPrinter(Printer):
    def __init__(self):
        self.__banner = Banner

    def print_weak(self):
        print("printer_week")

    def print_strong(self):
        print("printer_strong")


class PrinterBanner(Banner):
    def __init__(self, string):
        super().__init__(string)

    def print_week(self):
        self.show_with_aster()

    def print_strong(self):
        self.show_with_aster()


def main():
    banner_printer = BannerPrinter()
    banner_printer.print_strong()
    banner_printer.print_weak()

    printer_banner = PrinterBanner("banner")
    printer_banner.print_strong()
    printer_banner.print_week()


if __name__ == "__main__":
    main()


