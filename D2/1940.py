# 1940. 가랏! RC카

T = int(input())

for test_case in range(1, int(T)+1):
    line = int(input())
    speed = 0
    running = 0

    for i in range(0, line):
        input_speed = list(map(int, input().split()))
        if(input_speed[0] == 1):
            speed += input_speed[1]
        if(input_speed[0] == 2):
            speed -= input_speed[1]
            if(speed < 0):
                speed = 0
        running += speed

    print("#" + str(test_case) + " " + str(running))
    
