#math
t, r = map(int, input().split())
if t-(1+r)*abs(t//(1+r)):
    print(1)
else:
    print(0)