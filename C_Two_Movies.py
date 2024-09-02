t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))

    aSum,bSum = 0,0
    negative,positive = 0,0
    for i in range(n):
        if a[i] > b[i]:
            aSum += a[i]

        elif b[i] > a[i]:
            bSum += b[i]

        else:
            if a[i] == -1:
                negative += 1
            if a[i] == 1:
                positive += 1

    
       if aSum < bSum:
        aSum,bSum = bSum,aSum

    while negative:
        aSum -= 1
        negative -= 1
        if aSum < bSum:
            aSum,bSum = bSum,aSum

    while positive:
        bSum += 1
        positive -= 1
        if aSum < bSum:
            aSum,bSum = bSum,aSum

    print(min(aSum,bSum))



    
        
       

        

