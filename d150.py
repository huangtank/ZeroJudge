#貪心
for _ in range(int(input())):
    n = int(input())
    arr = [int(i) for i in input().split()]
    arr.sort(reverse = True)
    ans = 0
    for i in range(2, n, 3):
        ans += arr[i]
    print(ans)