from threading import Lock
from time import sleep


class MoneyLock(object):

    def __init__(self):
        super().__init__()
        self._count = 0
        self._lock = Lock()

    def add(self, money):
        self._lock.acquire()
        try:
            newCount = self._count + money
            sleep(0.1)
            self._count = newCount
        finally:
            self._lock.release()

    @property
    def count(self):
        return self._count
