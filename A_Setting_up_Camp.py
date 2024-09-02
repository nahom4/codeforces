t = int(input())
for _ in range(t):

    i,e,u = map(int,input().split())
    eT = e // 3
    rE = e % 3
    
    if rE == 0 or rE + u >= 3: # 0 0 0
        #valid
        lT = (rE + u) // 3
        if (rE + u) % 3 != 0:
            lT += 1

        print(i + eT + lT)

    else:
        print(-1)
   