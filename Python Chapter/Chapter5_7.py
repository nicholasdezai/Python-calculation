from math import sqrt


def isprime(n):
    if n <= 1:
        return False
    for i in range(2, int(sqrt(n))):
        if n % i == 0:
            return False
    return True


if __name__ == "__main__":
    n = int(input("Enter a number: "))
    if isprime(n):
        print(f"{n} is a prime number.")
    else:
        print(f"{n} is not a prime number.")
