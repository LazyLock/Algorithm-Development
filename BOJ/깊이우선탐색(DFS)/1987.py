import sys

s, c = map(int, sys.stdin.readline().split())
seq = [list(map(lambda x: ord(x) - 65, sys.stdin.readline().rstrip())) for _ in range(s)]
visit = [0] * 26
answer = 0


def dfs(x, y, cnt):
    global answer
    answer = max(answer, cnt)

    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < c and 0 <= ny < s and visit[seq[ny][nx]] == 0:
            visit[seq[ny][nx]] = 1
            dfs(nx, ny, cnt + 1)
            visit[seq[ny][nx]] = 0
    return answer


visit[seq[0][0]] = 1
dfs(0, 0, 1)
print(answer)