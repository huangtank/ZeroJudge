#迴文
n = input()
for i in range(len(n)//2):
    if n[i] != n[-1-i]:
        print('no')
        break
else:
    print('yes')