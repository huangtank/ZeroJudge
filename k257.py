    # 字串
n = input()
if len(n) == 2:
    print(n[0]+"00"+n[1])
elif len(n) == 3:
    print(n[0]+"0"+n[1::])
else:
    print(n)