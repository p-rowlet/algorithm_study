# 1948. 날짜 계산기
import datetime

T = int(input())

for test_case in range(1, int(T)+1):
    input_time = list(map(int, input().split()))

    start_date = datetime.date(1990, input_time[0], input_time[1])
    target_date = datetime.date(1990, input_time[2], input_time[3])

    d_day = target_date - start_date
    print("#" + str(test_case) +" " + str(int(d_day.days + 1)))