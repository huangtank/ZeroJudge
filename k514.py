a = [int(i) for i in input().split()]
n = int(input())
arr = [[int(i) for i in input().split()] for _ in range(4)]
for i in range(n):
    b = arr[0][i]//a[0]
    for j in range(1, 4):
        if a[j]*b not in arr[j]:
            break
    else:
        for i in range(4):
            print(a[i]*b,end=" ")
        break
else:
    print(-1)