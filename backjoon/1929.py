# 1929. 소수 구하기
import sys
import math

def isPrime(num):
    root_num = math.sqrt(num)
    for i in range(2, math.ceil(root_num)+1):
        if(num % i == 0):
            return False
    return True

n, m = map(int, sys.stdin.readline().split())
if n == 1 or n == 2:
    n = 3
    print(2)

for i in range(n, m+1):
    root_num = math.sqrt(i)
    if(isPrime(i) == True):
        print(i)