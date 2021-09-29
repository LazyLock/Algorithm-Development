import sys
from collections import deque

n = int(sys.stdin.readline())
tree = [[] for _ in range(n + 1)]

for _ in range(n):
    list1 = list(map(int, sys.stdin.readline().split()))
    x = len(list1)
    for i in range(1, x - 1, 2):
        tree[list1[0]].append([list1[i], list1[i + 1]])


def bfs(a):
    q = deque()
    q.append(a)
    visit = [0] * (n + 1)
    visit[a] = 1

    while q:
        node = q.popleft()
        for j in tree[node]:
            next_node, dist = j[0], j[1]
            if visit[next_node] == 0:
                q.append(next_node)
                visit[next_node] = visit[node] + dist

    return visit

visited = bfs(1)
result = bfs(visited.index(max(visited)))
print(max(result) - 1)