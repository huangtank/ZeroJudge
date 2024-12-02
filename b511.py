# dp, 排序
n = int(input())
coins = [int(i) for i in input().split()]
target = int(input())
dp = [[] for i in range(target+1)]
dp[0].append([0 for _ in range(n)])
for coin in range(n):
    for i in range(coins[coin], target+1):
        for j in dp[i-coins[coin]]:
            temp = j.copy()
            temp[coin] += 1
            dp[i].append(temp)
ans = sorted(dp[target].copy())
for i in ans:
    print("("+",".join(map(str, i))+")")