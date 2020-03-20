# https://atcoder.jp/contests/abc079/tasks/abc079_d
# D - Wall

# import pprint

H, W = map(int, input().split())
costs = []
wall = []

for i in range(10):
    cost_list = list(map(int, input().split()))
    costs.append(cost_list)
    # for j, cost in enumerate(cost_list):
    #     costs.append({"i": i, "j": j, "c": cost})

for h in range(H):
    line = list(map(int, input().split()))
    wall.append(line)

# warshall_floyd
for k in range(10):
    for i in range(10):
        for j in range(10):
            costs[i][j] = costs[i][j] if costs[i][j] < costs[i][k] + costs[k][j] else costs[i][k] + costs[k][j]

# pprint.pprint(costs)
# pprint.pprint(wall)

ans = 0 
for i, line in enumerate(wall):
    for j, cell in enumerate(line):
        if cell == -1:
            continue
        ans = ans + costs[cell][1]
print(str(ans))
