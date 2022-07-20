T = int(input())

input_list = list(map(int, input().split()))
input_list.sort()
middle = int(T/2)
print(str(input_list[middle]))