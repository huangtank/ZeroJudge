# BFS
def BFS(r, c, data):
    global now
    if data == 0: return 0
    for x, y in ((0, 1), (1, 0), (-1, 0), (0, -1)):
        if arr[r+x][c+y] > 0:
            BFS(r+x, c+y, arr[r+x][c+y])
        elif arr[r+x][c+y] != -1 and seen[r+x][c+y]:
            seen[r+x][c+y] = 0
            now += 1
    return 0

m, n, Q = map(int, input().split())
arr = []
for _ in range(m):
    temp = [int(i) for i in input().split()]+[-1]
    if -2 in temp:
        r, c = _, temp.index(-2) #初始炸彈
    arr.append(temp)
arr.append([-1]*n)
seen = [[1]*(n+1) for _ in range(m+1)]
q = [(r, c)]
head = 0
now = 1 # 目前格數
if Q == 1: print(0)
else:
    while head <= len(q):
        r, c = q[head]; head += 1
        for x, y in ((0, 1), (1, 0), (-1, 0), (0, -1)):
            if arr[r+x][c+y] > 0:
                BFS(r+x, c+y, arr[r+x][c+y])
            elif arr[r+x][c+y] != -1 or seen[r+x][c+y]:
                seen[r+x][c+y] = 0
                arr[r+x][c+y] = arr[r][c]+1
                q.append((r+x, c+y))
                now += 1
            if now >= Q:
                print(max([max(i) for i in arr]))
                break
# WA