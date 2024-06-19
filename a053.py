#判斷
k=int(input())
score=0
if (k<=10 and k>=0):
   score=6*k
   print (str(score))
elif (k>=11 and k<=20):
   score=2*k+40
   print (str(score))
elif (k>=21 and k<=40):
   score=k+60
   print (str(score))
elif (k>40):
   score=100
   print (str(score))