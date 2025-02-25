#堆疊
arr = input().split()
stack = []
for i in arr:
    if i == '+':
        b, a = stack.pop(), stack.pop()
        stack.append(a+b)
    elif i == '-':
        b, a = stack.pop(), stack.pop()
        stack.append(a-b)
    elif i == '*':
        b, a = stack.pop(), stack.pop()
        stack.append(a*b)
    elif i == '/':
        b, a = stack.pop(), stack.pop()
        stack.append(a//b)
    else:
        stack.append(int(i))
print(stack[0])