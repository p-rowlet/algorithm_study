# 1945. 간단한 소인수분해

T = int(input())
prime = [2, 3, 5, 7, 11]

for test_case in range(1, int(T)+1):
    test_num = int(input())
    i = 4
    prime_count = [0, 0, 0, 0, 0]
    while(test_num != 1):
        tmp = test_num % prime[i]
        if(tmp == 0):
            prime_count[i] += 1
            test_num = test_num / prime[i]
        else:
            i -= 1
    print("#" + str(test_case), end=" ")
    print(*prime_count)


