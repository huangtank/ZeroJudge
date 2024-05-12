#LIS, 二分搜
def bin_search(v):
    left, right, mid = 0, len(dp), 0
    while left != right:
        mid = left + (right - left) // 2
        if v >= dp[mid]:
            left = mid + 1
        else:
            right = mid
    return left

n = int(input())
p = []
for _ in range(n):
    p.append(tuple(map(int, input().split())))
p.sort(key=lambda x: x[0] * 10 ** 8 + x[1])
dp = []
for i in range(n):
    index = bin_search(p[i][1])
    if index >= len(dp):
        dp.append(p[i][1])
    else:
        dp[index] = p[i][1]
print(len(dp))