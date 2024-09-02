import heapq
n = int(input())
array = []
for _ in range(n):
    
    array.append(list(map(int,input().split()))) 

rooms = 0
ans = 0
heap = []
array.sort()

for i in range(n):
    s,e,r = array[i]
    while heap and  heap[0][0] < s:
        rooms -= heapq.heappop(heap)[1]

    rooms += r
    ans = max(ans,rooms)

    heapq.heappush(heap,(e,r))

print(ans)

