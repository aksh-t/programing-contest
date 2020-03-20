import sys
sys.setrecursionlimit(1000000000)

xls = []
removes = []
n = int(input())
for i in range(n):
    x, l = input().split()
    xls.append((int(x), int(l)))
    removes.append(False)
xls.sort()

def resolve(i):
    xi, li = xls[i]
    ri = removes[i]

    for j in range(i+1, len(xls)):
        xj, lj = xls[j]
        rj = removes[j]
        if not rj and xi + li > xj - lj:
            removes[j] = True

def main():
    res = 0
    for i in range(len(xls)):
        if not removes[i]:
            resolve(i)
    print(removes.count(False))

main()