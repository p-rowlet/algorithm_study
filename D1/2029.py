T = int(input())

for test_case in range(1, T + 1):
    input_list = list(map(int, input().split()))
    input1 = input_list[0] // input_list[1]
    input2 = input_list[0] % input_list[1]
    print("#" + str(test_case) + " " + str(input1) + " " + str(input2))

#몫과 나머지를 튜플로 => divmod 
