import sys

t = int(sys.stdin.readline())


def bfs(a, b):
    queue = [[a, b]]
    cnt = 1

    while queue:
        x, y = queue[0]
        del queue[0]

        for xy in range(4):
            nx = x + dx[xy]
            ny = y + dy[xy]

            if nx >= m or nx < 0 or ny < 0 or ny >= n:
                continue

            if tree[nx][ny] == 1:
                cnt += 1
                tree[nx][ny] = 0
                queue.append([nx, ny])
    return cnt


for i in range(t):
    answer = []
    m, n, k = map(int, sys.stdin.readline().split())
    tree = [[0] * n for _ in range(m)]

    for j in range(k):
        a, b = map(int, sys.stdin.readline().split())
        tree[a][b] = 1

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for mx in range(m):
        for my in range(n):
            if tree[mx][my] == 1:
                tree[mx][my] = 0
                answer.append(bfs(mx, my))

    print(len(answer))