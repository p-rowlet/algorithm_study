# 2001. 파리 퇴치

T = int(input())

for test_case in range(1, T+1):
    #n_and_m[0] : 파리 면적, n_and_m[1] : 파리채 면적 
    n_and_m = list(map(int, input().split()))
    pari = []
    max_value = 0
    for i in range(0, n_and_m[0]):
        input_list = list(map(int, input().split()))
        pari.append(input_list)

    point_row = 0
    point_col = 0
    while(point_col + n_and_m[1] != n_and_m[0]+1):
        sum_value = 0
        for j in range(point_col, point_col + n_and_m[1]):
            for k in range(point_row, point_row + n_and_m[1]):
                sum_value += pari[j][k]

        if(sum_value > max_value):
            max_value = sum_value
            
        if(point_row + n_and_m[1] == n_and_m[0]):
            point_row = 0
            point_col += 1
        else:
            point_row += 1

    print("#"+ str(test_case) + " " + str(max_value))




