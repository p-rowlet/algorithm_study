# 2750. 수 정렬하기
import sys

T = int(sys.stdin.readline())
sort_array = []

for case in range(1, T+1):
    tmp = int(sys.stdin.readline())
    sort_array.append(tmp)

sort_array.sort()

for i in range(0, T):
    print(sort_array[i])
