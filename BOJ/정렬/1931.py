import sys

n = int(sys.stdin.readline())
s = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

s.sort(key=lambda x: (x[1], x[0]))

time = s[0][1]
cnt = 1

for i in range(1, n):
    if time <= s[i][0]:
        cnt += 1
        time = s[i][1]

print(cnt)