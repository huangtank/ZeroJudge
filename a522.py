# dp 0/1背包
for _ in range(int(input())):
    want = int(input())
    input()
    metal = [int(i) for i in input().split()]
    m = len(metal)
    dp = [[False]*(want+1) for _ in range(m+1)]
    for i in range(m+1):
        dp[i][0] = True
    for i in range(1,m+1):
        for j in range(1, want+1):
            dp[i][j] = dp[i-1][j]
            if j >= metal[i-1]:
                dp[i][j] = dp[i][j] | dp[i-1][j-metal[i-1]]
    if dp[-1][-1]:
        print('YES')
    else:
        print('NO')