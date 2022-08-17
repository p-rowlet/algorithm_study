# 1934. 최소공배수 구하기
import sys

def Euclidean(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

T = int(sys.stdin.readline())

for i in range(0, T):
    a, b = map(int, sys.stdin.readline().split())
    gop = a * b
    lcm = Euclidean(a, b)
    result = gop / lcm
    print(int(result)) 

