t = int(input())

for _ in range(t):
    n = int(input())
    array = list(map(int,input().split()))
    array.sort() #I am thinking in the lines of greedy TBH

    running_sum = 0
    valid = True
    for i in range(n): #1 1 2 5 7
        if array[i] != 1 and running_sum < array[i]:
            valid = False
        
        running_sum += array[i]

    if valid:
        print('YES')
    else:
        print('NO')


