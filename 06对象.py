from time import sleep, localtime, time

from Clock import Clock
from Coder import Coder as co
from CoderPrivate import CoderPrivate
from Archmage import Archmage
from CoderProperty import CoderProperty
from CoderSlots import CoderSlots


# 1. 创建对象使用对象
def first():
    coder = co('叶佳楠', '男', 'JAVA')
    print(coder.name)
    coder.code('1小时')


# 2. 私有属性无法访问
def second():
    coder = CoderPrivate('叶佳楠', '男', 'JAVA')
    # (1)私有属性无法访问
    # print(coder.name)
    # coder.code('1小时')

    # (2)Python并没有从语法上严格保证私有属性或方法的私密性
    # 它只是给私有的属性和方法换了一个名字来妨碍对它们的访问
    # 我们更换名字的规则后依然可以访问到
    print(coder._CoderPrivate__name)
    coder._CoderPrivate__code('1小时')


"""
在实际开发中，我们并不建议将属性设置为私有的，因为这会导致子类
无法访问。所以大多数Python程序员会遵循一种命名惯例就是让属性名
以单下划线开头来表示属性是受保护的，本类之外的代码在访问这样的
属性时应该要保持慎重。这种做法并不是语法上的规则，单下划线开头
的属性和方法外界仍然是可以访问的，所以更多的时候它是一种暗示或
隐喻
"""

# 3. @property装饰器
"""
类似JAVA的set、get方法
Python一般建议给属性加单下划线说明属性是受保护的不建议直接访问,所以可以通过
setter修改器和getter访问器的方法来对属性进行操作
"""


def third():
    coderProperty = CoderProperty('叶佳楠', '男', 'JAVA')
    coderProperty.code('1小时')
    coderProperty.name = '楠佳叶'
    # coderProperty._name = '佳楠叶'  # 推荐用第一种装饰器方法,不推荐第二种直接访问属性
    coderProperty.gender = '女'
    # coderProperty.language = 'Python'  # 会报AttributeError: can't set attribute
    coderProperty.code('1小时')
    print(coderProperty.name)
    # print(coderProperty._name)  # 推荐用第一种装饰器方法,不推荐第二种直接访问属性
    print(coderProperty.gender)
    print(coderProperty.language)

    # 因为Python是一门动态语言,所以可以在程序运行时对属性解绑或者绑定新属性和方法
    coderProperty._other = '无'
    print(coderProperty._other)


# 4. __slots__限定属性
# 限定自定义类型的对象只能绑定某些属性
def fourth():
    coderSlots = CoderSlots('叶佳楠', '男', 'JAVA')
    coderSlots.code('1小时')
    coderSlots.name = '楠佳叶'
    coderSlots.gender = '女'
    coderSlots.language = 'Python'
    coderSlots.code('1小时')
    print(coderSlots.name)
    print(coderSlots.gender)
    print(coderSlots.language)

    # 由于类中加上了显示属性所以无法新增属性 AttributeError: 'CoderSlots' object has no attribute '_other'
    coderSlots._other = '无'
    print(coderSlots._other)


# 5. 静态方法和类方法
"""
一点理解:
    什么时候创建静态方法和类方法而不创建对象方法?
    比如黑暗大法师类我们传入头、左手、右手、左脚、右脚召唤出黑暗大法师
    这个召唤方法就是对象方法 但是怎么判断传入的五个参数是上述的呢 我们
    可以创建一个检测是否是上述要求的方法 这个方法早于黑暗大法师对象创建
    因此就是这个类的方法 这个方法可以使用静态方法
"""


def fifth():
    a, b, c, d, e = '头', '左手', '右手', '左脚', '右脚'
    if Archmage.check(a, b, c, d, e):
        archmage = Archmage(a, b, c, d, e)
        print(archmage.create())
        print(archmage.shout())
    else:
        print('条件不足,无法召唤')


"""
类方法和静态方法类似代表的是当前类相关的信息的对象（类本身也是一个对象，有的地方也称之为类的元数据对象）
通过这个参数我们可以获取和类相关的信息并且可以创建出类的对象, 类方法的第一个参数一般约定命名cls
"""


def sixth():
    # 通过类方法创建对象并获取系统时间
    # 体会一下三种获取对象的区别 第一种和第三种输出结果一致为什么
    # (1)
    clock = Clock.now()
    # (2)
    # clock = Clock()
    # (3)
    # ctime = localtime(time())
    # clock = Clock(ctime.tm_hour, ctime.tm_min, ctime.tm_sec)
    while True:
        print(clock.show())
        sleep(1)
        clock.run()


# 为了避免被别的类引用后直接执行详情参见05函数,例子可以参考Coder中加不加if __name__ == '__main__':时这个类执行时的输出
if __name__ == '__main__':
    # first()
    # second()
    # third()
    # fourth()
    # fifth()
    sixth()
