t = int(input())

for _ in range(t):
    A,B,C = map(int,input().split())

    curr = A + B
    ans = -1
   
    if( curr + C) % 2 != 0:
        ans = -1

    else:
        diff = curr - C

        if diff < 0:
            ans = curr

        else:
            ans = C + (diff) // 2

    print(ans)
        


  