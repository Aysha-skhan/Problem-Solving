def add_edge(adj, u, v):
    adj[u].append(v)


V = 8
adj = [[] for _ in range(V)]

add_edge(adj, 0, 1)
add_edge(adj, 0, 2)
add_edge(adj, 0, 3)
add_edge(adj, 1, 7)
add_edge(adj, 2, 0)
add_edge(adj, 3, 0)
add_edge(adj, 4, 1)
add_edge(adj, 4, 3)
add_edge(adj, 4, 6)
add_edge(adj, 5, 2)
add_edge(adj, 5, 0)
add_edge(adj, 5, 3)
add_edge(adj, 6, 1)
add_edge(adj, 6, 4)
add_edge(adj, 7, 1)
add_edge(adj, 7, 5)


def dfs(adj, start, end):
    visited = [False] * len(adj)
    parent = [-1] * len(adj)

    def dfs_util(curr):
        if curr == end:
            return True
        visited[curr] = True
        for x in adj[curr]:
            if not visited[x]:
                parent[x] = curr
                if dfs_util(x):
                    return True
        return False

    if dfs_util(start):
        path = []
        node = end
        while node != -1:
            path.append(node)
            node = parent[node]

        print("Path:", end=" ")
        for i in range(len(path) - 1, -1, -1):
            if i == 0:
                print(path[i])
            else:
                print(path[i], "--", end=" ")
    else:

        print("No path exists from", start, "to", end)


start = int(input('Enter starting point: '))
end = int(input('Enter ending point: '))
dfs(adj, start, end)














