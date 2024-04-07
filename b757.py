import sys

for a in sys.stdin:
    if a == '\n':
        continue
    a = float(a)
    b=((a*9)/5)+32
    print("%g"%(b))