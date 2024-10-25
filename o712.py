# 陣列
m, n, k, r, c = map(int, input().split())
arr = []
dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
cycle = 0
for _ in range(m):
    arr.append([int(i) for i in input().split()]+[-1])
arr.append([-1]*(n))
score = 0
ans = 0
while arr[r][c]:
    ans += 1
    score += arr[r][c]
    arr[r][c] -= 1
    if score%k == 0: cycle = (cycle+1)%4
    while True:
        nr, nc = dir[cycle][0]+r, dir[cycle][1]+c
        if arr[nr][nc] >= 0:
            r, c = nr, nc
            break
        cycle = (cycle+1)%4
print(ans)  