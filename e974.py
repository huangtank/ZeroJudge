# list
r, c, n = map(int, input().split())
x = (n//2 if n%2 else n//2-1)%r #單數餘數
y = (n//2)%c #雙數餘數
arr = [[0]*(c) for _ in range(r)]
now = 1
for i in range(r):
    for j in range(c):
        arr[x+i if x+i < r else x+i-r][y+j if y+j < c else y+j-c] = now
        now += 1
for h in arr:
    print(*h)