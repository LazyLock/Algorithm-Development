import sys

n = int(sys.stdin.readline())
s = []

for i in range(n):
    k = int(sys.stdin.readline())
    s = [str(sys.stdin.readline().rstrip()) for _ in range(k)]
    s.sort()
    is_break = False
    for j in range(k - 1):
        p = len(s[j])
        if s[j] in s[j + 1][:p]:
            is_break = True
            break
    print('NO' if is_break else 'YES')