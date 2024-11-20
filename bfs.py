from collections import deque


def bfs(adj, start, end):
    q = deque()
    visited = [False] * len(adj)
    path_initial = [-1] * len(adj)

    visited[start] = True
    q.append(start)
    # print(start)
    while q:
        curr = q.popleft()

        if curr == end:
            break

        for x in adj[curr]:
            if not visited[x]:
                visited[x] = True
                path_initial[x] = curr
                q.append(x)

    if visited[end]:
        path = []
        node = end
        while node != -1:
            path.append(node)
            node = path_initial[node]

        print("Path is:", end=" ")
        for i in range(len(path) - 1, 0, -1):
            print(path[i], "--", end=" ")
        print(path[0])
    else:
        print("No path exists!")


def add_edge(adj, u, v):
    adj[u].append(v)

V = 8
adj = [[] for _ in range(V)]

add_edge(adj, 0, 1)
add_edge(adj, 0, 2)
add_edge(adj, 0, 3)
add_edge(adj, 1, 7)
add_edge(adj,  2,0)
add_edge(adj, 3,0)
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

start=int(input('Enter starting point: '))
end=int(input('Enter starting point: '))
bfs(adj, start, end)
