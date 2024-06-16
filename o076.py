#迴圈
n = int(input())
build = [int(i) for i in input().split()]
ans = 0
for i in range(n):
    now = build[i]
    temp = 1
    for j in range(i+1, n):
        if now > build[j]:
            temp += 1
            now = build[j]
        else:
            break
    ans = max(ans, temp)
print(ans)