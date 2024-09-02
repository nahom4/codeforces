t = int(input())

for _ in range(t):
    num = list(input())
    n = len(num)
    #2050047
    ans = float('inf')
    for i in range(n):
        for j in range(i - 1,-1,-1):
            if not int(num[j] + num[i]) % 25: # 900057 # the game is about what you are including
                ans = min(ans,(n - i) - 1 + ((i - j) -  1))

    print(ans)


        




