import sys
import heapq as hq

n = int(sys.stdin.readline())
numbers = []

for _ in range(n):
    numbers.append(int(sys.stdin.readline()))

for i in range(1, n+1):
    heap = numbers[:i]
    if len(heap) == 1:
        print(heap[0])
    else:
        hq.heapify(heap)
        for _ in range(int(round(i / 2 + 0.1)) - 1):
            hq.heappop(heap)
        print(heap[0])
