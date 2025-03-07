# for if
while True:
    try:
        n, m = map(int, input().split())
        if m == 0:
            print("Go Kevin!!")
        else:
            if (1-n+m)%m == 0:
                print("Go Kevin!!")
            else:
                print("No Stop!!")
    except EOFError:
        break