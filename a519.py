#dp, 費氏
dp = [0,1,2,3]+[0]*80
temp = 4
while True:
    n = int(input())
    if not(n):
        break
    if not(dp[n]):
        for i in range(temp, n+1):
            dp[i] = dp[i-1]+dp[i-2]
        temp = n
        print(dp[n])
    else:
        print(dp[n])