import sys

m, n = map(int, sys.stdin.readline().split())

tree = []
queue = []
next_queue = []
day = 0
is_full = False

for i in range(n):
    temp = list(map(int, sys.stdin.readline().split()))
    for j, k in enumerate(temp):
        if k == 1:
            queue.append([i, j])
    tree.append(temp)

if len(queue) == m * n:
    is_full = True

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while queue:

    for y, x in queue:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and tree[ny][nx] == 0:
                next_queue.append([ny, nx])
                tree[ny][nx] = 1

    queue = next_queue
    next_queue = []
    day += 1

flag = False

for i in tree:
    for j in i:
        if j == 0:
            flag = True
            break
    if flag:
        print(-1)
        break

if not flag:
    if is_full:
        print(0)
    else:
        print(day - 1)