# 2005 파스칼의 삼각형

T = int(input())

for test_case in range(1, T+1):
    input_value = int(input())

    pascal = []
    print("#"+ str(test_case))

    for i in range(0, input_value):
        pascal.append([])
        for j in range(0, i+1):
            if(j in [0, i]):
                pascal[i].append(1)
            else:
                pascal[i].append(pascal[i-1][j-1] + pascal[i-1][j])
    
    for k in range(0, input_value):
        for l in range(0, k+1):
            print(pascal[k][l], end=" ")
        print()
