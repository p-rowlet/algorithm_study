# 1966. 숫자를 정렬하자
T = int(input())

for test_case in range(1, int(T)+1):
    max_sort = int(input())
    input_list = list(map(int, input().split()))
    input_list.sort()

    print("#"+ str(test_case), end=" ")
    print(*input_list)
