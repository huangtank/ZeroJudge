a, b, c = map(int, input().split())
d = b**2 - 4*a*c
if d > 0:
    print(f'Two different roots x1={int((-b+d**0.5)//(2*a))} , x2={int((-b-d**0.5)//(2*a))}')
elif d == 0:
    print(f'Two same roots x={int((-b+d**0.5)//(2*a))}')
else:
    print('No real root')