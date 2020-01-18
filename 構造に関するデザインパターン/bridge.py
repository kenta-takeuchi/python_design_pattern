import random
from abc import ABCMeta, abstractmethod


class DisplayFunc(object):
    """
    基本的な機能を実装する
    """
    def __init__(self, impl):
        # 意図しないImplが渡された場合は例外を発生させる
        if not isinstance(impl, DisplayImpl):
            raise TypeError()
        self.impl = impl

    def open(self):
        self.impl.raw_open()

    def print_body(self):
        self.impl.raw_print()

    def close(self):
        self.impl.raw_close()

    def display(self):
        self.open()
        self.print_body()
        self.close()


class DisplayCountFunc(DisplayFunc):
    """
    DisplayFuncインターフェースの機能を実装するクラス
    """
    def __init__(self, impl):
        super(DisplayCountFunc, self).__init__(impl)

    def multi_display(self, times):
        """
        引数で指定した回数分だけ文字列を繰り返し表示する
        :param times:繰り返し表示させる回数
        :return: times分だけ文字列を出力する
        """
        self.open()
        for _ in range(times):
            self.print_body()
        self.close()


class DisplayRandomFunc(DisplayFunc):
    """
    DisplayFuncインターフェースの機能を実装したクラス
    """
    def __init__(self, impl):
        super(DisplayRandomFunc, self).__init__(impl)

    def random_display(self, times):
        """
        引数で指定した数以下のランダムな回数分だけ文字列を繰り返し表示する
        例：5を渡された場合、1〜5回までをランダムに表示する
        :param times:繰り返し表示させる回数の最大値
        :return: times分だけ文字列を出力する
        """
        self.open()
        t = random.randint(0, times)
        for _ in range(t):
            self.print_body()
        self.close()


class DisplayImpl(metaclass=ABCMeta):
    """
    インターフェース
    """
    @abstractmethod
    def raw_open(self):
        pass

    @abstractmethod
    def raw_print(self):
        pass

    @abstractmethod
    def raw_close(self):
        pass


class DisplayStringImpl(DisplayImpl):
    """
    インターフェースを実装したクラス
    """
    def __init__(self, string):
        self.string = string
        self.width = len(string)

    def raw_open(self):
        self.print_line()

    def raw_print(self):
        print("|{0}|".format(self.string))

    def raw_close(self):
        self.print_line()
        print("")

    def print_line(self):
        line = '-' * self.width
        print("+{0}+".format(line))


class NotDisplayImpl:
    def __init__(self):
        pass


def main():
    d1 = DisplayFunc(DisplayStringImpl("DisplayFunc"))
    d2 = DisplayCountFunc(DisplayStringImpl("DisplayCountFunc"))
    d3 = DisplayRandomFunc(DisplayStringImpl("DisplayRandomFunc"))
    d1.display()
    d2.display()
    d2.multi_display(3)
    d3.random_display(10)

    # 意図しないImplを渡す
    DisplayRandomFunc(NotDisplayImpl)


if __name__ == '__main__':
    main()
