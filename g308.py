#模擬
n, t = map(int, input().split())
x = [int(i) for i in input().split()]
y = [int(i) for i in input().split()]
seen = [1 for i in range(n)]
score = 0
while seen[t]:
    score += y[t]
    seen[t] = 0
    t = x[t]
print(score)