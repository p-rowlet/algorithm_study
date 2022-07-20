T = list(map(int, input().split()))

if(T[0] == 1):
    if(T[1] == 2):
        print("B")
    else:
        print("A")
elif(T[0] == 2):
    if(T[1] == 1):
        print("A")
    else:
        print("B")
elif(T[0] == 3):
    if(T[1] == 1):
        print("B")
    else:
        print("A")
