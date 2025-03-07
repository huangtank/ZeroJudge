# 陣列 模擬
n = int(input())
arr = input()
idx = 1
dis = sum = minn = 0
num = -1
flag = True
for i in range(0, n):
    if arr[i] == 'p':
        j = i
        break
for i in range(j, n):
    if arr[i] == 'p':
        if flag:
            sum -= dis
            num += 2
            if sum < minn:
                minn = sum
                idx = num
        else:
            sum += dis
        flag = False if flag else True
        dis = 0
    else:
        dis += 1
print(idx)