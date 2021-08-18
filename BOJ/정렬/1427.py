import sys

n = int(sys.stdin.readline())
s = [int(sys.stdin.readline()) for _ in range(n)]

def quick_sort(s, left, right):
    pl, pr = left, right
    x = s[(pl + pr) // 2]

    while pl <= pr:
        while s[pl] < x: pl += 1
        while s[pr] > x: pr -= 1
        if pl <= pr:
            s[pl], s[pr] = s[pr], s[pl]
            pl += 1
            pr -= 1

    if left < pr: quick_sort(s, left, pr)
    if pl < right: quick_sort(s, pl, right)

quick_sort(s, 0 ,len(s) - 1)

for i in s:
    print(i, end='')