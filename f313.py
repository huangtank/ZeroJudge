#模擬
r,c,k,m=map(int,input().split())
arr=[]
for _ in range(r):
  arr.append(list(map(int,input().split())))
for _ in range(m):
  arr_add=[[0]*c for _ in range(r)] #增加值
  for i in range(r):
    for j in range(c):
      if arr[i][j]==-1: #如果不是城市
        continue
      if i-1>=0: #上
        if arr[i-1][j]!=-1:
          temp=arr[i-1][j]//k
          arr_add[i-1][j]-=temp
          arr_add[i][j]+=temp
      if i+1<r: #下
        if arr[i+1][j]!=-1:
          temp=arr[i+1][j]//k
          arr_add[i+1][j]-=temp
          arr_add[i][j]+=temp
      if j-1>=0: #左
        if arr[i][j-1]!=-1:
          temp=arr[i][j-1]//k
          arr_add[i][j-1]-=temp
          arr_add[i][j]+=temp
      if j+1<c: #右
        if arr[i][j+1]!=-1:
          temp=arr[i][j+1]//k
          arr_add[i][j+1]-=temp
          arr_add[i][j]+=temp
  #print(arr_add)
  for i in range(r):
    for j in range(c):
      arr[i][j]+=arr_add[i][j]
x=0
for i in range(r):
  for j in range(c):
    if x==0:
      if arr[i][j]!=-1:
        ans_m=arr[i][j]
        ans_n=arr[i][j]
        x=1
    else:
      if arr[i][j]>ans_m: #大
        ans_m=arr[i][j]
      if arr[i][j]<ans_n and arr[i][j]!=-1: #小
        ans_n=arr[i][j]
print(ans_n)
print(ans_m)