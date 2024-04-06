n = int(input())
target = n
p = 2
result = []
while p*p <= n:
    times = 0
    while target%p == 0:
        times += 1
        target //= p
    if times:
        result.append((p, times))
    if target == 1:
        break
    p += 1
else:
    result.append((target, 1))

ans = []
for a, b in result:
    if b == 1:
        ans.append(str(a))
    else:
        ans.append(f"{a}^{b}")
print(" * ".join(ans))