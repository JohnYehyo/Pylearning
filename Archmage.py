class Archmage(object):
    __slots__ = ('_a', '_b', '_c', '_d', '_e')

    def __init__(self, a, b, c, d, e):
        self._a = a
        self._b = b
        self._c = c
        self._d = d
        self._e = e

    @staticmethod
    def check(a, b, c, d, e):
        return a == '头' and b == '左手' and c == '右手' and d == '左脚' and e == '右脚'

    def create(self):
        return self._a + self._b + self._c + self._d + self._e

    def shout(self):
        return '出来吧黑暗大法师!'


