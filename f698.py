#堆疊
arr = input().split()
stack = []
for i in arr:
    if i.isdigit():
        stack.append(int(i))
    else:
        a, b = stack.pop(-2), stack.pop()
        if i == '+':
            stack.append(a+b)
        elif i == '-':
            stack.append(a-b)
        elif i == '*':
            stack.append(a*b)
        else:
            stack.append(a//b)
print(stack[0])
# 70% 測資有誤？