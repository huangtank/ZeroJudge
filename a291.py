#模擬
from sys import stdin, stdout
opt = ''
for s in stdin:
    if(s.strip() == ''): continue
    ans = s.strip().split()
    cnt = {str(i): 0 for i in range(10)}
    for c in ans: cnt[c] += 1
    w = int(stdin.readline())
    for _ in range(w):
        A, B, C = 0, 0, cnt.copy()
        t = stdin.readline().strip().split()
        bchk = []
        for i in range(4):
            d = t[i]
            if C[d]:
                if d == ans[i]:
                    A += 1
                    C[d] -= 1
                else: 
                    bchk.append(d)
        for d in bchk:
            if C[d]:
                B += 1
                C[d] -= 1
        opt += '{}A{}B\n'.format(A, B)
stdout.write(opt.strip())