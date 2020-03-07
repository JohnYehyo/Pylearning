import time
from threading import Thread


class MoneyThread2(Thread):

    def __init__(self, money):
        super().__init__()
        self._count = 0
        self._money = money

    def run(self):
        newCount = self._count + self._money
        time.sleep(0.1)
        self._count = newCount
        print(self._count)

    @property
    def count(self):
        return self._count