import sys

n, m = map(int, sys.stdin.readline().split())

tree = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = [[0, 0]]

while queue:
    x, y = queue[0][0], queue[0][1]
    del queue[0]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue

        if tree[nx][ny] == 0:
            continue

        if tree[nx][ny] == 1:
            queue.append([nx, ny])
            tree[nx][ny] = tree[x][y] + 1

print(tree[n - 1][m - 1])