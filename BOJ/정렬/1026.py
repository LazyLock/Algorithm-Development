import sys

n = int(sys.stdin.readline())
list1 = list(map(int, sys.stdin.readline().split()))
list2 = list(map(int, sys.stdin.readline().split()))
list3 = []
answer = [None] * n
result = 0

for idx, k in enumerate(list2):
    list3.append([idx, k])

list3.sort(key=lambda x: x[1])
list1.sort(reverse=True)

for i in range(n):
    answer[list3[i][0]] = list1[i]

for i in range(n):
    result += answer[i] * list2[i]

print(result)