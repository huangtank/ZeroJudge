x, y = map(int, input().split())
y = x*60 + y
y += 150
x, y = y//60, y%60
if x>=24:
    x -= 24
x, y = str(x), str(y)
if len(x) == 1:
    x = '0'+x
if len(y) == 1:
    y = '0'+y
print(f'{x}:{y}')