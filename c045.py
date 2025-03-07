# list
arr = []
while True:
    try:
        arr.append(input())
    except EOFError:
        break
for i in range(max([len(i) for i in arr])):
    for j in range(len(arr)-1, -1, -1):
        if len(arr[j]) > i:
            print(arr[j][i], end="")
        else:
            print(" ", end="")
    print()