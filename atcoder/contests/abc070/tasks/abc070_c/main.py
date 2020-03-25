from collections import defaultdict

N = int(input())
Ts = list(set([int(input()) for _ in range(N)]))

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def lcm(a, b):
    g = gcd(a, b)
    return a // g * b

res = Ts[0]
for T in Ts:
    res = lcm(res, T)
print(int(res))
