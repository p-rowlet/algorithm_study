import sys
sys.setrecursionlimit(10**7)

number = int(input("몇까지 입력? : "))

def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num-1)

print(factorial(number))