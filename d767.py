#歐拉算法+RMQ 求 lca
#ep 表示 dfs前序出現的節點
#depth 表示 ep index 裡的深度
#first 表示每個在 ep index 最先出現
from collections import defaultdict
import sys
input = sys.stdin.readline
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
# RMQ
n = len(depth)
bin_log = [0] * (n + 1)
for i in range(2, n + 1):
    bin_log[i] = bin_log[i // 2] + 1

m = [[(0, 0)] * (bin_log[n] + 1) for _ in range(n)]

for i in range(n):
    m[i][0] = (depth[i], i)

LOG = bin_log[n] + 1
for k in range(1, LOG):
    for i in range(n - (1 << k) + 1):
        left = m[i][k - 1]
        right = m[i + (1 << (k - 1))][k - 1]
        m[i][k] = left if left[0] <= right[0] else right  # 儲存值較小的 (值, 索引)
#查詢
def query(L, R):
    j = bin_log[R - L + 1]
    left = m[L][j]
    right = m[R - (1 << j) + 1][j]
    return left[1] if left[0] <= right[0] else right[1]  # 返回 (值, 索引)
for _ in range(Q):
    a, b = map(int, input().split())
    a = first[a]; b = first[b]
    if a > b: a, b = b, a
    now = query(a, b)
    print(ep[now], depth[a]+depth[b]-2*depth[now])
# score 99% #6 TLE(3s)