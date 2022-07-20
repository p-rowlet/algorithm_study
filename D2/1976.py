# 1976. 시각 덧셈

import datetime

T = int(input())

for test_case in range(1, T+1):
    input_list = list(map(int, input().split()))

    time_1 = datetime.datetime.strptime(str(input_list[0]) +':'+ str(input_list[1]),"%I:%M")

    time_interval = time_1 + datetime.timedelta(hours=input_list[2], minutes=input_list[3])
    time_value = list(map(int, time_interval.strftime('%I %M').split()))
    print("#"+ str(test_case), end=" ")
    print(*time_value)
    