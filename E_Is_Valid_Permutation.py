from collections import Counter
t = int(input())
for _ in range(t):
    n = int(input())
    array = list(map(int,input().split()))

    lis = [array[0]]
    for i in range(1,n - 1):
        lis.append(array[i] - array[i - 1])

    print(lis)
    ct = Counter(lis)

    #list has elements 1 -> n no repeats
    #Things we are certain of 
    #n - 2 Valid numbers must be there
    #hen we can extract the remaining numbers
    #The sum this two should be equal with the odd one out 
    #If this not the case print No


    


