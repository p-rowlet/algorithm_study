# 1984. 중간 평균값 구하기

T = int(input())

for test_case in range(1, T+1):
    input_list = list(map(int, input().split()))
    result = round((sum(input_list) - min(input_list) - max(input_list)) / 8)
    print("#"+ str(test_case) +" "+ str(result))