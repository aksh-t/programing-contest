# B - String Palindrome
# https://atcoder.jp/contests/abc159/tasks/abc159_b

import sys

S = input()
N = len(S)

def is_palindrome(s):
    return s == s[::-1]

if not is_palindrome(S):
    print("No")
    sys.exit()

if not is_palindrome(S[:(N-1)//2]):
    print("No")
    sys.exit()

if not is_palindrome(S[(N+3)//2-1:]):
    print("No")
    sys.exit()

print("Yes")