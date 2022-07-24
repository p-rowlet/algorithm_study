# 1288. 새로운 불면증 치료법

T = int(input())

for test_case in range(1, int(T)+1):
    sheep = int(input())
    count = 1
    sheep_tmp = str(sheep)
    sheep_set = set(list(sheep_tmp))
    sheeps = 0

    while(len(sheep_set) < 10):
        sheeps = sheep * count
        sheep_set.update(list(str(sheeps)))
        count += 1

    print("#" + str(test_case) + " " + str(sheeps))