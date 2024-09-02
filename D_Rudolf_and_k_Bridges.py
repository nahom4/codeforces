from collections import deque
t = int(input())
for _ in range(t):
    n,m,k,d = map(int,input().split())

    ans = []
    for _ in range(n): # d - 1 
        row = list(map(int,input().split()))
        row = list(map(lambda x : x + 1,row))
        cache = [0] * m 
        # 0 1 2 3 4 5 4 3 2 1 0
        # 1 3 4 5 6 7 8 7 6 0 0
        # d = 4
        queue = deque([0])
        cache[0] = row[0]
        for i in range(1,m): #0 3 3 0
            cache[i] += cache[queue[0]] + row[i] #6
            
            while queue and cache[queue[-1]] > cache[i]: #monotonic queue
                queue.pop()

            queue.append(i)  # [1 6] 
            if (i - queue[0]) > d: 
                queue.popleft()
            
        ans.append(cache[-1]) # the cost at  a particular row

    #pick k of them
    left = 0
    runningSum = 0
    res = sum(ans)
    for right in range(len(ans)):
        runningSum += ans[right]
        if right >= k: 
            runningSum -= ans[left]
            left += 1
            
        if right - left + 1 == k:
            res = min(res,runningSum) 


    print(res)

    