import heapq
import sys
n, k = map(int, sys.stdin.readline().split())
songs = []
heap = []
for _ in range(n):
    songs.append(list(map(int,input().split())))

songs.sort(key = lambda p: -p[1])

maxBeauty = 0
runningSum = 0
for i in range(n):
    l,b = songs[i]
    heapq.heappush(heap,l)

    runningSum += l

    while len(heap) > k:
        runningSum -= heapq.heappop(heap)

    
    maxBeauty = max(maxBeauty,runningSum * b)


print(maxBeauty)



