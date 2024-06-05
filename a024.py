#GCD
x, y = map(int,input().split())
x1 = max(x,y)
y1 = min(x,y)
while y1:
    x1, y1 = y1, x1%y1
print(x1)