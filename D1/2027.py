num = 1
for i in range(1, 6):
    for j in range(1, 6):
        if(j == num):
            print("#", end="")
        else:
            print("+", end="")
    print("")
    num += 1
