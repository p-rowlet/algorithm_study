# 1986 지그재그 숫자

T = int(input())

for test_case in range(1, T+1):
    input_value = int(input())
    result = 0

    for i in range(1, input_value+1):
        if(i%2 == 0):
            result -= i
        else:
            result += i
    print("#"+ str(test_case) +" "+ str(result))
