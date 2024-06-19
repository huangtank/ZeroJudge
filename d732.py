#二分搜
n, k = map(int, input().split())
a = [int(i) for i in input().split()]
q = [int(i) for i in input().split()]
def biset(a, i):
    L = -1
    R = n
    while R-L > 1:
        mid = (L+R)//2
        if i == a[mid]:
            return mid
        elif i < a[mid]:
            R = mid
        else:
            L = mid
    return -1
for i in range(k):
    print(biset(a, q[i])+1)