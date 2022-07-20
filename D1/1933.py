T = int(input())

# 입력값/2 까지

for i in range(1, T+1):
    if T % i == 0:
        print(str(i), end=" ")