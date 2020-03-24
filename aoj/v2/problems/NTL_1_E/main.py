# https://onlinejudge.u-aizu.ac.jp/problems/NTL_1_E
# 拡張ユークリッドの互除法

a, b = map(int, input().split())

def extgcd(a, b):
    d = a
    if b != 0:
        d, xprime, yprime = extgcd(b, a % b)
        x = yprime
        y = xprime - (a // b) * yprime
    else:
        x = 1
        y = 0
    return d, x, y

_, x, y = extgcd(a, b)
print(f"{x} {y}")
