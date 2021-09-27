import sys
from collections import deque

n = int(sys.stdin.readline())
tree = {i: [] for i in range(n + 1)}

for _ in range(n - 1):
    a, b, d = map(int, sys.stdin.readline().split())
    tree[a].append([b, d])
    tree[b].append([a, d])

'''
tree = [{} for _ in range(n + 1)]
for _ in range(n - 1):
    a, b, d = map(int, sys.stdin.readline().split())
    tree[a][b] = d
    tree[b][a] = d
'''


def bfs(x):
    q = deque()
    q.append([x, 0])  # 첫 노드는 가중치가 없다.
    visit = [False] * (n + 1)
    visit[x] = True
    result = [0, 0]

    while q:
        node, cnt = q.popleft()
        for i in tree[node]:
            a1, d1 = i[0], i[1]
            if not visit[a1]:
                visit[a1] = True
                q.append([a1, d1 + cnt])  # 아직 방문하지 않았다면 현재 노드, 이전 가중치에 현재 가중치 더해준 값을 append.
                if result[1] <= d1 + cnt:  # result[1]의 값과 현재 가중치까지의 합의 비교를 통해 result[1] 갱신
                    result[0] = a1
                    result[1] = d1 + cnt
    return result


print(bfs(bfs(1)[0])[1])
