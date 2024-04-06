import sys

for i in sys.stdin:
    n = int(i)
    target = n
    p = 2
    ans = 0
    while p*p <= n:
        times = 0
        while target%p == 0:
            times += 1
            target //= p
        if times:
            ans += p*times
        if target == 1:
            break
        p += 1
    else:
        ans += target
    print(ans)