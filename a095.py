while True:
   try:
      n, m = map(int, input().split())
   except:
      break
   if n == m:
      print(m)
   else:
      print(m+1)