d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500,'M': 1000}
t = {1000: "M", 900: "CM", 500: "D", 400: "CD", 100: "C", 90: "XC", 50: "L", 40: "XL", 10: "X", 9: "IX", 5: "V", 4: "IV", 1:"I" }

def rton(r):
    result = 0
    for i in range(len(r)-1):
        now = d[r[i]]
        nex = d[r[i+1]]
        if (now >= nex):
            result += now
        else:
            result -= now
    result += d[r[-1]]
    return result

while True:
    a = input().split()
    if len(a) == 1:
        break
    a, b = a[0], a[1]
    an, bn = 0, 0
    an, bn = rton(a), rton(b)
    n = abs(bn-an)
    if not(n):
        print('ZERO')
        continue
    ans = ''
    for key, value in t.items():
        while n >= key:
            n -= key
            ans += value
    print(ans)