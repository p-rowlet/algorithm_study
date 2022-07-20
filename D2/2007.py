T = int(input())

for test_case in range(1, T+1):
    input_list = list(input())
    pattern1 = []
    pattern2 = [0]
    point = 1
    
    for i in range(0, len(input_list)):
        pattern1.append(input_list[i])
        pattern2.pop(0)
        
        if(i == 0):
            pattern2.append(input_list[point])
            point += 1
            continue

        for j in range(0, 2):
            pattern2.append(input_list[point])
            point += 1
        
        if(pattern1 == pattern2):
            print("#"+ str(test_case) + " " + str(len(pattern1)))
            break
