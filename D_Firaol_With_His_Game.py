import heapq
t = int(input())
for _ in range(t):
    n,s = map(int,input().split())
    nums = list(map(int,input().split()))
    heap = []
    running_sum = 0
    ans = 0
    for i in range(n):
        running_sum += nums[i]
        print(heap)
        if heap and heap[0][0] + running_sum <= s:
            ans = heap[0][0] + 1
            print(ans)

        else:
            break
       
        heapq.heappush(heap,(-nums[i],i))
        # print(heap

    if not ans:
        print(ans)

    else:
        print(0)
    