n = int(input())

i = 1
k = 1

while k < n:
    k = i * (i + 1) / 2
    k = k * 6 + 1
    i += 1

print(i)