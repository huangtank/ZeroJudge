#bin
n = input()
for i in range(len(n)-1):
   print(abs(ord(n[i])-ord(n[i+1])),end='')