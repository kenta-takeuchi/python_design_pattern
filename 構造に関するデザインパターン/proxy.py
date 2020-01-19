from abc import ABCMeta, abstractmethod
import sys
import time


class Printable(metaclass=ABCMeta):

    @abstractmethod
    def set_printer_name(self, name):
        pass

    @abstractmethod
    def get_printer_name(self):
        pass

    @abstractmethod
    def my_printer(self, string):
        pass


class Printer(Printable):

    def __init__(self, name):
        self.__name = name
        self.__heavy_job('Printerのインスタンス({0})を生成中'.format(self.__name))

    def set_printer_name(self, name):
        self.__name = name

    def get_printer_name(self):
        return self.__name

    def my_printer(self, string):
        print('===' + ' ' + self.__name + ' ' + '===')
        print(string)

    @staticmethod
    def __heavy_job(msg):
        sys.stdout.write(msg)
        for i in range(1, 4):
            try:
                time.sleep(1)
            except InterruptedError:
                pass
            sys.stdout.write('.')
        print('完了')


class PrinterProxy(Printable):

    def __init__(self, name):
        self.__name = name
        self.__real = None

    def set_printer_name(self, name):
        if self.__real is not None:
            self.__real.set_printer_name(name)
        self.__name = name

    def get_printer_name(self):
        return self.__name

    def my_printer(self, string):
        self.__realize()
        self.__real.my_printer(string)

    def __realize(self):
        if self.__real is None:
            self.__real = Printer(self.__name)


def main():
    pp = PrinterProxy('Alice')
    print('名前は現在' + pp.get_printer_name() + 'です。')
    pp.set_printer_name('Bob')
    print('名前は現在' + pp.get_printer_name() + 'です。')
    pp.my_printer('Hello, world.')


if __name__ == '__main__':
    main()
