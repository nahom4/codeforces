from collections import Counter
t = int(input())

for _ in range(t):
    n,f,k = map(int,input().split())
    array = list(map(int,input().split()))
    ct = Counter(array)
    target = array[f - 1]
    array.sort(reverse=True)

    # print(array)

    start = array.index(target) + 1
    end = start + ct[target] - 1

    #NNNNNKNNNNNNNNNN

    '''
        2 1 1
        2 1
    '''
    if k < start:
        print("NO")

    elif k >= end:
        print("YES")

    else:
        print("MAYBE")
 