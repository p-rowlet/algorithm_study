# 2023. 신기한 소수
import sys
import math
n = int(sys.stdin.readline())
num_r = 10

prime_num = [2, 3, 5, 7]
prime_num2 = [1, 3, 7, 9]

def isPrime(num):
    root_num = math.sqrt(num)
    for i in range(2, math.ceil(root_num)):
        if(num % i == 0):
            return False
    return True

if(n != 1):
    for i in range(1, n):
        tmp = []
        for j in prime_num:
            for k in prime_num2:
                tmp_num = j * num_r + k
                if(isPrime(tmp_num)):
                    tmp.append(tmp_num)
        prime_num = tmp
    num_r *= 10

for i in prime_num:
    print(i)