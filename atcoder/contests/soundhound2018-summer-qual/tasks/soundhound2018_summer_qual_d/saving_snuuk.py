from collections import defaultdict

money = 10 ** 15
inf = float('inf')

N, M, S, T = map(int, input().split())

edges = defaultdict(dict)
for i in range(1, M + 1):
    u, v, a, b = map(int, input().split())
    edges[u][v] = {"a": a, "b": b}
    edges[v][u] = {"a": a, "b": b}

costs_y = defaultdict(int)
costs_s = defaultdict(int)

def find_lowest_cost_node(costs, processed):
    lowest_cost = inf
    lowest_cost_node = None

    for node in costs:
        cost = costs[node]
        
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

# Sから両替所候補となる各ノードへの円を使った最短距離を計算する
temp_processed = []
for i in range(1, N + 1):
    if i is S:
        costs_y[i] = 0
        temp_processed.append(i)
    else:
        costs_y[i] = inf


node = find_lowest_cost_node(costs_y, temp_processed)
while node is not None:
    cost = costs_y[node]
    neighbors = edges[node].keys()
    for n in neighbors:
        new_cost = cost + edges[node][n]["a"]
        if costs_y[n] > new_cost:
            costs_y[n] = new_cost
    temp_processed.append(node)
    node = find_lowest_cost_node(costs_y, temp_processed)

# 両替所候補となる各ノードからTへのスヌークを使った最短距離を計算する
temp_processed = []
for i in range(1, N + 1):
    if i is T:
        costs_s[i] = 0
        temp_processed.append(i)
    else:
        costs_s[i] = inf

node = find_lowest_cost_node(costs_s, temp_processed)
while node is not None:
    cost = costs_s[node]
    neighbors = edges[node].keys()
    for n in neighbors:
        new_cost = cost + edges[node][n]["b"]
        if costs_s[n] > new_cost:
            costs_s[n] = new_cost
    temp_processed.append(node)
    node = find_lowest_cost_node(costs_s, temp_processed)


# S->i + i->T の合計コスト
total_costs = []
for i in range(1, N + 1):
    total_costs.append(costs_y[i] + costs_s[i])

for i in range(N):
    print(money - min(total_costs[i:]))
