r, c = map(int, input().split())
target = int(input())
arr = [[i for i in input().split()] for _ in range(r)]
d = {}
for i in range(r):
    for j in range(c):
        if arr[i][j] != "0":
            d[ord(arr[i][j])] = (i, j)
if target <= len(d):
    temp = sorted(d)
    a = 0
    while target:
        print(d[temp[a]][0], d[temp[a]][1])
        target -= 1
        a += 1
else:
    print("Mission fail.")