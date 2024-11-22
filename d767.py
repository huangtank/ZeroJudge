#歐拉算法
#ep 表示 dfs前序
#depth 表示 ep index 裡的深度
#first 表示每個在 ep index 最先出現
from collections import defaultdict
import sys
n, Q = map(int, input().split())
d = defaultdict(list)
seen = set()
for i in range(1, n+1):
    arr = [int(i) for i in input().split()]
    for j in arr:
        if j != 0:
            d[i].append(j)
            seen.add(j)
sys.setrecursionlimit(30000)
def dfs(n, dt):
    if n in d:
        for i in d[n]:
            if i not in seen:
                seen.add(i)
                first[i] = len(ep)
            ep.append(i)
            depth.append(dt+1)
            dfs(i, dt+1)
            ep.append(n)
            depth.append(dt)
q = [i for i in range(1, n+1) if i not in seen]
ep = [q[0]]
depth = [0]
seen = set()
first = [0]*(n+1)
dfs(q[0], 0)
for _ in range(Q):
    a, b = map(int, input().split())
    a = first[a]; b = first[b]
    if a > b: a, b = b, a
    now = depth[a:b+1].index(min(depth[a:b+1]))+a
    print(ep[now], depth[a]+depth[b]-2*depth[now])
# score 97% #4 TLE(9s)