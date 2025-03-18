# from queue import PriorityQueue

# n = int(input())
# pq = PriorityQueue()

# for _ in range(n):
#     x = int(input())

#     if x != 0:
#         pq.put((abs(x), x))
#     else:
#         if pq.empty():
#             print(0)
#         else:
#             output = pq.get()[1]
#             print(output)

import heapq
import sys

n = int(sys.stdin.readline())

heapq_seq = []

for _ in range(n):
    x = int(sys.stdin.readline())

    if x != 0:
        heapq.heappush(heapq_seq, (abs(x), x))
    else:
        if len(heapq_seq) == 0:
            print(0)
        else:
            output = heapq.heappop(heapq_seq)[1]
            print(output)
