import sys
import heapq

n = int(sys.stdin.readline())
max_heapq = []

for _ in range(n):
    x = int(sys.stdin.readline())

    if x > 0:
        heapq.heappush(max_heapq, (-x, x))
    else:
        if len(max_heapq) == 0:
            print(0)
        else:
            output = heapq.heappop(max_heapq)[1]
            print(output)
