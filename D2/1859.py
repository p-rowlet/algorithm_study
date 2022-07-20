# 1859. 백만 장자 프로젝트

T = int(input())

for test_case in range(1, T+1):
    input_max = int(input())
    input_list = list(map(int, input().split()))
    
    max_value = 0
    total_profit = 0
    for i in range(len(input_list) -1, -1, -1):
        if (input_list[i] > max_value):
            max_value = input_list[i]
        else:
            total_profit += max_value - input_list[i]
    print("#"+ str(test_case) + " " + str(total_profit))


