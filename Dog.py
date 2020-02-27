from Animal import Animal


class Dog(Animal):
    """狗"""

    def call(self):
        print(f'{self._nickname}在汪汪叫')
