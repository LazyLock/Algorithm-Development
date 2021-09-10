m, n = map(int, input().split())

queue = [m]
flag = False
cnt = 0
visit = [False] * 100001

while queue:
    new_queue = []
    for i in queue:
        if i == n:
            flag = True
            break

        for j in (i - 1, i + 1, i * 2):
            if 0 <= j <= 100000 and not visit[j]:
                visit[j] = True
                new_queue.append(j)

    queue = new_queue
    cnt += 1

    if flag:
        break

print(cnt)