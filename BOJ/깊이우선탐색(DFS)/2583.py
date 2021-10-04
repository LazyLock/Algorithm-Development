import sys

sys.setrecursionlimit(10000)

a, b, c = map(int, sys.stdin.readline().split())
seq = [[0] * b for _ in range(a)]
result = []
cnt = 0

for _ in range(c):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            seq[j][i] = 1


def dfs(x, y):
    global rec
    rec += 1
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    seq[y][x] = 1
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < b and 0 <= ny < a and seq[ny][nx] == 0:
            dfs(nx, ny)


for i in range(a):
    for j in range(b):
        rec = 0
        if seq[i][j] == 0:
            dfs(j, i)
            cnt += 1
        if rec != 0:
            result.append(rec)

print(cnt)
result.sort()
print(*result)