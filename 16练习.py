import os
import time


def reveal():
    '''
        跑马灯效果
    :return:
    '''
    content = '你看到我了'
    while True:
        # windows
        os.system('cls')
        # linux
        # os.system('clear')
        print(content)
        time.sleep(0.5)
        content = content[1:] + content[0]


if __name__ == '__main__':
    reveal()