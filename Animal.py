from abc import ABCMeta, abstractmethod


class Animal(object, metaclass=ABCMeta):
    """动物"""

    def __init__(self, name, nickname):
        self._name = name
        self._nickname = nickname

    @property
    def name(self):
        return self._name

    @property
    def nickname(self):
        return self._nickname

    @name.setter
    def name(self, name):
        self._name = name

    @nickname.setter
    def nickname(self, nickname):
        self._nickname = nickname

    def eat(self, food):
        """吃饭"""
        print(f'{self._name}吃{food}')

    @abstractmethod
    def call(self):
        """叫"""
        pass
