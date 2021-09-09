import sys

sys.setrecursionlimit(2500)

t = int(sys.stdin.readline())


def dfs(a, b):
    if a < 0 or a >= n or b < 0 or b >= m:
        return False

    if tree[a][b] == 1:
        tree[a][b] = 0
        for xy in range(4):
            nx = b + dx[xy]
            ny = a + dy[xy]
            dfs(ny, nx)
        return True
    return False


for i in range(t):
    answer = 0
    m, n, k = map(int, sys.stdin.readline().split())
    tree = [[0] * m for _ in range(n)]

    for j in range(k):
        a, b = map(int, sys.stdin.readline().split())
        tree[b][a] = 1

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for my in range(n):
        for mx in range(m):
            if dfs(my, mx):
                answer += 1

    print(answer)