import socket
import time
import sys
import os

try:
    with open(os.getenv('temp')+'\\abc.txt', 'x') as fp:
        fp.write('Server')
except:
    print('Server already exists.')
    sys.exit(0)

def sendServerIP():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        # 获取本机IP
        IP = socket.gethostbyname(socket.gethostname())
        # 255表示广播地址
        IP = IP[:IP.rindex('.')]+'.255'
        # 发送信息
        sock.sendto('ServerIP'.encode(), (IP, 5050))
        time.sleep(1)

print('Server started.....')
sendServerIP()
