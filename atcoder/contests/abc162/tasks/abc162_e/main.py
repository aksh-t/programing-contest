from math import gcd
from itertools import combinations_with_replacement, permutations

N, K = map(int, input().split())

answer = 0

for c in combinations_with_replacement(range(1, K + 1), N):
    n = c[0]
    for v in c[1:]:
        n = gcd(n, v)
    answer += n * len(set(permutations(c)))

print(answer)
