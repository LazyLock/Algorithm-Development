from collections import deque
import sys

m, n , v = map(int, sys.stdin.readline().split())
tree = [[] for i in range(m + 1)]
visit = [False] * (m + 1)

for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    tree[a] += [b]
    tree[b] += [a]

for i in tree:
    i.sort()


def BFS(node):
    queue = deque([node])
    visit = [False] * (m + 1)
    visit[node] = True

    while queue:
        s = queue.popleft()
        print(s, end=' ')
        for i in tree[s]:
            if not visit[i]:
                queue.append(i)
                visit[i] = True

def DFS(node):
    visit[node] = True
    print(node, end=' ')
    for i in tree[node]:
        if not visit[i]:
            DFS(i)

def DFS2(node):
    stack = [node]
    list = []
    visit = [False] * (m + 1)
    while stack:
        s = stack.pop()
        if not visit[s]:
            visit[s] = True
            list.append(s)
            tree[s].sort(reverse=True)
            stack += tree[s]
    return list

BFS(v)
print()
print(' '.join(map(str, DFS2(v))))