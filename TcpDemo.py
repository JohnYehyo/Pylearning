
from datetime import datetime
from socket import socket, AF_INET, SOCK_STREAM


class TcpDemo(object):

    def __init__(self):
        pass


    """
    

    """
    def action(self):
        # 1.创建套接字对象并指定使用哪种传输服务
        # class socket:
        #     family: int
        #     type: int
        #     proto: int
        #
        #     family:
        #       AF_INET - IPv4
        #       AF_INET6 - IPv6地址
        #
        #     type:
        #       SOCK_STREAM - TCP套接字
        #       SOCK_DGRAM - UDP套接字
        #       SOCK_RAW - 原始套接字
        server = socket(family=AF_INET, type=SOCK_STREAM)
        # 2 绑定ID和端口
        server.bind(('127.0.0.1', 8988))
        # 3 开启监听
        server.listen(512)
        print('服务器启动...')
        print('开始监听...')
        while True:
            # 4 循环接收客户端连接并处理
            # accept方法是一个阻塞方法如果没有客户端连接到服务器代码不会向下执行
            # accept方法返回一个元组其中的第一个元素是客户端对象
            client, address = server.accept()
            print(type(client))
            print(f'{address}连接服务器')
            # 5 发送数据
            client.send(str(datetime.now()).encode('utf-8'))
            # 6 断开连接
            client.close

