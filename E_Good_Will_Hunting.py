n,m = map(int,input().split())

ct = -1
ans = 0
while n or m: # 01 10 1000 i got it
    ct += 1
    if n & 1 != m & 1: #if both are on
        ans = (2*(1 << ct) - 1)    
    n = n >> 1
    m = m >> 1

print(ans)