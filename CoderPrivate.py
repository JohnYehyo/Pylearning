"""类中属性私有在属性前加'__'"""


class CoderPrivate(object):

    # __init__方法用于在创建对象时进行初始化操作
    # self后面的name、gender、language使我们可以通过这个方法绑定的属性
    def __init__(self, name, gender, language):
        self.__name = name
        self.__gender = gender
        self.__language = language
        # self.name = name
        # self.gender = gender
        # self.language = language

    def __code1(self, time):
        print(f'{self.__name},性别{self.__gender},{self.__language}开发工程师已经编程了{time}')

    if __name__ == '__main__':
        print('我执行了!')
