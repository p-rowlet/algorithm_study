# 1850. 최대공약수
import sys

def Euclidean(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

a, b = map(int, sys.stdin.readline().split())
gcd = Euclidean(a, b)
for i in range(0, gcd):
    print("1", end = "")