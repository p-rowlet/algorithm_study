# 1954. 달팽이 숫자
T = int(input())

for test_case in range(1, int(T)+1):
    list_index = int(input())
    
    snail = new_matrix = [[0 for col in range(list_index)]for row in range(list_index)]

    min_add = 0
    max_add = list_index-1

    row_add = 0
    col_add = 0

    row_index = 0
    col_index = 0

    for i in range(1, (list_index * list_index)+1):
        if((row_index == min_add and col_index == min_add) or (row_index == min_add -1 and col_index == min_add)):
            row_add = 1
            col_add = 0
        elif(row_index == max_add and col_index == min_add):
            row_add = 0
            col_add = 1
        elif(row_index == max_add and col_index == max_add):
            row_add = -1
            col_add = 0
        elif(row_index == min_add and col_index == max_add):
            max_add -= 1
            min_add += 1
            col_add = -1
            row_add = 0

        snail[col_index][row_index] = i
        row_index += row_add
        col_index += col_add
    
    print("#"+ str(test_case))

    for j in range(0, list_index):
        for k in range(0, list_index):
            print(snail[j][k], end=" ")
        print()