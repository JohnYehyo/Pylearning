from multiprocessing import Process
from random import randint
from threading import Thread
from time import sleep, time

from DownLoadThread import DownLoadThread
from DownLoadProcess import DownLoadProcess


def download(name):
    print("开始下载文件" + name)
    time1 = randint(5, 10)
    sleep(time1)
    print(f'文件{name}下载完毕,耗时{time1}秒')


if __name__ == '__main__':
    # 1 普通下载
    # download('高性能Mysql.pdf')
    # download('深入理解JAVA虚拟机.pdf')

    # 2 多进程下载
    # start = time()
    # print(start)
    # process1 = Process(target=download, args=('高性能Mysql.pdf',))
    # process1.start()
    # process2 = Process(target=download, args=('深入理解JAVA虚拟机.pdf',))
    # process2.start()
    # process1.join()
    # process2.join()
    # end = time()
    # print(f'下载完成耗时{(end - start):.2f}秒')

    # 3 多线程下载
    # start = time()
    # print(start)
    # thread1 = Thread(target=download, args=('高性能Mysql.pdf',))
    # thread1.start()
    # thread2 = Thread(target=download, args=('深入理解JAVA虚拟机.pdf',))
    # thread2.start()
    # thread1.join()
    # thread2.join()
    # end = time()
    # print(f'下载完成耗时{(end - start):.2f}秒')

    # 4 封装自定义进程类调用
    start = time()
    process3 = DownLoadProcess('高性能Mysql.pdf')
    process4 = DownLoadProcess('深入理解JAVA虚拟机.pdf')
    process3.start()
    process4.start()
    process3.join()
    process4.join()
    end = time()
    print(f'下载完成耗时{(end - start):.2f}秒')

    # 5 封装自定义线程类调用
    # start = time()
    # thread3 = DownLoadThread('高性能Mysql.pdf')
    # thread4 = DownLoadThread('深入理解JAVA虚拟机.pdf')
    # thread3.start()
    # thread4.start()
    # thread3.join()
    # thread4.join()
    # end = time()
    # print(f'下载完成耗时{(end - start):.2f}秒')
