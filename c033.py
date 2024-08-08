#質數
while True:
    try:
        n, c = map(int, input().split())
        ans = []
        for i in range(1, n+1):
            for j in range(2, int(i**0.5)+1):
                if not(i%j):
                    break
            else:
                ans.append(i)
        if 2*c >= len(ans) or (2*c)-1 >= len(ans):
            print(f"{n} {c}:", *ans)
        elif len(ans)%2:
            L = len(ans)//2
            e = ((c*2)-1)//2
            print(f"{n} {c}:", *ans[L-e:L+e+1])
        else:
            L = len(ans)//2
            #" ".join(map(str, ans[L-c//2:L+c//2]))
            print(f"{n} {c}:", *ans[L-c:L+c])
    except:
        break