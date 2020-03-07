from threading import Thread


class MoneyThread(Thread):

    def __init__(self, count, money):
        super().__init__()
        self._count = count
        self._money = money

    def run(self):
        self._count.add(self._money)

