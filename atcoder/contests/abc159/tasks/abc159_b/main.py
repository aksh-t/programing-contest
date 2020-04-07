# B - String Palindrome
# https://atcoder.jp/contests/abc159/tasks/abc159_b

import sys

S = input()
N = len(S)

def is_palindrome(s):
    n = len(s)
    if n == 2:
        if s[0] == s[1]:
            return True
        else:
            return False
    else:
        if s[:n//2] == s[:n//2:-1]:
            return True
        else:
            return False

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