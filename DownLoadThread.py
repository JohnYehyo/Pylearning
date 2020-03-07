from random import randint
from threading import Thread
from time import sleep


class DownLoadThread(Thread):

    def __init__(self, fileName):
        super().__init__()
        self._fileName = fileName

    def run(self):
        print("开始下载文件" + self._fileName)
        time1 = randint(5, 10)
        sleep(time1)
        print(f'文件{self._fileName}下载完毕,耗时{time1}秒')
