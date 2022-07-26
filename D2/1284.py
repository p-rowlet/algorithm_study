# 1284. 수도 요금 경쟁

T = int(input())

for test_case in range(1, T+1):
    # 0 : P / 1 : Q 2: R 3: S / 4 : W(사용량)
    input_list = list(map(int, input().split()))
    P = input_list[0]
    Q = input_list[1]
    R = input_list[2]
    S = input_list[3]
    W = input_list[4]

    a_water = P * W
    b_water = Q if W <= R else Q + S * (W - R)

    print("#" + str(test_case), end=" ")
    print(a_water if a_water < b_water else b_water)
