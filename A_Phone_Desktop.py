import math
t = int(input())
for _ in range(t):
    x,y = map(int,input().split())
    
    d = y // 2
    rm = y % 2
    s = d * 7
    if rm > 0:
        d += 1
        s += 11
    x -= s
    if x > 0:
        d += math.ceil(x / 15)

    print(d)