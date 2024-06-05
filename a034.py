# 2 bit
while True:
    try:
        n = int(input())
    except:
        break
    print('{0:b}'.format(n))