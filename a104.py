#sort
while True:
   try:
      m = int(input())
      n = list(map(int,input().split()))
   except:
      break
   n.sort()
   print(' '.join(map(str,n)))