for _ in range(int(input())):
    n = input()
    if len(n) == 5:
        print(3)
    else:
        if n[0] == 'o' and n[1] == 'n' or n[0] == 'o' and n[2] == 'e' or n[1] == 'n' and n[2] == 'e':
            print(1)
        else:
            print(2)