#貪心
while True:
    n, d, r = map(int, input().split())
    if n == d == r == 0:
        break
    morning = sorted([int(i) for i in input().split()])
    evening = sorted([int(i) for i in input().split()], reverse = True)
    morning = [evening[i] + morning[i] for i in range(n)]
    finish = sum([i-d for i in morning if i > d])
    print(finish*r)