# 快速冪
import sys
input = sys.stdin.readlines()
for i in input:
    b, p, m = map(int, i.split())
    print(pow(b, p, m))
#	AC (71ms, 4.9MB)