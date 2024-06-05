#併查集, disjoint set
def find(x):
    if parent[x] == x: return x
    else:
        parent[x] = find(parent[x])
    return parent[x]

def unite(x, y):
    x = find(x)
    y = find(y)
    if x == y: return
    elif x <= y: parent[x] = y
    else: parent[y] = x

n, m, q = map(int, input().split())
parent = [i for i in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    unite(a, b)
for i in range(q):
    a, b = map(int, input().split())
    if find(a) == find(b):
        print(':)')
    else:
        print(':(')