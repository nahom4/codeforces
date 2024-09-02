t = int(input())
stack = [1]
overflow =  2 ** 32 - 1

for _ in range(t):
    x = input()

    if 'add' in x:
        stack[-1] = stack[-1] + 1

    if 'for' in x:
        _,num = x.split()
        num = int(num)
        stack.append(num)
        stack.append(0)

    if 'end' in x:
        top = stack.pop()
        stack[-1] = stack[-1] * top
        second = stack.pop()
        stack[-1] = stack[-1] + second


    # print(stack)
val = sum(stack) - 1

if val <= overflow:
    print(val)

else:
    print('OVERFLOW!!!')

