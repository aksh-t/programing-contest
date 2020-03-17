# https://onlinejudge.u-aizu.ac.jp/problems/GRL_1_B
# 単一始点最短経路（負の重みをもつ辺を含む）

# 初期化、入力の処理
INF = float('inf')
edges = []
V, E, r = map(int, input().split())

for i in range(E):
    s, t, d = map(int, input().split())
    edges.append({"s": s, "t": t, "d": d})

# ベルマンフォード法
ds = [INF for i in range(V)]
ds[r] = 0
i = 0
while True:
    i = i + 1
    update = False
    for j in range(E):
        edge = edges[j]
        if ds[edge["s"]] != INF and ds[edge["t"]] > ds[edge["s"]] + edge["d"]:
            if i == V - 1:
                print("NEGATIVE CYCLE")
                exit()

            ds[edge["t"]] = ds[edge["s"]] + edge["d"]
            update = True
    if not update:
        break

for i in range(V):
    print(ds[i] if ds[i] != INF else "INF")
