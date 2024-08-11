#math
T = int(input())
for i in range(T):
    ans = 1
    n = input()
    for j in n:
        ans *= int(j)
    print(ans)