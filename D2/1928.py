# 1928. Base64 Decoder

# 첫번째 간단한 풀이 - 라이브러리 사용하기 (사용불가)
import base64

T = int(input())

for test_case in range(1, int(T)+1):
    base64_string = str(input())
    base64_byte = base64.b64decode(base64_string)
    base64_decode = base64_byte.decode('utf8')
    print("#" + str(test_case) + " " + str(base64_decode))

# 두번째 풀이 - 매우 정석적인 풀이

T = int(input())

for test_case in range(1, int(T)+1):
    base64_string = list(str(input()))

    base64_encoding = list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/")
    base64_order = [i for i in range(0, 64)]
    string_list = dict(zip(base64_encoding, base64_order))

    baselist = []
    # 입력받은 문자들을 대응하는 숫자로 변경
    for i in range(len(base64_string)):
        tmp = base64_string[i]
        baselist.append(string_list[tmp])
    
    binary_list = []
    #각 숫자를 6자리 이진수로 표현한 다음 합치기
    for i in range(len(baselist)):
        binary_list.append(str(f'{baselist[i]:06b}'))
    binary = "".join(binary_list)
    
    #이어붙인 이진수들을 8자리씩 끊어 십진수로 바꾸기
    length = 8 
    dec_list = [binary[i:i+length] for i in range(0, len(binary), length)]
    
    dec_list2 = []
    for i in range(0, len(dec_list)):
        dec_list2.append(int(dec_list[i], 2))
    
    #끊어낸 10진수를 아스키 코드로 변환
    decode_complate = []
    print("#" + str(test_case) + " ", end="")
    for i in range(0, len(dec_list2)):
        print(chr(dec_list2[i]), end="")
    print()