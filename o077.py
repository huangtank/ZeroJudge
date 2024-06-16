#二維
h, w, n = map(int, input().split())
arr = [[0]*w for _ in range(h)]
art = []
for _ in range(n):
    art.append([int(i) for i in input().split()])
for i in range(h):
    for j in range(w):
        for x in art:
            if abs(i-x[0])+abs(j-x[1]) <= x[2]:
                arr[i][j] += x[3]
for i in arr:
    print(*i)