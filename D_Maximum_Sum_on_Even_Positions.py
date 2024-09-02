t = int(input())

for _ in range(t):
    n = int(input())
    array = list(map(int,input().split()))

    curr = 0
    for i in range(0,n,2):
        curr += array[i]
    
    runningSum  = 0
    evenMin = 0
    oddMin = 0
    currAns = 0

    for i in range(n):
        if i % 2 == 0:
            runningSum -= array[i]
        else:
            runningSum += array[i]

        if i % 2 == 0:
            currAns = max(currAns,runningSum - evenMin)
            evenMin = min(evenMin,runningSum)

        else:
            currAns = max(currAns,runningSum - oddMin)
            oddMin = min(oddMin,runningSum)

    print(currAns + curr)


