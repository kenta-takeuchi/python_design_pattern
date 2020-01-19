from abc import ABCMeta, abstractmethod


class Display(metaclass=ABCMeta):
    """
    抽象クラス
    """
    @abstractmethod
    def get_columns(self):
        pass

    @abstractmethod
    def get_rows(self):
        pass

    @abstractmethod
    def get_row_text(self, i):
        pass

    def show(self):
        for i in range(self.get_rows()):
            print(self.get_row_text(i))


class StringDisplay(Display):
    """
    文字列を1列だけ表示するクラス
    """
    def __init__(self, string):
        self.__string = string

    def get_columns(self):
        return len(self.__string)

    def get_rows(self):
        return 1

    def get_row_text(self, row):
        if row == 0:
            return self.__string
        else:
            return None


class Border(Display, metaclass=ABCMeta):
    """
    抽象クラス
    """
    def _border(self, display):
        self._display = display


class SideBorder(Border):
    """
    左右に
    """

    def __init__(self, display, ch):
        self.display = display
        self.__border_char = ch

    def get_columns(self):
        return 1 + self.display.get_columns() + 1

    def get_rows(self):
        return self.display.get_rows()

    def get_row_text(self, row):
        return self.__border_char + \
            self.display.get_row_text(row) + \
            self.__border_char


class FullBorder(Border):

    def __init__(self, display):
        self.display = display

    def get_columns(self):
        return 1 + self.display.get_columns() + 1

    def get_rows(self):
        return 1 + self.display.get_rows() + 1

    def get_row_text(self, row):
        if row == 0:
            return '+' + self._make_line('-', self.display.get_columns()) + '+'
        elif row == self.display.get_rows() + 1:
            return '+' + self._make_line('-', self.display.get_columns()) + '+'
        else:
            return '|' + self.display.get_row_text(row - 1) + '|'

    @staticmethod
    def _make_line(ch, count):
        buf = []
        for i in range(0, count):
            buf.append(ch)
        return ' '.join(buf)


def main():
    b1 = StringDisplay('Hello, world')
    b2 = SideBorder(b1, '#')
    b3 = FullBorder(b2)
    b4 = SideBorder(
        FullBorder(
            FullBorder(
                SideBorder(
                    FullBorder(
                        StringDisplay('こんにちは。')
                    ), '*'
                )
            )
        ), '/'
    )

    b1.show()
    b2.show()
    b3.show()
    b4.show()


if __name__ == "__main__":
    main()
