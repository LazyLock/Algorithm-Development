from collections import Counter
import sys

n = int(sys.stdin.readline())
s = [int(sys.stdin.readline()) for _ in range(n)]

s.sort()

val1 = sum(s) / n
ans1 = round(val1)
ans2 = s[n//2]
ans3 = 0

count = Counter(s).most_common()
if len(s) > 1:
    if count[0][1] == count[1][1]:
        ans3 = count[1][0]
    else:
        ans3 = count[0][0]
else:
    ans3 = s[0]

ans4 = s[-1] - s[0]

print(ans1)
print(ans2)
print(ans3)
print(ans4)