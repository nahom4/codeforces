from collections import defaultdict
t = int(input())

for _ in range(t):
    n,x,y = map(int,input().split())

    array = list(map(int,input().split()))
    hashMap = defaultdict(int)
    ct = 0
    for i in range(n):
        rmX = array[i] % x
        rmY = array[i] % y

        if rmX % rmY == 0:
            ct += hashMap[rmX]
            hashMap[rmX] += 1


    print(ct)
