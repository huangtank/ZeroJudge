#for
q= 1
while q!=0:
    q=int(input())
    for i in range (1,q):
        if (i%7==0):
            pass
        elif (i==q-1):
            print(str(i))
        else:
            print(str(i), end=" ")