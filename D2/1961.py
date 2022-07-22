# 1961. 숫자 배열 회전
T = int(input())

def matrix_rotate(size, matrix):
    new_matrix = [[0 for col in range(size)]for row in range(size)]
    matrix_pointer = size-1
    for i in range(0, size):
        for j in range(0, size):
            new_matrix[j][i] = matrix[matrix_pointer][j]
        matrix_pointer -= 1
    
    return new_matrix

for test_case in range(1, int(T)+1):
    matrix_size = int(input())
    matrix = []

    for i in range(0, matrix_size):
        input_list = list(map(str, input().split()))
        matrix.append(input_list)

    rotate90 = matrix_rotate(matrix_size, matrix)
    rotate180 = matrix_rotate(matrix_size, rotate90)
    rotate270 = matrix_rotate(matrix_size, rotate180)

    print("#"+ str(test_case))
    for j in range(0, matrix_size):
        tmp_rotate90 = []
        tmp_rotate180 = []
        tmp_rotate270 = []
        for k in range(0, matrix_size):
            tmp_rotate90.append(rotate90[j][k])
            tmp_rotate180.append(rotate180[j][k])
            tmp_rotate270.append(rotate270[j][k])
        
        print("".join(tmp_rotate90), end=" ")
        print("".join(tmp_rotate180), end=" ")
        print("".join(tmp_rotate270))
    