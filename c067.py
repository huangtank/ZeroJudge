#陣列
n = int(input())
time = 1
while n:
    num = [int(i) for i in input().split()]
    print(f"Set #{time}")
    M = sum(num)/len(num)
    print(f"The minimum number of moves is {int(sum([i-M for i in num if i > M]))}.")
    print()
    n = int(input())
    time += 1