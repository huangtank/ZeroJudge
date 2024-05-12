#DAC, tree
for _ in range(int(input())):
    d, i = map(int, input().split())
    n = 1
    for _ in range(d-1):
        if i%2==0:
            i //= 2
            n = 2*n+1
        else:
            if i != 1:
                i //= 2
            n = n*2
    print(n)