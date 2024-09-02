from collections import Counter
N, M = map(int,input().split())
array = list(map(int,input().split()))

sm = 0
rmCounter = Counter()
rmCounter[0] = 1
ans = 0
for i in range(N):
    sm += array[i]

    rm = sm % M
    ans += rmCounter[rm]
    rmCounter[rm] += 1


print(ans)
    
