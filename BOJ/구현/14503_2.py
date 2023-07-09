import sys

m, n = map(int, sys.stdin.readline().split())
x, y, d = map(int, sys.stdin.readline().split())

room = []
visited = [[0] * n for _ in range(m)]

for _ in range(m):
    room.append(list(map(int, sys.stdin.readline().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 1

while True:
    is_empty = False
    for _ in range(4):
        d = (d + 3) % 4
        n_dx = x + dx[d]
        n_dy = y + dy[d]
        if (0 <= n_dx < m) and (0 <= n_dy < n) and (room[n_dx][n_dy] == 0):
            if (visited[n_dx][n_dy] == 0):
                visited[n_dx][n_dy] = 1
                x = n_dx
                y = n_dy
                result += 1
                is_empty = True
                break
            # else:
            #     continue

    # if not is_empty:
    #     n_d = (d + 2) % 4
    #     n_dx = x + dx[n_d]
    #     n_dy = y + dy[n_d]
    #     # if (0 <= n_dx < m) and (0 <= n_dy < n):
    #     if room[n_dx][n_dy] == 1:
    #         break
    #     else:
    #         x = n_dx
    #         y = n_dy

    if not is_empty:  # 4방향 모두 청소가 되어 있을 때,
        if room[x-dx[d]][x-dy[d]] == 1:  # 후진했는데 벽
            print(result)
            break
        else:
            x, y = x-dx[d], y-dy[d]

# print(result)
