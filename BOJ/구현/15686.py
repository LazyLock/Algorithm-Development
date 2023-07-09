import sys
from itertools import combinations

n, m = map(int, sys.stdin.readline().split())
# sys 모듈 기억 잘 안나서 테스트
# seq = list(map(int, sys.stdin.readline().split()))

chicken_arr = []
house_arr = []

for i in range(n):
    seq = list(map(int, sys.stdin.readline().split()))
    for j in range(len(seq)):
        if seq[j] == 1:
            house_arr.append([i, j])
        elif seq[j] == 2:
            chicken_arr.append([i, j])
        else:
            continue

iter_seq = list(combinations(range(len(chicken_arr)), m))
result = 1000000000
# result 값은 일부러 극단적인 큰 값 제시


def calcu_dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


answer_arr = []

for s in iter_seq:
    new_chicken_arr = [chicken_arr[i] for i in s]
    result_arr = []
    for house in house_arr:
        min_arr = []
        for chiken in new_chicken_arr:
            min_arr.append(calcu_dist(house, chiken))
        result_arr.append(min(min_arr))
    answer_arr.append(sum(result_arr))

print(min(answer_arr))
