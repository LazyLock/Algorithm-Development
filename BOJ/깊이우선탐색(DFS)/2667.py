import sys

n = int(input())
tree = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
count = 0
answer = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(tree, a, b):
    if a < 0 or a >= n or b < 0 or b >= n:
        return False

    global count

    if tree[a][b] == 1:
        tree[a][b] = 0
        count += 1
        for i in range(4):
            na = a + dx[i]
            nb = b + dy[i]
            dfs(tree, na, nb)
        return True
    return False


for i in range(n):
    for j in range(n):
        if dfs(tree, i, j):
            answer.append(count)
            count = 0

answer.sort()
print(len(answer))
for i in answer:
    print(i)