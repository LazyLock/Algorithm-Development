import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

tree = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    tree[a] += [b]
    tree[b] += [a]

visit = [False] * (n + 1)
cnt = 0

def dfs(x):
    global cnt
    if not visit[x]:
        visit[x] = True
        cnt += 1
        for i in tree[x]:
            dfs(i)
    return cnt

print(dfs(1) - 1)
