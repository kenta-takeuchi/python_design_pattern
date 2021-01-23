from abc import ABCMeta, abstractmethod
from pathlib import Path


class Command(metaclass=ABCMeta):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def display(self):
        pass


class FileTouchCommand(Command):
    def __init__(self, filename, receiver_object):
        self.__filename = filename
        self.__receiver = receiver_object

    def execute(self):
        self.__receiver.create_file(self.__filename)

    def display(self):
        print("% touch {0}".format(self.__filename))


class ChmodCommand(Command):
    def __init__(self, filename, permission, receive_object):
        self.__filename = filename
        self.__permission = permission
        self.__receiver = receive_object

    def execute(self):
        self.__receiver.change_file_mode(self.__filename, self.__permission)

    def display(self):
        permission = format(self.__permission, 'o')
        print("% chmod {0} {1}".format(permission, self.__filename))


class FileOperator(object):
    def create_file(self, filename):
        Path(filename).touch()

    def change_file_mode(self, filename, permission):
        Path(filename).chmod(permission)


class CompositeCommand(Command):
    def __init__(self):
        self.__cmds = []

    def append_cmd(self, cmd):
        self.__cmds.append(cmd)

    def execute(self):
        for cmd in self.__cmds:
            cmd.execute()

    def display(self):
        for cmd in self.__cmds:
            cmd.display()


def main(filename, permission):
    recv = FileOperator()
    cc = CompositeCommand()
    cc.append_cmd(FileTouchCommand(filename, recv))
    cc.append_cmd(ChmodCommand(filename, permission, recv))
    cc.execute()
    cc.display()


if __name__ == "__main__":
    filename = 'test1.txt'
    permission = '777'
    main(filename, int(permission, 8))

