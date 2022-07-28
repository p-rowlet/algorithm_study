# 11660. 구간합 구하기 5

import sys

T, T1 = map(int, sys.stdin.readline().split())

# 일반 배열 생성 
case = []
for i in range(0, T):
    case.append(list(map(int, sys.stdin.readline().split()))) 

#누적합 배열 생성
case_sum = [[0 for j in range(T+1)] for i in range(T+1)]
case_sum[1][1] = case[0][0]

# 1행과 1열 담기
for i in range(2, T+1):
    case_sum[1][i] = case_sum[1][i-1] + case[0][i-1]
    case_sum[i][1] = case_sum[i-1][1] + case[i-1][0]

#나머지 누적합 배열 담기
for i in range(2, T+1):
    for j in range(2, T+1):
        case_sum[i][j] = case[i-1][j-1] + case_sum[i][j-1] + case_sum[i-1][j] - case_sum[i-1][j-1]

# 누적합 계산
for i in range(0, T1):
    i, j, k, l = map(int, sys.stdin.readline().split())
    print(case_sum[k][l] - case_sum[k][j-1] - case_sum[i-1][l] + case_sum[i-1][j-1])