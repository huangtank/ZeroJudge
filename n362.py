#math
n = int(input())
flag = True
for i in range(2, int(n**0.5)+1):
    if not(n%i):
        for j in range(2, int(i**0.5)+1):
            if not(i%j):
                break
        else:
            ano = n//i
            for h in range(2, int(ano**0.5)+1):
                if not(ano%h):
                    break
            else:
                print(i, ano)
                flag = False
                break
if flag:
    print(0, 0)