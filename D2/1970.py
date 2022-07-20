# 1970. 쉬운 거스름돈

T = int(input())

for test_case in range(1, T+1):
    input_value = int(input())

    print("#"+ str(test_case))
    coin = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    for i in coin:
        reminder = input_value // i
        if(reminder >= 1):
            print(reminder, end=" ")
            input_value = input_value - (i * reminder)
        else:
            print("0", end=" ")
    print()
