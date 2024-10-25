# 迴圈
n = int(input())
w1, w2, h1, h2 = map(int, input().split())
num = [int(i) for i in input().split()]
size1 = w1*w1*h1
size2 = w2*w2*h2
ans = 0
for i in num:
    if i <= size1:
        ans = max(ans, i//(w1*w1))
        size1 = max(0, size1-i)
    elif i-size1 <= size2:
        ans = max(ans, size1//(w1*w1)+(i-size1)//(w2*w2))
        size1 = 0
        size2 = max(0, size2-(i-size1))
    else:
        ans = max(ans, size1//(w1*w1)+size2//(w2*w2))
    if size1 == size2 == 0:
        break
print(ans)