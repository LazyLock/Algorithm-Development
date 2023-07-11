import sys

n, k = map(int, sys.stdin.readline().split())
weight = list(map(int, sys.stdin.readline().split()))
robots = [0] * (2 * n)

result = 0

while True:
    # 1단계
    # 2차원 배열로 진행하면 복잡해질 것 같아 그냥 1차원 배열로 정의
    # 시간 복잡도는 어떻게 될지 모르겠으나 deque 사용은 싫어서 임의로 회전 (맨 앞에 요소 추가) 정의
    weight = [weight.pop(), *weight]
    robots = [robots.pop(), *robots]
    # 언제든 로봇이 내리는 위치에 도착하면 즉시 내림
    robots[n - 1] = 0

    # robots 배열에 들어있는 로봇의 위치 역순으로 확인 (먼저 들어간 로봇부터)
    for i in range(n - 1, -1, -1):
        if robots[i] == 1:      # 로봇이 존재할 경우
            if (weight[i + 1] > 0) and (robots[i + 1] == 0):
                weight[i + 1] -= 1
                robots[i] = 0
                # 언제든 로봇이 내리는 위치에 도착하면 즉시 내림
                if (i + 1) == n - 1:
                    robots[i + 1] = 0
                else:
                    robots[i + 1] = 1

    if weight[0] > 0:
        robots[0] = 1
        weight[0] -= 1

    # 과정 테스트
    # print(weight)
    # print(robots)
    # print('\n')

    result += 1

    if weight.count(0) >= k:
        break


print(result)
