T = int(input())

for test_case in range(1, T+1):
    sum = 0
    avg = 0
    input_list = list(map(int, input().split()))
    for cur_input in input_list:
        sum += cur_input
    avg = round(sum / 10)
    print("#"+str(test_case) + " "+str(avg))