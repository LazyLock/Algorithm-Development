import sys

wheels = {}
directions = [True, True, True]
is_wheel_turn = [False, False, False, False]

for i in range(1, 5):
    reader = [s for s in map(str, sys.stdin.readline())]
    reader = reader[:8]
    wheels[i] = reader

n = map(int, sys.stdin.readline())

for _ in range(n):

    # 맞물린 톱니바퀴 방향
    for i in range(3):
        if wheels[i + 1][2] == wheels[i + 2][6]:
            directions[0] = True
        else:
            directions[0] = False

    m, k = map(int, sys.stdin.readline().split())
    target_wheel = wheels[m]
    is_wheel_turn[m - 1] = True

    if k == 1:
        target_wheel = [target_wheel.pop(), *target_wheel]

    else:
        first_direction = target_wheel.pop(0)
        target_wheel = [*target_wheel, first_direction]


    for i in range(1,3):
        direction_m = m - i
        if (direction_m >= 0) and (direction_m <= 2):
            
