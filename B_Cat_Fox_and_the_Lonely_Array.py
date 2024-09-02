

for _ in range(t):
    n = int(input())
    array = list(map(int,input().split()))

    lis = [0] * (n + 1)
    lis[-1] = {2 ** i : 0 for i in range(33)}
    for i in range(n - 1):
        lis[i] = calculate(lis[i - 1],array[i])

    #k + k // 2 + k // 3 + k // 4 + ... + 1

t = int(input())

def calculate(map,num):
    bitMask = 2 ** 32
    newMap = {}
    while bitMask > 0:
        if bitMask & num:
            newMap[bitMask] = map[bitMask] + 1
        bitMask = bitMask >> 1

def isPossible(k):

    left = 0

    while left + k < n:
        


