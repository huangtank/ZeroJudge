count = 1
while True:
    n1, n2 = map(int, input().split())
    if not(n1) and not(n2):
        break
    n1_arr = [int(i) for i in input().split()]
    n2_arr = [int(i) for i in input().split()]
    dp = [[1]*(n1) for _ in range(n2)]
    for i in range(1, n2):
        for j in range(1, n1):
            if n1_arr[j-1] == n2_arr[i-1]:
                dp[i][j] = dp[i-1][j-1]+1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    print(f"Twin Towers #{count}")
    count += 1
    print(f"Number of Tiles : {dp[n2-1][n1-1]}")
    print()