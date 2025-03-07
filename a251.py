#math
for _ in range(int(input())):
    arr = [int(i) for i in input().split()]
    n = arr[0]
    arr.pop(0)
    for i in range(4, n):
        arr.append(arr[i-4]+arr[i-1])
    arr.sort()
    print(arr[(n+1)//2-1])