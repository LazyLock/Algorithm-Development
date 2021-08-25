import sys

n, s = map(int, sys.stdin.readline().split())
list1 = list(map(int, sys.stdin.readline().split()))

pl, pr = 0, n - 1
is_break = 0

while True:
    x = sum(list1[pl:pr + 1])
    a, b = list1[pl], list1[pr]
    if x - a >= s or x - b >= s:
        if a >= b:
            pr -= 1
        else:
            pl += 1
    else:
        break

if pl > pr:
    print(0)
else:
    print(pr - pl + 1)