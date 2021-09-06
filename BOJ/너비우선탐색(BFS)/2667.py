from collections import deque
import sys


def bfs(tree, a, b):
    cnt = 1
    queue = deque()
    queue.append([a, b])
    tree[a][b] = 0

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        x, y = queue[0]
        del queue[0]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            if tree[nx][ny] == 1:
                cnt += 1
                tree[nx][ny] = 0  #  이 한줄이 이중 for문의 효율성을 엄청 높여준다
                queue.append([nx, ny])

    return cnt


n = int(sys.stdin.readline())
tree = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
answer = []

for i in range(n):
    for j in range(n):
        if tree[i][j] == 1:
            answer.append(bfs(tree, i, j))

answer.sort()
print(len(answer))
for i in answer:
    print(i)