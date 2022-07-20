# 1974. 스도쿠 검증

T = int(input())

for test_case in range(1, T+1):
    sudoku = []
    unique_value = True
    for i in range(0, 9):
        input_list = list(map(int, input().split()))
        sudoku.append(input_list)
    
    # 가로값 검증 
    for garo in range(0, 9):
        garo_check = set(sudoku[garo])
        if(len(garo_check)!= 9):
            unique_value = False
        
    #세로값 검증
    if(unique_value != False):
        for sero in range(0, 9):
            sero_list = []
            for se1 in range(0, 9):
                sero_list.append(sudoku[se1][sero])
            
            sero_check = set(sero_list)
            if(len(sero_check) != 9):
                unique_value = False
                break
            
    #사각형 검증
    if(unique_value != False):
        for i in range(0, 9):
            check_list = []
            row = 0
            col = 0

            if(row == 9):
                row = 0
                col +=3
            else:
                row +=3

            #추가하는 대신 리스트를 슬라이싱해서 더하는 방법도 있을 듯
            for j in range(col-3, col):
                for k in range(row-3, row):
                    check_list.append(sudoku[k][j])

            check_set = set(check_list)
            if(len(check_set)!= 9):
                unique_value = False
                break
            

    if(unique_value == True):
        print("#"+ str(test_case) +" 1")
    else:
        print("#"+ str(test_case) +" 0")