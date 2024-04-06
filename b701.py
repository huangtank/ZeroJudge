def BFS(x, y):
    ans = [y,x,y,x,1] #W N E S A
    q = [(x, y)]
    head = 0
    while head < len(q):
        x, y = q[head];head += 1
        for i, j in (0, 1), (1, 0), (0, -1), (-1, 0):
            if x+i >= 0 and y+j >= 0 and x+i < m and y+j < n and arr[x+i][y+j] and not(vis[x+i][y+j]):
                q.append((x+i, y+j))
                ans = [min(ans[0], y+j), min(ans[1], x+i), max(ans[2], y+j), max(ans[3], x+i), ans[4]+1]
                vis[x+i][y+j] = 1
    return ans

n, m = map(int, input().split())
arr = []
vis = [[0]*(m) for _ in range(n)]
for _ in range(m):
    arr.append([int(i) for i in input().split()])

for i in range(m):
    for j in range(n):
        if arr[i][j] == 1 and not(vis[i][j]):
            vis[i][j] = 1
            print(*BFS(i,j))