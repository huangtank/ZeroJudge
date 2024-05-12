#dp, 費氏
import sys
dp = [1, 2] + [0]*(500)
temp = 2
for i in sys.stdin:
    i = int(i)-1
    if dp[i] == 0:
        for j in range(temp, i+1):
            dp[j] = dp[j-1]+j
        temp = i
        print(dp[i])
    else:
        print(dp[i])