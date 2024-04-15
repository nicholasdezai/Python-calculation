# 由1，2，3，4这四个数字组成的质数，且每个数字只能用一次
def permutations(digits, length):
    if length == 1:
        return [[digit] for digit in digits]
    return [[digit] + smaller_permutation for digit in digits for smaller_permutation in
            permutations(digits, length - 1) if digit not in smaller_permutation]


# 示例用法
digits = ['1', '2', '3', '4']
out_perms = []
for length in range(1, len(digits) + 1):
    perms = permutations(digits, length)
    out_perms.append(perms)
    for perm in perms:
        print(''.join(perm))


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


print('Primes:', [int(''.join(perm)) for perms in out_perms for perm in perms if is_prime(int(''.join(perm)))])
