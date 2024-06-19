#前綴和
n = int(input())
a = [int(i) for i in input().split()]
m = 0
for i in range(n):
    a[i] += m
    m = a[i]
print(*a)