# 1427. 소트인사이드
import sys

n = int(sys.stdin.readline())
T = list(map(int, str(n)))
result = 0
multiply = 1

T.sort()

for i in range(0, len(T)):
    result += multiply * T[i]
    multiply *= 10

print(result)