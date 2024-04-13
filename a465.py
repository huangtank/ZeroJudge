for i in range(1, int(input())+1):
    n = int(input())
    jump = 0
    arr = list(input())
    ans = 0
    while jump < n:
        if arr[jump] == '.':
            jump += 3
            ans += 1
        else:
            jump += 1
    print(f'Case {i}: {ans}')