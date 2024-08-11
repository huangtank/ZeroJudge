#math
while True:
   try:
      n = list(map(int,input().split()))
   except:
      break
   N = n[0]
   n = sum(n[1::])
   n /= N
   print('no' if n > 59 else 'yes')