#此題for c 和 c++ 所以不會過是正常的
n = int(input())
arr = []
vis = [[1]*n for _ in range(n)]
x, y = map(int, input().split())
for _ in range(n):
    arr.append([int(i) for i in input().split()])
q = [[x,y]]
head = 0
time = 1
while head < len(q):
    x,y = q[head];head += 1
    vis[x][y] = 0
    h = arr[x][y]
    for i,j in (1,0),(0,1),(-1,0),(0,-1):
        if x+i >= 0 and y+j >= 0 and x+i < n and y+j < n and vis[x+i][y+j] and abs(arr[x+i][y+j]-h) < 3:
            q.append([x+i,y+j])
            time += 1
            vis[x+i][y+j] = 0
print(time)