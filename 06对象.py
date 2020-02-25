from Coder import Coder as co
from CoderPrivate import CoderPrivate


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

# 为了避免被别的类引用后直接执行详情参见05函数,例子可以参考Coder中加不加if __name__ == '__main__':时这个类执行时的输出
if __name__ == '__main__':
    first()
    second()
