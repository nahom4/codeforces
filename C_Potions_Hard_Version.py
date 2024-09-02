import heapq
n = int(input())
array = list(map(int,input().split()))

heap = []
runningSum = 0
for i in range(n):
    if array[i] > 0:
        runningSum += array[i]
        heapq.heappush(heap,array[i])
    
    else:
        runningSum += array[i]
        heapq.heappush(heap,array[i])

        while runningSum < 0:
            runningSum -= heapq.heappop(heap)

print(len(heap))

