from collections import deque

def bfs1(graph, node):
    queue = deque([node])
    visited = []

    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.append(n)
            queue += graph[n]

    return visited