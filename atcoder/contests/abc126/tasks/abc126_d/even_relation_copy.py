import sys
sys.setrecursionlimit(4100000)

N = int(input())
root = [[] for i in range(N)]
for i in range(N-1):
    u, v, w = map(int,input().split())
    root[u-1].append([v-1,w%2])
    root[v-1].append([u-1,w%2])

ans = [-1 for i in range(N)]

def dfs(index):
    if ans[index]==-1:
        ans[index] = 0
    for i in root[index]:
        if ans[i[0]] == -1:
            ans[i[0]] = (ans[index]+i[1])%2
            dfs(i[0])

for i in range(N):
    dfs(i)

for i in ans:
    print(i)
