from abc import ABCMeta, abstractmethod


def main():
    a = LimitSupport('A', 50)
    b = LimitSupport('B', 100)
    c = SpecialSupport('C', 429)
    d = LimitSupport('D', 200)
    e = OddSupport('E')
    f = NoSupport('F')

    a.set_next(
        b
    ).set_next(
        c
    ).set_next(
        d
    ).set_next(
        e
    ).set_next(
        f
    )

    for i in range(0, 500, 33):
        a.support(Trouble(i))


class Trouble:
    """
    イベントを表すクラス
    """
    def __init__(self, number):
        self.number = number

    def __str__(self):
        return '[Trouble {}]'.format(self.number)


class Support(metaclass=ABCMeta):
    """
    トラブルを解消するサポート抽象クラス
    """
    def __init__(self, name):
        self.name = name
        self.next = None

    def set_next(self, next):
        self.next = next
        return next

    def support(self, trouble):
        """
        トラブルが解決できる場合、解決する。
        解決できないトラブルの場合は次のサポートクラスにトラブルを引き渡す。
        :param trouble: トラブルインスタンス
        """
        if self.resolve(trouble):
            self.done(trouble)
        elif self.next is not None:
            self.next.support(trouble)
        else:
            self.fail(trouble)

    @abstractmethod
    def resolve(self, trouble):
        pass

    def done(self, trouble):
        """
        トラブルを無事に解決させる。
        :param trouble: トラブルインスタンス
        """
        print('{} is resolved by {}.'.format(trouble, self))

    @classmethod
    def fail(cls, trouble):
        """
        トラブルの解決に失敗する。
        :param trouble: トラブルインスタンス
        """
        print('{} cannot be resolved.'.format(trouble))

    def __str__(self):
        return '[{}]'.format(self.name)


class NoSupport(Support):
    """
    サポートで解決できないトラブルを受け取る
    """
    def __init__(self, name):
        super().__init__(name)

    def resolve(self, trouble):
        return False


class LimitSupport(Support):
    """
    Limit未満のトラブル番号を解決できるサポートクラス
    """
    def __init__(self, name, limit):
        super().__init__(name)
        self.limit = limit

    def resolve(self, trouble):
        if trouble.number < self.limit:
            return True
        return False


class OddSupport(Support):
    """
    奇数のトラブル番号を解決できるサポートクラス
    """
    def __init__(self, name):
        super().__init__(name)

    def resolve(self, trouble):
        if trouble.number % 2 == 1:
            return True
        return False


class SpecialSupport(Support):
    """
    ある特的のトラブル番号を解決できるサポートクラス
    """
    def __init__(self, name, number):
        super().__init__(name)
        self.number = number

    def resolve(self, trouble):
        if trouble.number == self.number:
            return True
        return False


if __name__ == '__main__':
    main()
