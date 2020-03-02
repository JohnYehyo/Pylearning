import time


def readInfo():
    """读取文件(一次性读完)"""
    f = None
    info = None
    # method 1
    # try:
    #     f = open('将进酒1.txt', mode='r', encoding='UTF-8')
    #     info = f.read()
    # except FileNotFoundError:
    #     print('不存在文件!')
    # finally:
    #     if f:
    #         f.close()
    # return info

    # method 2

    try:
        with open('将进酒.txt', 'r', encoding='UTF-8') as f:
            info = f.read()
    except FileNotFoundError:
        print('不存在文件!')
    return info


def readInfoByLine():
    """读取文件(按行读取)"""
    # try:
    #     with open('将进酒.txt', 'r', encoding='UTF-8') as f:
    #         for line in f:
    #             print(line, end='')
    #             time.sleep(0.5)
    #         print()
    # except FileNotFoundError:
    #     print('不存在文件!')

    """读取文件(读取为一行显示)"""
    try:
        with open('将进酒.txt', 'r', encoding='UTF-8') as f:
            lines = f.readlines()
            print(lines)
    except FileNotFoundError:
        print('不存在文件!')


# def write(str):


if __name__ == '__main__':
    # print(readInfo())
    readInfoByLine()
