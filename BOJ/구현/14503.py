import sys

m, n = map(int, sys.stdin.readline().split())
x, y, d = map(int, sys.stdin.readline().split())
room = []

for _ in range(max(n, m)):
    room.append(list(map(int, sys.stdin.readline().split())))


def is_empty(m, n):
    seqs = [[m-1, n], [m, n+1], [m+1, n], [m, n-1]]
    for seq in seqs:
        if (seq[0] < 0) or (seq[1] < 0):
            continue
        else:
            if room[seq[0]][seq[1]] == 0:
                return True
    return False


calcu_seq = [[-1, 0], [0, 1], [1, 0], [0, -1]]
answer = 0


def clean(x, y, d):
    global answer

    if room[x][y] == 0:
        room[x][y] = 2
        answer += 1
    else:
        return

    if is_empty(x, y) == False:
        new_d = int((d + 2) % 4)
        x = x + calcu_seq[new_d][0]
        y = y + calcu_seq[new_d][1]
        if (x < 0) or (y < 0):
            return
        elif room[x][y] == 1:
            return
        else:
            clean(x, y, d)
    else:
        d = int((d + 3) % 4)
        if room[x + calcu_seq[d][0]][y + calcu_seq[d][1]] == 0:
            x = x + calcu_seq[d][0]
            y = y + calcu_seq[d][1]
        clean(x, y, d)


clean(x, y, d)
print(answer)
