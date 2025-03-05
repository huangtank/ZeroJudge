# math 快速冪
import math
def q(a, b, c):
    a = a%c
    ans = 1
    while b != 0:
        if b&1:
            ans = (ans*a)%c
        b >>= 1
        a = (a*a)%c
    return ans
mod = 1000000007
n = int(input())
print(int(((n*(n-1))//(2))%mod*(q(2, n-1, mod))%mod))