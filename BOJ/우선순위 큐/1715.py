import sys
import heapq as hq

n = int(sys.stdin.readline())
heap = []
answer = 0

for _ in range(n):
    card = int(sys.stdin.readline())
    hq.heappush(heap, card)

for _ in range(n - 1):
    first_card = hq.heappop(heap)
    second_card = hq.heappop(heap)
    sum_card = first_card + second_card
    answer += sum_card
    hq.heappush(heap, sum_card)

print(answer)
