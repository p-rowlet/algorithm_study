# 간단한 369 게임 (그런데 뭔가 변화구를 던진)

# 첫번째 풀이법 : 숫자를 문자열로 취급하고 풀이하기
T = int(input())

for i in range(1, int(T)+1):
    number = list(str(i))
    is369 = 0
    for j in number:
        if(j in ['3', '6', '9']):
            is369 += 1
    if(is369 == 0):
        print(i, end=" ")
    else:
        print("-" * is369, end=" ")

# 두번째 풀이법 : 정규표현식 사용
# 작동은 되지만, 삼성 코테 사이트에서는 re 모듈이 지원되지 않는다. 
import re

T = int(input())

for i in range(1, int(T)+1):
    is369 = re.compile('[369]')
    result = is369.findall(str(i))
    if(len(result) == 0):
        print(i, end=" ")
    else:
        print("-" * len(result), end=" ")