# dp零錢
c, n = map(int, input().split())
dp = [float("inf")]*(c+1)
dp[0] = 0
coins = []
for _ in range(n):
    coins.append(int(input()))
for coin in coins:
    for i in range(coin, c+1):
        dp[i] = min(dp[i], dp[i-coin]+1)
print(dp[i])