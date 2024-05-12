#DFS
for _ in range(int(input())):
    n = int(input())
    num = [i for i in range(1, n+1)]
    result = [[]]
    for i in num:
        new = [j+[i] for j in result]
        print(f'This is {new}')
        result.extend(new)
    result.sort(key=lambda x: [len(x),x])
    result[0] = [0]
    for i in result:
        print('{'+','.join(map(str,i))+'}')
    print()