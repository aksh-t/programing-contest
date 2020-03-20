from collections import defaultdict

money = 10 ** 15
N, M, S, T = map(int, input().split())

edges = defaultdict(dict)
for i in range(1, M + 1):
    u, v, a, b = map(int, input().split())
    edges[u][v] = {"a": a, "b": b}
    edges[v][u] = {"a": a, "b": b}

inf = float('inf')
costs_from_S_by_y = defaultdict(int)
costs_to_T_by_s = defaultdict(int)

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
temp_costs = defaultdict(int)
for i in range(1, N + 1):
    if i is S:
        temp_costs[i] = 0
    else:
        temp_costs[i] = inf

node = find_lowest_cost_node(temp_costs, temp_processed)
while node is not None:
    cost = temp_costs[node]
    neighbors = edges[node].keys()
    for n in neighbors:
        new_cost = cost + edges[node][n]["a"]
        if temp_costs[n] > new_cost:
            temp_costs[n] = new_cost
    costs_from_S_by_y[node] = temp_costs[node]
    temp_processed.append(node)
    node = find_lowest_cost_node(temp_costs, temp_processed)

# 両替所候補となる各ノードからTへのスヌークを使った最短距離を計算する
temp_processed = []
temp_costs = defaultdict(int)
for i in range(1, N + 1):
    if i is T:
        temp_costs[i] = 0
    else:
        temp_costs[i] = inf

node = find_lowest_cost_node(temp_costs, temp_processed)
while node is not None:
    cost = temp_costs[node]
    neighbors = edges[node].keys()
    for n in neighbors:
        new_cost = cost + edges[node][n]["b"]
        if temp_costs[n] > new_cost:
            temp_costs[n] = new_cost
    costs_to_T_by_s[node] = temp_costs[node]
    temp_processed.append(node)
    node = find_lowest_cost_node(temp_costs, temp_processed)


# S->i + i->T の合計コスト
total_costs = []
for i in range(1, N + 1):
    total_costs.append(costs_from_S_by_y[i] + costs_to_T_by_s[i])

for i in range(N):
    print(money - min(total_costs[i:]))
