# 1204. 최빈수 구하기
from collections import Counter

T = int(input())

for test_case in range(1, int(T)+1):
    case = int(input())
    numbers = list(map(int, input().split()))
    counting = Counter(numbers).most_common()
    equal = []
    for i in range(0, len(counting)):
        equal.append(counting[i][0])
        if(counting[i][1] == counting[i+1][1]):
            equal.append(counting[i+1][0])
        else:
            break
    equal.sort(reverse=True)
    print("#" + str(test_case) + " " +str(equal[0]))