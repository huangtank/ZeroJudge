#枚舉
def made(x, n, a):
    if len(a) == n: return a
    for i in x:
        ans.add(made(x, n, a+i))
K = input()
n = int(input())
S = input()
S_have = set()
for i in range(len(S)-n+1):
    S_have.add(S[i:i+n])
ans = set()
made(K, n, "")
ans = sorted([i for i in ans if i != None])
for i in ans:
    if i not in S_have:
        print(i)
        break