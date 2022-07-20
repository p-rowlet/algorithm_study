T = int(input())

for test_case in range(1, T+1):
    input_list = list(map(int, input().split()))
    size = ""
    if input_list[0] == input_list[1]:
        size = "="
    elif input_list[0] > input_list[1]:
        size = ">"
    elif input_list[0] < input_list[1]:
        size = "<"
    print("#"+str(test_case) + " "+size)