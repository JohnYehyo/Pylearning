from Animal import Animal


class Cat(Animal):
    """猫"""

    def call(self):
        print(f'{self._nickname}在喵喵叫')
