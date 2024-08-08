#模擬
n = int(input())
while n:
    step = []
    dic = [1, 2, 3]
    for _ in range(n):
        step.append(input())
    for i in step:
        if i == 'north':
            dic[0], dic[1], dic[2] = 7-dic[1], dic[0], dic[2]
        elif i == 'south':
            dic[0], dic[1], dic[2] = dic[1], 7-dic[0], dic[2]
        elif i == 'east':
            dic[0], dic[1], dic[2] = dic[2], dic[1], 7-dic[0]
        else:
            dic[0], dic[1], dic[2] = 7-dic[2], dic[1], dic[0]
    print(dic[0])
    n = int(input())