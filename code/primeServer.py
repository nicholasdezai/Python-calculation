import socket
from threading import Thread

primes = {2, 3, 5}
def getPrimes():
    def isPrime(n):
        m = n % 6
        if m!=1 and m!=5:
            return False
        else:
            for i in range(3, int(n**0.5)+1, 2):
                if n%i == 0:
                    return False
            else:
                return True
    num = 7
    while True:
        if isPrime(num):
            primes.add(num)
        num = num+2

def recieveNumber():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('', 5005))
    sock.listen(1)
    while True:
        conn, _ = sock.accept()
        data = int(conn.recv(1024))
        if data > max(primes):
            conn.sendall(b'too big, wait a moment.')
        elif data in primes:
            conn.sendall(b'yes')
        else:
            conn.sendall(b'no')

Thread(target=getPrimes).start()
Thread(target=recieveNumber).start()
