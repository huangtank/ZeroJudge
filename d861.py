#走訪問題
def find(a, b):
    if not b: 
        return ""
    v = b[-1]
    idx = a.index(v)
    return v+find(a[:idx], b[:idx])+find(a[idx+1:], b[idx:-1])
x = input()
y = input()
print(find(x, y))