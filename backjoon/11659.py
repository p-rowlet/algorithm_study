# 11659. 구간합 구하기 4

# 리스트로 푼 경우 - 시간 초과로 실패

# T = list(map(int, input().split()))
# case = list(map(int, input().split()))

# for i in range(0, T[1]):
#     add_range = list(map(int, input().split()))
#     range_sum = 0
#     for j in range(add_range[0]-1, add_range[1]):
#         range_sum += case[j]
#     print(range_sum)

# 다른 방법으로 풀어보자

import sys

T, T1 = map(int, sys.stdin.readline().split())
case = list(map(int, sys.stdin.readline().split()))

#누적합 배열 생성
range_arr = [0]
for i in range(0, len(case)):
    range_arr.append(range_arr[i]+ case[i])

# 누적합 계산
for i in range(0, T1):
    i, j = map(int, sys.stdin.readline().split())
    print(range_arr[j]-range_arr[i-1])