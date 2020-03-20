N = int(input())

node_edges = {i: {} for i in range(1, N + 1)}
node_colors = {i: None for i in range(1, N + 1)}

for i in range(1, N):
    u, v, w = map(int, input().split())
    node_edges[u][v] = w % 2
    node_edges[v][u] = w % 2

def paint(i):
    if node_colors[i] is None:
        node_colors[i] = 0

    for u, w in node_edges[i].items():
        if node_colors[u] is None:
            if w == 0:
                node_colors[u] = node_colors[i]
            else:
                node_colors[u] = abs(node_colors[i] - 1)

node_colors[1] = 0
for i in range(1, N + 1):
    paint(i)
    print(node_colors[i])
