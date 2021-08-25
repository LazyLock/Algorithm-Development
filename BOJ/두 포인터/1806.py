import sys

N, S = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

pl, pr, x = 0, 0, arr[0]
answer = 100001

while True:
    if x >= S:
        answer = min(answer, pr - pl + 1)
        x -= arr[pl]
        pl += 1
    else:
        if pr == N - 1:
            break
        else:
            pr += 1
            x += arr[pr]

if answer == 100001:
    answer = 0

print(answer)
