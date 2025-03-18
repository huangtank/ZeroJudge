#模擬
n, m = map(int, input().split())
arr = []
change = []
for i in range(n):
  arr.append(list(map(int, input().split())))
wt = input()
for i in range(n):
  change.append(list(map(int, input().split())))
for i in range(n):
  for j in range(m):
    s = 0
    for k in range(m):
      s += change[i][k]
    for k in range(n):
      if k != i:
        s += change[k][j]
    if s%2 != 0:
      if arr[i][j] == 0:
        arr[i][j] = 1
      else:
        arr[i][j] = 0
for i in arr:
  print(*i)