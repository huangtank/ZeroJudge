#迴圈
k = int(input())
M, a, wrong = -2, 0, 0
for _ in range(k):
    t, s = map(int, input().split())
    if s > M:
        M = s
        a = t
    if s == -1:
        wrong += 1
print(M-k-wrong*2 if M-k-wrong*2 >= 0 else 0, a)