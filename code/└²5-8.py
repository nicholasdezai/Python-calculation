def isPrime(n):
    m = int(n**0.5)+1
    for i in range(2, m):
        if n%i==0:
            return False
    return True

def demo(n):
    if isinstance(n,int) and n>0 and n%2==0:
        for i in range(3, n//2+1, 2):
            if isPrime(i) and isPrime(n-i):
                print(i, '+', n-i, '=', n)

demo(38)
