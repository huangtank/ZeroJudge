for t in range(1, int(input())+1):
    ans = []
    d = {}
    for i in input():
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    for i in d:
        if d[i] == 1:
            continue
        for j in range(2, int(d[i]**0.5)+1):
            if not(d[i]%j):
                break
        else:
            ans.append(i)
    print(f'Case {t}: ',end='')
    if ans:
        print(''.join(sorted(ans)))
    else:
        print('empty')