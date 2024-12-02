# 質數
def is_prime(a):
    if a < 2:
        return False
    if a in (2, 3):
        return True
    if a % 2 == 0 or a % 3 == 0:
        return False
    # Miller-Rabin test with specific bases for 32-bit integers
    d, s = a - 1, 0
    while d % 2 == 0:
        d //= 2
        s += 1
    
    for i in [2, 7, 61]:
        if i >= a:
            continue
        x = pow(i, d, a)
        if x == 1 or x == a - 1:
            continue
        for j in range(s):
            x = pow(x, 2, a)
            if x == a - 1:
                break
        else:
            return False
    return True

while True:
    try:
        o = int(input())
        if is_prime(o):
            print('質數')
        else:
            print('非質數')
    except:
        break