import sys

n = int(sys.stdin.readline())
s = [int(sys.stdin.readline().rstrip()) for _ in range(n)]

s.sort(key=lambda x: (len(x), x))

for i in s:
    print(i)