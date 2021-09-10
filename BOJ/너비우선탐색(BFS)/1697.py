from collections import deque

n, m = map(int, input().split())
visit = [0] * 100001


def bfs(x):
    queue = deque()
    queue.append(n)

    while queue:
        a = queue.popleft()

        if a == m:
            print(visit[a])
            break

        for j in (a - 1, a + 1, a * 2):
            if 0 <= j <= 100000 and visit[j] == 0:
                visit[j] = visit[a] + 1
                queue.append(j)


bfs(n)
