# 迴圈
n = int(input())
while n:
    for _ in range(8):
        for i in range(n):
            if _%2:
                print("."*n+"#"*n+"."*n+"#"*n+"."*n+"#"*n+"."*n+"#"*n)
            else:
                print("#"*n+"."*n+"#"*n+"."*n+"#"*n+"."*n+"#"*n+"."*n)
    n = int(input())