from TcpDemo import TcpDemo

if __name__ == '__main__':
    # TCP 客户端
    tcpDemo = TcpDemo('127.0.0.1', 8988)
    tcpDemo.client_action()
