import sys

n = int(sys.stdin.readline())
s = [int(sys.stdin.readline()) for _ in range(n)]

def merge_sort(s):
    if len(s) <= 1:
        return s

    mid = len(s) // 2
    left = merge_sort(s[:mid])
    right = merge_sort(s[mid:])

    i, j, k = 0, 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            s[k] = left[i]
            i += 1
        else:
            s[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        s[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        s[k] = right[j]
        j += 1
        k += 1

    return s

merge_sort(s)

for i in s:
    print(i)