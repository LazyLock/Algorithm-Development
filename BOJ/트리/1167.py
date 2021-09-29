import sys
from collections import deque

n = int(sys.stdin.readline())
tree = {j: [] for j in range(n + 1)}

for _ in range(n):
    list1 = list(map(int, sys.stdin.readline().split()))
    len_list1 = len(list1)
    x = list1[0]
    for i in range(1, len_list1 - 1, 2):
        tree[x].append([list1[i], list1[i + 1]])


def bfs(a):
    q = deque()
    q.append([a, 0])
    visit = [False] * (n + 1)
    visit[a] = True
    result = [0, 0]

    while q:
        now_node, cnt = q.popleft()  # cnt는 직전까지의 가중치의 합
        for j in tree[now_node]:
            next_node, next_dist = j[0], j[1]
            if not visit[next_node]:
                visit[next_node] = True
                q.append([next_node, cnt + next_dist])
                if result[1] <= cnt + next_dist:
                    result[0] = next_node
                    result[1] = cnt + next_dist

    return result


print(bfs(bfs(1)[0])[1])