from Coder import Coder as co


def main():
    coder = co('叶佳楠', '男', 'JAVA')
    coder.code('1小时')


# 为了避免被别的类引用后直接执行详情参见05函数,例子可以参考Coder中加不加if __name__ == '__main__':时这个类执行时的输出
if __name__ == '__main__':
    main()
