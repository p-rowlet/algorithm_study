# 1928. Base64 Decoder

# 첫번째 간단한 풀이 - 라이브러리 사용하기 (사용불가)
# import base64

# T = int(input())

# for test_case in range(1, int(T)+1):
#     base64_string = str(input())
#     base64_byte = base64.b64decode(base64_string)
#     base64_decode = base64_byte.decode('utf8')
#     print("#" + str(test_case) + " " + str(base64_decode))

# 두번째 풀이 - 매우 정석적인 풀이

T = int(input())

for test_case in range(1, int(T)+1):
    base64_string = str(input())