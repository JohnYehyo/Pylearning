import json
import time
import traceback


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
        # with open('将进酒.txt', 'r', encoding='UTF-8') as f:
        with open('C://Users/T460P/Desktop/application.yml', 'r', encoding='UTF-8') as f:
            info = f.read()
    except FileNotFoundError:
        print('不存在文件!')
    return info


def readLineByLine():
    """读取文件(按行读取)"""
    try:
        with open('将进酒.txt', 'r', encoding='UTF-8') as f:
            for line in f:
                print(line, end='')
                time.sleep(0.5)
            print()
    except FileNotFoundError:
        print('不存在文件!')


def readInfoByLine():
    """读取文件(读取为一行显示)"""
    try:
        with open('将进酒.txt', 'r', encoding='UTF-8') as f:
            lines = f.readlines()
            print(lines)
    except FileNotFoundError:
        traceback.print_exc()


def writeNum():
    """将奇数与偶数分别写到a.txt和b.txt"""
    filenames = ('a.txt', 'b.txt')

    for i in range(0, 10000):
        if i % 2 == 0:
            readNum(filenames[0], str(i))
            continue
        readNum(filenames[1], str(i))
    print('执行完毕...')


def readNum(filename, i):
    """
    写入操作
    :param filename:
    :param i:
    :return:
    """
    try:
        with open(filename, 'a', encoding='UTF-8') as f:
            f.write(i + '\n')
    except Exception:
        traceback.print_exc()


def copy():
    """
    复制图片 (操作二进制文件)
    :return:
    """
    try:
        with open('watermelon.jpg', 'rb') as f1:
            data = f1.read()
            print(type(data))
        with open('new.jpg', 'wb') as f2:
            f2.write(data)
    except Exception:
        traceback.print_exc()


def writeAsJson():
    """
    将字典写成json文件
    :return:
    """
    mydict = {
        'name': '叶佳楠',
        'age': 29,
        'friends': ['银', '琦玉'],
        'cars': [
            {'brand': 'BYD', 'max_speed': 180},
            {'brand': 'Audi', 'max_speed': 280},
            {'brand': 'Benz', 'max_speed': 320}
        ]
    }
    try:
        with open('oneJson.json', 'w', encoding='UTF-8') as f:
            # 将Python对象转为json字符串
            jsonStr = json.dumps(mydict)
            print(type(jsonStr))
            print(jsonStr)
            # 将Python对象按照JSON格式序列化到文件中
            json.dump(mydict, f)
            # 将json字符串反序列化为Python对象
            dic1 = json.loads(jsonStr)
            print(type(dic1))
            print(dic1)
        with open('oneJson.json', 'r', encoding='UTF-8') as ff:
            # 将文件中的json数据反序列化为对象
            dic2 = json.load(ff)
            print(type(dic2))
            print(dic2)
    except Exception:
        traceback.print_exc()


if __name__ == '__main__':
    # print(readInfo())
    # readLineByLine()
    # readInfoByLine()
    # writeNum()
    # copy()
    writeAsJson()
