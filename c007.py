# 字串
n = 0
while True:
    try:
        N = input()
        for i in N:
            if i == '"':
                n += 1
                if n%2 == 1:
                    print("``", end="")
                else:
                    print("''", end="")
            else:
                print(i, end="")
        print('')
    except EOFError:
        break