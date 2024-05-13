import socket
import time

def findServer():
    # 创建socket对象
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 绑定socket
    sock.bind(('', 5050))
    while True:
        # 接收信息
        data, addr = sock.recvfrom(1024)
        # 服务器广播信息
        if data.decode() == 'ServerIP':
            # 查看服务器IP
            print(addr[0])
        # 休息一秒
        time.sleep(1)        
findServer()
