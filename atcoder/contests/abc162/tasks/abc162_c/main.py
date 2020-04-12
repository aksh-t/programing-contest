from math import gcd
from collections import defaultdict

N = int(input())

answer = 0

for a in range(1, N + 1):
    for b in range(1, N + 1):
        for c in range(1, N + 1):
            n = gcd(gcd(a, b), c)
            answer += n

print(answer)

