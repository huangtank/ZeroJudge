S = ['普通', '吉', '大吉']
m, d = map(int, input().split())
print(S[(m*2+d)%3])