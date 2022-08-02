# 1377. 버블 소트
import sys

T = int(sys.stdin.readline())
sort_dic = {}
max_value = 0
index = 0

for i in range(0, T):
    tmp = int(sys.stdin.readline())
    sort_dic[i] = tmp

sort_dic2 = dict(sorted(sort_dic.items(), key=lambda x: x[1]))

for i in list(sort_dic2.keys()):
    tmp = i - index
    if(max_value < tmp):
        max_value = tmp
    index += 1

print(max_value + 1)
