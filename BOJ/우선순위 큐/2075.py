# import sys
# import heapq

# n = int(sys.stdin.readline())
# seq_heapq = []

# for _ in range(n):
#     n_seq = sys.stdin.readline().split()
#     for nn in n_seq:
#         heapq.heappush(seq_heapq, (-int(nn), int(nn)))

# for _ in range(n - 1):
#     heapq.heappop(seq_heapq)

# print(heapq.heappop(seq_heapq)[1])

# 메모리 초과 문제 -> 공간 복잡도 확인

import sys
import heapq
import io


def sol():
    n = int(sys.stdin.readline())

    min_heapq = list(map(int, sys.stdin.readline().split()))
    heapq.heapify(min_heapq)

    for _ in range(n - 1):
        numbers_seq = list(map(int, sys.stdin.readline().split()))
        for n in numbers_seq:
            if min_heapq[0] < n:
                heapq.heappop(min_heapq)
                heapq.heappush(min_heapq, n)

    print(min_heapq[0])


if __name__ == "__main__":
    # test_input = """5
    # 12 7 9 15 5
    # 13 8 11 19 6
    # 21 10 26 31 16
    # 48 14 28 35 25
    # 52 20 32 41 49
    # """

    # sys.stdin = io.StringIO(test_input)
    sol()
