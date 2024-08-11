#字串運算
n, m = map(int,input().split())
ans = []
for i in range(n,m+1):
    i = str(i)
    num = len(i)
    h = 0
    for j in range(len(i)):
        h += int(i[j])**num
    if int(i) == h:
        ans.append(i)
if ans == []:
    print('none')
else:
    print(' '.join(map(str, ans)))