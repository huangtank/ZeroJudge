#字典
d={'A':1,'B':10,'C':19,'D':28,'E':37,\
   'F':46,'G':55,'H':64,'I':39,'J':73,\
   'K':82,'L':2,'M':11,'N':20,'O':48,\
   'P':29,'Q':38,'R':47,'S':56,'T':65,\
   'U':74,'V':83,'W':21,'X':3,'Y':12,\
   'Z':30}

n = input()

ans = int(n[0])*8+int(n[1])*7+int(n[2])*6+int(n[3])*5+int(n[4])*4+int(n[5])*3+int(n[6])*2+int(n[7])+int(n[8])

for i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
    if (ans + d[i]) % 10 == 0:
        print(i,end='')