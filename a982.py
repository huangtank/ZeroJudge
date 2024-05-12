#BFS
dx = [0, 1, 0, -1] 
dy = [1, 0, -1, 0]
def BFS(x, y):
    q = [(x, y)]
    head = 0
    while head < len(q):
        x, y = q[head]; head += 1
        for i in range(4):
            if x+dx[i] >= 0 and y+dy[i] >= 0 and x+dx[i] < n and y+dy[i] < n:
                if not(vis[x+dx[i]][y+dy[i]]):
                    vis[x+dx[i]][y+dy[i]] = 1
                    if arr[x+dx[i]][y+dy[i]] =='.':
                        arr[x+dx[i]][y+dy[i]] = arr[x][y] + 1
                        q.append((x+dx[i], y+dy[i]))
                    else:
                        arr[x+dx[i]][y+dy[i]] = 0

n = int(input())
arr = []
vis = [[0]*(n) for _ in range(n)]
for _ in range(n):
    arr.append(list(input()))
x, y = 1, 1
if arr[x][y] == '#':
    print('No solution!')
else:
    vis[x][y] = 1
    arr[x][y] = 1
    BFS(x, y)
    if str(arr[n-2][-2]).isdigit():
        print(arr[n-2][n-2])
    else:
        print('No solution!')