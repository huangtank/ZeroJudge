#矩陣
while True:
  try:
    m,n = map(int,input().split())
  except:
    break
  m01=[]
  for i in range(m):
    m01.append([ int(j) for j in input().split()])
  for i in range(n):
    for j in range(m):
      if j == m-1:
        print(m01[j][i])
      else:
        print(m01[j][i], end=' ')