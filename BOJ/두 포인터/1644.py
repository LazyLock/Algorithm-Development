n = int(input())

prime_bool = [False, False] + [True] * (n - 1)
m = int(n ** 0.5)

for i in range(2, m + 1):
    if prime_bool[i]:
        for j in range(i * 2, n + 1, i):
            prime_bool[j] = False

answer = [i for i in range(1, n + 1) if prime_bool[i]]

pl, pr = 0, 0
flag = 0
x = answer[0] if answer else 0

while x:
    if x > n:
        x -= answer[pl]
        pl += 1
    else:
        if x == n:
            flag += 1
        if pr == len(answer) - 1:
            break
        pr += 1
        x += answer[pr]

print(flag)