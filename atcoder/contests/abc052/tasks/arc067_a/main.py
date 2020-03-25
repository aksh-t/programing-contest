# https://atcoder.jp/contests/abc052/tasks/arc067_a
# C - Factors of Factorial

N = int(input())

n = 1
for i in range(2, N + 1):
    n = n * i


def get_prime_factor(n):
    from collections import defaultdict
    res = defaultdict(int)
    for i in range(2, n + 1):
        if i * i > n:
            break
        while n % i == 0:
            res[i] = res[i] + 1
            n = n // i
    if n != 1:
        res[n] = 1
    return res

prime_factor = get_prime_factor(n)

# WIP
# TODO: 素因数から約数(の個数)をどうやって取り出すか
