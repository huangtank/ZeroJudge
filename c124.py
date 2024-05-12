#BFS
def BFS(x, y, z):
    q = [(x, y, z)]
    head = 0
    flag = False
    while head < len(q):
        x, y, z = q[head]; head += 1
        for dx, dy, dz in (0, 0, 1), (0, 1, 0), (1, 0, 0), (0, 0, -1), (0, -1, 0), (-1, 0, 0):
            if x+dx >= 0 and y+dy >= 0 and z+dz >= 0 and x+dx < R and y+dy < C and z+dz < L and not(vis[z+dz][x+dx][y+dy]):
                if arr[z+dz][x+dx][y+dy] == '.':
                    q.append((x+dx, y+dy, z+dz))
                    vis[z+dz][x+dx][y+dy] = 1
                    arr[z+dz][x+dx][y+dy] = arr[z][x][y]+1
                elif arr[z+dz][x+dx][y+dy] == 'E':
                    arr[z+dz][x+dx][y+dy] = arr[z][x][y]+1
                    flag = True
                    break
        if flag:
            break

while True:
    L, R, C = map(int, input().split())
    if L == R == C == 0:
        break
    arr = []
    vis = [[[0]*(C) for _ in range(R)] for _ in range(L)]
    for i in range(L):
        temp = []
        for j in range(R):
            temp.append(list(input()))
        input()
        arr.append(temp)
    x, y, z = 0, 0, 0
    nx, ny, nz = 0, 0, 0
    for i in range(L):
        for j in range(R):
            if 'S' in arr[i][j]:
                z, x, y = i, j, arr[i][j].index('S')
    for i in range(L):
        for j in range(R):
            if 'E' in arr[i][j]:
                nz, nx, ny = i, j, arr[i][j].index('E')
    vis[z][x][y] = 1
    arr[z][x][y] = 0
    BFS(x, y, z)
    if str(arr[nz][nx][ny]).isdigit():
        print(f'Escaped in {arr[nz][nx][ny]} minute(s).')
    else:
        print('Trapped!')