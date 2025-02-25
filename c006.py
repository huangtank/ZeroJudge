a, b, c, d = map(int, input().split())
while not(a == b == c == d == 0):
    total = 360*3
    total += 9*(a-b if a-b >= 0 else 40+(a-b))
    total += 9*(c-b if c-b >= 0 else 40+(c-b))
    total += 9*(c-d if c-d >= 0 else 40+(c-d))
    print(total)
    a, b, c, d = map(int, input().split())