for _ in range(int(input())):
    a, b, c, d = map(int, input().split())
    ans = [a, b, c, d]
    if d-c == c-b == b-a:
        ans.append(2*d-c)
    else:
        ans.append(d*(b//a))
    print(*ans)