import sys

n = int(sys.stdin.readline())
s = []
for i in range(n):
    a, b = sys.stdin.readline().split()
    s.append([int(a), str(b)])

s.sort(key=lambda x: x[0])

for i in s:
    print(*i)