import sys

while True:
    d1, d2, d3 = map(int, sys.stdin.readline().split())
    seq = [d1, d2, d3]

    if sum(seq) == 0:
        break

    seq.sort()

    d1 = seq[2]
    d2 = seq[1]
    d3 = seq[0]

    if d1 >= (d2 + d3):
        print("Invalid")
        continue

    if (d1 == d2):
        if (d1 == d3):
            print("Equilateral")
        else:
            print("Isosceles")
    elif (d2 == d3):
        print("Isosceles")
    else:
        print("Scalene")
