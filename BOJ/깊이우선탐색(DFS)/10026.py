import sys

sys.setrecursionlimit(5000)

n = int(sys.stdin.readline())
tree = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
result = [0, 0]
visit1 = [[0] * n for _ in range(n)]
visit2 = [[0] * n for _ in range(n)]


def dfs_normal(a, b, x, visit):
    visit[b][a] = 1
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    for i in range(4):
        nx = a + dx[i]
        ny = b + dy[i]

        if 0 <= nx < n and 0 <= ny < n and tree[ny][nx] in x and visit[ny][nx] == 0:
            dfs_normal(nx, ny, x, visit)


for i in range(n):
    for j in range(n):
        color = [tree[i][j]]
        if visit1[i][j] == 0:
            dfs_normal(j, i, color, visit1)
            result[0] += 1
        if visit2[i][j] == 0:
            if color == ['R'] or color == ['G']:
                color_list = ['R', 'G']
            else:
                color_list = ['B']
            dfs_normal(j, i, color_list, visit2)
            result[1] += 1

print(result[0], result[1])
