#BFS
from collections import deque

def BFS():
    direct = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while queue:
        x, y = queue.popleft()
        for dx, dy in direct:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == 0 and vitex[nx][ny] == float('inf'):
                vitex[nx][ny] = vitex[x][y] + 1
                queue.append((nx, ny))

    m = 0
    for i in range(n):
        for j in range(n):
            if vitex[i][j] != -1 and vitex[i][j] != float('inf'):
                m = max(m, vitex[i][j])
    return m

n = int(input())
arr = []
for _ in range(n):
    arr.append([int(i) for i in input().split()])
vitex = [[-1 if arr[i][j] == -1 else float('inf') for j in range(n)] for i in range(n)]
queue = deque()

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            queue.append((i, j))
            vitex[i][j] = 0
print(BFS())
#TLE