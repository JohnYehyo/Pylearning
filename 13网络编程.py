from SendEmailDemo import SendEmailDemo
from TcpDemo import TcpDemo

if __name__ == '__main__':
    # TCP服务端
    # tcpDemo = TcpDemo('127.0.0.1', 8988)
    # tcpDemo.server_action()

    # Eamil
    email = SendEmailDemo()
    email.send()