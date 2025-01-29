import sys

h, w, n, m = map(int, sys.stdin.readline().split())

height = h // (n + 1)
weight = w // (m + 1)

if h % (n + 1) > 0:
    height += 1

if w % (m + 1) > 0:
    weight += 1

print(int(height * weight))
