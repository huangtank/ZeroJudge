#判斷
input()
for h in [int(i) for i in input().split()]:
    if h%3 == 0 and h%2 == 0:
        print(1, end=" ")
    elif h%2 != 0 and h%3 != 0:
        print(2, end=" ")
    elif h == int(h**0.5)**2 or h%2 == 0 and h%7 != 0:
        print(3, end=" ")
    else:
        print(0, end=" ")