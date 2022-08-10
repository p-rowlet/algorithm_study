# 1920. 원하는 정수 찾기

import sys

n = sys.stdin.readline()
num1 = list(map(int, sys.stdin.readline().split()))
num1.sort()

m = sys.stdin.readline()
num2 = list(map(int, sys.stdin.readline().split()))

def search(nums, target):
    def binary_search(left, right):
        if left <= right:
            mid = (left + right) // 2
            if nums[mid] < target :
                return binary_search(mid+1, right)
            elif nums[mid] > target :
                return binary_search(left, mid-1)
            else:
                return 1
        else: 
            return 0
    return binary_search(0, len(nums) - 1)

for i in num2:
    print(search(num1, i))
