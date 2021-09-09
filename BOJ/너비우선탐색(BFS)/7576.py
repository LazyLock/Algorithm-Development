from collections import deque
import sys

m, n = map(int, sys.stdin.readline().split())

tree = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
queue = deque()
day = -2

for i in range(m):
    for j in range(n):
        if tree[j][i] == 1:
            queue.append([j, i])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while queue:
    y, x = queue.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m and 0 <= ny < n and tree[ny][nx] == 0:
            queue.append([ny, nx])
            tree[ny][nx] = tree[y][x] + 1

flag = False

for i in tree:
    for j in i:
        if j == 0:
            flag = True
            break
        day = max(day, j)
    if flag:
        print(-1)
        break

if not flag:
    if day == -1:
        print(0)
    else:
        print(day - 1)