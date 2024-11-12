# DP硬幣
coins = [1, 5, 10, 25, 50]
dp = [0]*(7490)
dp[0] = 1
for coin in coins:
    for i in range(coin, 7490):
        dp[i] += dp[i-coin]
while True:
    try:
        n = int(input())
        print(dp[n])
    except EOFError:
        break