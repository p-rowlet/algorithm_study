T = int(input())

# 생각해보니 정규표현식을 사용하는 방법도 있었을 지도... 
for test_case in range(1, T+1):
    input_value = str(input())
    input_list = list(input_value)
    
    year = "".join([input_list[0], input_list[1], input_list[2], input_list[3]])
    month = "".join([input_list[4], input_list[5]])
    day = "".join([input_list[6], input_list[7]])

    month_num = int(month)
    day_num = int(day)
    if not month_num in range(1, 13):
        print("#"+str(test_case) + " -1")
    elif month_num in [1, 3, 5, 7, 8, 10, 12] :
        if not day_num in range(1, 32):
            print("#"+str(test_case) + " -1")
        else : 
            print("#"+str(test_case) + " "+ "/".join([year, month, day]))  
    elif month_num in [4, 6, 9, 11]:
        if not day_num in range(1, 31):
            print("#"+str(test_case) + " -1")
        else : 
            print("#"+str(test_case) + " "+ "/".join([year, month, day]))  
    elif(month_num == 2):
        if not day_num in range(1, 29):
            print("#"+str(test_case) + " -1")
        else : 
            print("#"+str(test_case) + " "+ "/".join([year, month, day]))       
    