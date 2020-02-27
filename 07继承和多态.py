from Cat import Cat
from Dog import Dog


def do():
    pets = [Dog('狗狗', '小黑'), Cat('猫猫', '小花')]
    for p in pets:
        # 继承
        p.eat('骨头')
        # 多态
        p.call()
        print("******")


if __name__ == '__main__':
    do()
