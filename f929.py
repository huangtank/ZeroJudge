# 優先佇列
import heapq
zero = []
seen = set()
n = int(input())
arr = [int(i) for i in input().split()]
for i in range(n): 
    if arr[i] == 0: 
        heapq.heappush(zero, i)
        seen.add(i)
for _ in range(int(input())):
    a = [int(i) for i in input().split()]
    if a[0] == 1:
        if len(zero):
            temp = heapq.heappop(zero)
            seen.remove(temp)
    elif a[0] == 2:
        if a[1] not in seen:
            heapq.heappush(zero, a[1])
            seen.add(a[1])
    else:
        print(zero[0] if len(zero) else -1)