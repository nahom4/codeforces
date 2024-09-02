t = int(input())

for _ in range(t):
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    b.sort()
    a.sort()
    leftA,rightA = 0,len(a) - 1
    leftB,rightB = 0,len(b) - 1

    sm = 0
    for i in range(n):
        first = abs(a[leftA] - b[rightB])
        second = abs(a[rightA] - b[leftB])

        if first > second:
            leftA += 1
            rightB -= 1

        else:
            rightA -= 1
            leftB += 1

        sm += max(first,second)
        
    print(sm)

