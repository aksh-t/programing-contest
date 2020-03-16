'2'
'3 1 4 2 5 6 7 8 9 10'
'10 9 8 7 6 5 4 3 2 1'
# YES
# NO

from collections import deque

case_num = int(input())
cases = [input().split(' ') for i in range(case_num)]
cases = [[int(x) for x in case ] for case in cases]


def dfs(a, b, c):
    if not a:
        return True

    ball = a.popleft()
    
    if not b or ball > list(b)[-1]:
        b.append(ball)
        if dfs(a, b, c):
            return True
    
    if not c or ball > list(c)[-1]:
        c.append(ball)
        if dfs(a, b, c):
            return True

    return False

def solve(case):
    a = deque(case)
    b = deque()
    c = deque()
    print('YES' if dfs(a, b, c) else 'NO')


for case in cases:
    solve(case)
