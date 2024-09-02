t = int(input())
for _ in range(t):
    n = int(input())
    ct = 0
    for _ in range(n):
        a,b = map(int,input().split())

        if a - b > 0:
            ct += 1

    print(ct)
