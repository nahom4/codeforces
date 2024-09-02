import bisect
s = input()
n = len(s)

next_greater = [0] * n
stack = []
array = [None] * n

array[-1] = s[-1]
for i in range(n - 2,-1,-1):
    array[i] = min(s[i],array[i + 1])

stack = []

def can_remove(char,index):
    idx = bisect.bisect_left(array,char)

    if idx >= n:
        return char == array[-1]
    return idx <= index

stack = []
ans = []
for i in range(n):

    while stack and can_remove(stack[-1],i):
        char = stack.pop()
        ans.append(char)

    stack.append(s[i])
ans.extend(stack[::-1])
print(''.join(ans))
