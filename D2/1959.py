# 1959 두 개의 숫자열

T = int(input())

for test_case in range(1, int(T)+1):
    list_index = list(map(int, input().split()))
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))

    if(len(a_list) > len(b_list)):
        # 파이써닉한 스왑
        a_list, b_list = b_list, a_list
    
    pointer = 0
    max_value = 0
    
    while(pointer + len(a_list) < len(b_list) + 1):
        value = 0
        for i in range(0, len(a_list)):
            value = value + (a_list[i] * b_list[pointer+i])
        if(value > max_value):
            max_value = value
        pointer += 1
    
    print("#"+ str(test_case)+ " " + str(max_value))

