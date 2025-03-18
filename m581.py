n = int(input())
arr = [int(i) for i in input().split()]
seen = set()
n = int(input())
while n:
    if n-1 in seen:
        print("Wrong")
        break
    seen.add(n-1)
    arr[n-1] = 0
    n = int(input())
else:
    print("Werewolves" if -1 in arr else "Townsfolk")