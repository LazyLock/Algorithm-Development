import sys

n = int(sys.stdin.readline())

tree = [[] for _ in range(n + 1)]
visit = [0] * (n + 1)
visit[1] = 1

for _ in range(n - 1):
    a, b = map(int, sys.stdin.readline().split())
    tree[a] += [b]
    tree[b] += [a]


def dfs(node):
    stack = [node]

    while stack:
        parent = stack.pop()
        for child in tree[parent]:
            if not visit[child]:
                visit[child] = parent
                stack.append(child)
    print('\n'.join(map(str,visit[2:])))


dfs(1)