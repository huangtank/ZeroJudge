#math
while True:
    try:
        n = int(input())
    except:
        break
    print(int(((n+1)*((n*n)-n+6))/6))