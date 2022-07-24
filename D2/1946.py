# 1946. 간단한 압축 풀기
T = int(input())

for test_case in range(1, int(T)+1):
    test_text = int(input())
    count = 0
    print("#" + str(test_case) +" ")
    
    for i in range(0, test_text):
        input_text = list(input().split())
        for j in range(0, int(input_text[1])):
            if(count == 10):
                count = 0
                print()
            print(input_text[0], end="")
            count += 1
    print()