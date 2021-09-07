import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

tree = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    tree[a] += [b]
    tree[b] += [a]

queue = [1]
cnt = 0
visit = [False] * (n + 1)

while queue:
    x = queue[0]
    del queue[0]

    if not visit[x]:
        visit[x] = True
        cnt += 1
        for i in tree[x]:
            queue.append(i)

print(cnt - 1)