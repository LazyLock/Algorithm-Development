import sys

n, m = map(int, sys.stdin.readline().split())
basket = []

for _ in range(n):
    seq = list(map(int, sys.stdin.readline().split()))
    basket.append(seq)

# 구름 이동용 8가지 방향 배열
dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

# 물 복사 버그용 대각선 방향 배열
copy_dx = [-1, -1, 1, 1]
copy_dy = [-1, 1, 1, -1]

# 초기 구름 위치 인덱스
cloud_idx = [[n - 1, 0], [n - 1, 1], [n - 2, 0], [n - 2, 1]]

for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    i -= 1
    # n 행, 열과 0 행, 열이 연결되어 있는 상황이므로
    n_dx = dx[i] * j + n * 50
    n_dy = dy[i] * j + n * 50

    moved_cloud_idx = []

    for x, y in cloud_idx:
        x = (x + n_dx) % n
        y = (y + n_dy) % n

        moved_cloud_idx.append([x, y])
        basket[x][y] += 1

        # 물 복사 버그
    for x, y in moved_cloud_idx:
        cnt = 0
        for i in range(4):
            copy_x = x + copy_dx[i]
            copy_y = y + copy_dy[i]

            if (0 <= copy_x < n) and (0 <= copy_y < n):
                if basket[copy_x][copy_y] > 0:
                    cnt += 1
                else:
                    continue

        basket[x][y] += cnt

    new_cloud_idx = []

    for i in range(n):
        for j in range(n):
            if ([i, j] not in moved_cloud_idx) and basket[i][j] >= 2:
                basket[i][j] -= 2
                new_cloud_idx.append([i, j])
            else:
                continue

    cloud_idx = new_cloud_idx

    # debuging

    # for seq in basket:
    #     print(seq)
    # print(cloud_idx)
    # print(moved_cloud_idx)
    # print('\n')

result = 0
for seq in basket:
    result += sum(seq)

print(result)


#######################################################################
# 다른 사람 풀이인데 내 풀이랑 로직 같은데... 왜 내건 틀리고 이건 맞을까...
# 참고용으로 일단 주석 처리 해놓음
# 출처 : https://kimjingo.tistory.com/170

# # 입력
# N, M = map(int, input().split())
# board = [list(map(int, input().split())) for _ in range(N)]
# moves = [tuple(map(int, input().split())) for _ in range(M)]

# # 8방향
# dy8 = ("empty", 0, -1, -1, -1, 0, 1, 1, 1)
# dx8 = ("empty", -1, -1, 0, 1, 1, 1, 0, -1)

# # 대각 4방향
# dy4 = (-1, -1,  1, 1)
# dx4 = (-1,  1, -1, 1)

# clouds = [(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)]  # 구름 좌표
# for d, s in moves:
#     # 모든 구름 이동
#     moved_clouds = []
#     for y, x in clouds:
#         # 구름들을 d 방향으로 s만큼 이동(구름의 좌표는 연결되어있으므로 %N)
#         ny = (y + dy8[d] * s) % N
#         nx = (x + dx8[d] * s) % N
#         board[ny][nx] += 1  # 물의 양 추가
#         moved_clouds.append((ny, nx))  # 이동한 구름 좌표에 추가

#     for y, x in moved_clouds:
#         # 이동한 구름들의 대각 4방향을 조사하여 count만큼 물의 양 추가
#         cnt = 0
#         for d in range(4):
#             ny = y + dy4[d]
#             nx = x + dx4[d]
#             # 이 때는 구름의 좌표가 연결되어 있지 않으므로 예외처리)
#             if ny < 0 or nx < 0 or ny >= N or nx >= N:
#                 continue
#             elif board[ny][nx] > 0:
#                 cnt += 1
#         board[y][x] += cnt

#     new_clouds = []
#     for y in range(N):
#         for x in range(N):
#             # 이동한 구름의 좌표와 동일하지 않고, 물의 양이 2 이상인 경우
#             if (y, x) in moved_clouds or board[y][x] < 2:
#                 continue
#             # 물을 2만큼 소비하고 새로운 구름 배열(new_clouds)에 추가
#             board[y][x] -= 2
#             new_clouds.append((y, x))
#     clouds = new_clouds  # 다음 loop에서 사용할 clouds 배열을 new_clouds로 교체

# # 물의 양 합 계산 후 출력
# result = 0
# for y in range(N):
#     for x in range(N):
#         result += board[y][x]
# print(result)
