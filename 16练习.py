import os
import random
import time


def reveal():
    """
    跑马灯效果
    :return:
    """
    content = '你看到我了'
    while True:
        # windows
        os.system('cls')
        # linux
        # os.system('clear')
        print(content)
        time.sleep(0.5)
        content = content[1:] + content[0]


def randomStr(length):
    """
    产生指定长度随机码
    :param length:
    :return:
    """
    # 指定一个码池
    strPool = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'a', 'b', 'c', 'd', 'e', 'f', 'g',
               'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
               'y']
    mark = ''
    poolLength = len(strPool) - 1
    for i in range(length):
        index = random.randint(0, poolLength)
        mark += strPool[index]
    return mark


if __name__ == '__main__':
    # reveal()
    print(randomStr(6))
