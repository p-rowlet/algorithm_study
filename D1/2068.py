T = int(input())

for test_case in range(1, T+1):
    maxnum = ''
    input_list = list(map(int, input().split()))
    maxnum = max(input_list)
    print("#"+str(test_case) + " "+str(maxnum))