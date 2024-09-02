import heapq
from collections import Counter
t = int(input())

for _ in range(t):
    n = int(input())
    array = list(map(int,input().split()))
    array = list(Counter(array).items())

    array.sort()
    heap = []

    cake = 0
    for i in range(len(array)): #1 2 3 4  round : 1 --> i = 2: 3 cakes 
        num,need = array[i]
        cake += need # cake = 1, 
        heapq.heappush(heap,(-need,num))
    
        if i - len(heap) + 1  < cake: #i = 1    len(heap) = 1   1 - 1 = Around = 0 Bround = 1 
            # print(heap)
            cake += heapq.heappop(heap)[0]
    
    # print(heap)
    print(len(array) - len(heap))
                



