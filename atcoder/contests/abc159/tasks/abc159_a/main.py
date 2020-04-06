# A - The Number of Even Pairs
# https://atcoder.jp/contests/abc159/tasks/abc159_a

from math import factorial

N, M = map(int, input().split())

def combinations_count(n, r):
    return factorial(n) // (factorial(n - r) * factorial(r))

combination_count_in_N = combinations_count(N, 2) if N >= 2 else 0
combination_count_in_M = combinations_count(M, 2) if M >= 2 else 0

print(combination_count_in_N + combination_count_in_M)
