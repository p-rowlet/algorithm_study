# 1989 초심자의 회문 검사

T = int(input())

for test_case in range(1, T+1):
    input_list = list(str(input()))

    if(input_list == input_list[::-1]):
        print("#"+ str(test_case)+" 1")
    else:
        print("#"+ str(test_case)+" 0")