class CoderProperty(object):

    # __init__方法用于在创建对象时进行初始化操作
    # self后面的name、gender、language使我们可以通过这个方法绑定的属性
    def __init__(self, name, gender, language):
        self._name = name
        self._gender = gender
        self._language = language

    # 访问器 getter方法
    @property
    def name(self):
        return self._name

    @property
    def gender(self):
        return self._gender

    @property
    def language(self):
        return self._language

    # 修改器 setter方法
    @name.setter
    def name(self, name):
        self._name = name

    @gender.setter
    def gender(self, gender):
        self._gender = gender

    # @language.setter
    # def language(self, language):
    #     self._language = language

    def code(self, time):
        print(f'{self.name},性别{self.gender},{self.language}开发工程师已经编程了{time}')

    if __name__ == '__main__':
        print('我执行了!')
