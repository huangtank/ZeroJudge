def BFS(x, y, e):
    q = [(x, y)]
    head = 0
    while head < len(q):
        x, y = q[head]; head += 1
        for i, j in (0, 1), (1, 0), (0, -1), (-1, 0):
            if x+i >= 0 and y+j >= 0 and x+i < r and y+j < c and vis[x+i][y+j] and arr[x+i][y+j] == e:
                q.append((x+i, y+j))
                vis[x+i][y+j] = 0
for n in range(1, int(input())+1):
    d = {}
    r, c = map(int, input().split())
    arr = []
    vis = [[1]*(c) for _ in range(r)]
    for _ in range(r):
        arr.append(list(input()))
    for i in range(r):
        for j in range(c):
            if vis[i][j]:
                vis[i][j] = 0
                BFS(i, j, arr[i][j])
                if arr[i][j] not in d:
                    d[arr[i][j]] = 1
                else:
                    d[arr[i][j]] += 1
    a = sorted(d.items(), key=lambda x: (-x[1], x[0]))
    print(f'World #{n}')
    for i, j in a:
        print(f'{i}: {j}')