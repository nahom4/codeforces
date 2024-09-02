s = input()

stack = []

for i in range(len(s)):
    if s[i] == '(':
        stack.append('(')

    else:
        if stack and stack[-1] == '(':
            stack.pop()
        else:
            stack.append(')')


print(len(s) - len(stack))