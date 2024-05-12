#進位
while True:
    n = bin(int(input()))[2::]
    if n == '0':
        break
    print(f'The parity of {n} is {sum([1 for i in n if i == "1"])} (mod 2).')