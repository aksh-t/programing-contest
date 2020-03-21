from collections import defaultdict

N = int(input())
Ts = list(set([int(input()) for _ in range(N)]))

def get_prime_factor(n):
    res = defaultdict(int)
    for i in range(2, n):
        if i * i > n:
            break
        while n % i == 0:
            res[i] = res[i] + 1
            n = n / i
    if n != 1:
        res[n] = 1
    return res

def merge_prime_factor(a, b):
    for k, v in b.items():
        a[k] = v if a[k] < v else a[k]
    return a


lcm_prime_factor = defaultdict(int)
for T in Ts:
    lcm_prime_factor = merge_prime_factor(lcm_prime_factor, get_prime_factor(T))

res = 1
for k, v in lcm_prime_factor.items():
    res = res * (k ** v)
print(res)
