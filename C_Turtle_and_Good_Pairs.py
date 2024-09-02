from collections import Counter
from heapq import heappop,heapify,heappush
t = int(input())
for _ in range(t):
    n = int(input())
    cnt = Counter(input())
 
    max_heap = [ (-c , ch) for ch,c in cnt.items()]
    heapify(max_heap)

    result = ""

    last = None
    #I want to print the values step by step right
    while max_heap:
        #just pop twice
        ct,char = heappop(max_heap)
        ct += 1

        result += char
        if max_heap:
            ct2,char2 = heappop(max_heap)
            ct2+= 1
            result += char2
            if ct2:
                heappush(max_heap,(ct2,char2))

        if ct:
            heappush(max_heap,(ct,char))

    print(result)
