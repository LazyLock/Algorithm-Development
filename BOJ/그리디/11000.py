import heapq
import sys

# 시간복잡도 계산
# import math
# print(math.log(200000))

n = int(sys.stdin.readline())

subjects = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
# subjects.sort(key = lambda x : x[1])
subjects.sort()

class_room = []

for subject in subjects:
    if len(class_room) == 0:
        heapq.heappush(class_room, subject[1])
    else:
        if class_room[0] <= subject[0]:
            heapq.heappop(class_room)
        heapq.heappush(class_room, subject[1])
    # 강의실 디버깅
    # print(class_room)

print(len(class_room))

