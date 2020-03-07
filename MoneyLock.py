from threading import Lock
from time import sleep


class MoneyLock(object):

    def __init__(self):
        super().__init__()
        self._count = 0
        self._lock = Lock()

    def add(self, money):
        # 获取锁
        self._lock.acquire()
        try:
            self._count += money
            sleep(0.1)
            print(f'账户到账{money}元')
        finally:
            # 释放锁
            self._lock.release()

    @property
    def count(self):
        return self._count
