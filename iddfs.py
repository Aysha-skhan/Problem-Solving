def dls(adj, node, end, depth):
    if node == end:
        return True
    if depth == 0:
        return False
    for n in adj[node]:
        if dls(adj, n, end, depth - 1):
            return True
    return False

def iddfs(adj, start, end, max_depth):
    for depth in range(max_depth + 1):
        if dls(adj, start, end, depth):
            print(f"Level: {depth}")
            return True
    return False

def add_edge(adj, u, v):
    adj[u].append(v)

V = 8
adj = [[] for _ in range(V)]

add_edge(adj, 0, 1)
add_edge(adj, 0, 2)
add_edge(adj, 0, 3)
add_edge(adj, 1, 7)
add_edge(adj, 4, 6)
add_edge(adj, 5, 2)
add_edge(adj, 5, 3)


s = int(input('Enter starting point: '))
d = int(input('Enter ending point: '))
max_depth = int(input('Enter maximum depth: '))

if iddfs(adj, s, d, max_depth):
    print(f"Path exists between {s} and {d}")
else:
    print(f"No path exists between {s} and {d}")


