#math
n = int(input())
ans = [0, 0, 0]
for ii in range(n):
   N = int(input())
   if N % 3 ==0:
      ans[0] += 1
   elif N % 3 == 1:
      ans[1] += 1
   else:
      ans[2] += 1
print(' '.join(map(str,ans)))