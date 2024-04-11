for i in range(1, int(input())+1):
    arr = []
    M = 0
    for _ in range(10):
        temp = input().split()
        M = max(M, int(temp[1]))
        arr.append(temp)
    print(f'Case #{i}:')
    for j,g in arr:
        if int(g) == M:
            print(j)