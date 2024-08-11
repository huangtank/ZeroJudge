#字串
n = input()
n = n[::-1]
while n[0] == '0' and len(n) != 1:
    n = n[1::]
print(n)