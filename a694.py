# 二維前綴和
from itertools import accumulate #累積和
while True:
    try:
        n, m = map(int, input().split())
        arr = [[0]*(n+1)]
        for _ in range(n):
            t = [int(x) for x in input().split()]
            t = list(accumulate([0]+t))
            v = arr[-1]
            v = [a1+a2 for a1, a2 in zip(t,v)]
            arr.append(v)
            #print(arr)
        for _ in range(m):
            x1, y1, x2, y2 = map(int, input().split())
            r = arr[x2][y2]-arr[x2][y1-1]-arr[x1-1][y2]+arr[x1-1][y1-1]
            print(r)
    except EOFError:
        break