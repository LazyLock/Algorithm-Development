import sys

n = int(sys.stdin.readline())

for _ in range(n):
    # 초기화 부분
    def_seq = sys.stdin.readline().rstrip()
    m = int(sys.stdin.readline())
    arr_seq = sys.stdin.readline().rstrip()

    if arr_seq == '[]':
        arr_seq = list()
    else:
        arr_seq = list(arr_seq[1:-1].split(','))

    # error_flag : error를 표시할지 아닐지, reverse_cnt : 뒤집어주는 횟수 카운트
    error_flag = False
    reverse_cnt = 0

    for s in def_seq:
        if s == "R":
            reverse_cnt += 1
        else:
            if len(arr_seq) == 0:
                error_flag = True
                break
            else:
                if reverse_cnt % 2 == 0:
                    arr_seq.pop(0)
                else:
                    arr_seq.pop()
    if error_flag:
        print("error")
    else:
        if reverse_cnt % 2 == 1:
            arr_seq.reverse()
            print("[" + ','.join(arr_seq) + "]")
        else:
            print("[" + ','.join(arr_seq) + "]")
