#math
many = int(input())
for ii in range(1, many+1):
   x = int(input())
   y = int(input())
   ans = 0
   for i in range(x, y+1):
      if i**0.5 % 1 == 0:
         ans += i
   print(f'Case {ii}: {ans}')