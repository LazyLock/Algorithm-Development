import sys
from collections import deque

n = int(sys.stdin.readline())
queue_plus = []
queue_minus = []
is_zero = False
result = 0

for _ in range(n):
    k = int(sys.stdin.readline())
    if k > 1:
        queue_plus.append(k)
    elif k == 1:
        result += 1
    elif k == 0:
        is_zero = True
    else:
        queue_minus.append(k)

queue_minus.sort()
queue_minus = deque(queue_minus)

queue_plus.sort()
queue_plus = deque(queue_plus)


if len(queue_minus) % 2 == 1:
    if is_zero:
        queue_minus.pop()
    else:
        result += queue_minus.pop()


for i in range(0, len(queue_minus), 2):
    result += (queue_minus[i] * queue_minus[i + 1])

if len(queue_plus) % 2 == 1:
    result += queue_plus.popleft()

for i in range(0, len(queue_plus), 2):
    result += (queue_plus[i] * queue_plus[i + 1])

print(result)