for _ in range(int(input())):
    e, f, c = map(int, input().split())
    e = e+f
    ans = 0
    while e//c:
        e, ans = (e%c)+(e//c), e//c+ans
    print(ans)