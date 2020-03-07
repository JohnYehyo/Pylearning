from time import sleep


class Money(object):

    def __init__(self):
        super().__init__()
        self._count = 0

    def add(self, money):
        newCount = self._count + money
        sleep(0.1)
        self._count = newCount


    @property
    def count(self):
        return self._count