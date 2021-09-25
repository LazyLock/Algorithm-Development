import sys
from collections import deque

sys.setrecursionlimit(100000)

dx = [-1, 1, 0, 0, -1, 1, -1, 1]
dy = [0, 0, -1, 1, 1, -1, -1, 1]


def dfs(x, y):
    for n in range(8):
        nx = dx[n] + x
        ny = dy[n] + y

        if 0 <= nx < b and 0 <= ny < a and tree[nx][ny] == 1:
            tree[nx][ny] = 0
            dfs(nx, ny)


def bfs(x, y):
    queue = deque()
    queue.append([x, y])

    while queue:
        x1, y1 = queue.popleft()
        for n in range(8):
            nx = dx[n] + x1
            ny = dy[n] + y1

            if 0 <= nx < b and 0 <= ny < a and tree[nx][ny] == 1:
                tree[nx][ny] = 0
                queue.append([nx, ny])


while True:
    cnt = 0
    a, b = map(int, sys.stdin.readline().split())
    if a == 0 and b == 0:
        break

    tree = [list(map(int, sys.stdin.readline().split())) for _ in range(b)]

    for i in range(b):
        for j in range(a):
            if tree[i][j] == 1:
                tree[i][j] = 0
                bfs(i, j)
                cnt += 1

    print(cnt)