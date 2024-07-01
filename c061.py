from math import gcd
while True:
    n, m = map(int, input().split())
    if n == m == 0:
        break
    up = 1
    a = m
    while a:
        up *= n
        n -= 1
        a -= 1
    down = 1
    for i in range(1, m+1):
       down *= i
    D = gcd(up, down)
    print((up//D)//(down//D))
#TLE