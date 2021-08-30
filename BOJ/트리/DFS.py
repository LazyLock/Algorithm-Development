

def dfs1(graph, node):  #  node는 시작 노드
    visited = []
    stack = [node]

    while stack:
        n = stack.pop()
        if n not in set(visited):
            visited.append(n)
            stack += set(graph[n]) - set(visited)

    return visited


def dfs2(graph, node, visited):
    visited.append(node)

    print(node, end=' ')
    print(visited)

    for i in graph[node]:
        if i not in visited:
            dfs2(graph, i, visited)