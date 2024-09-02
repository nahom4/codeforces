from collections import defaultdict,deque
t = int(input())

for _ in range(t):
    n,k = map(int,input().split())
    graph = defaultdict(list)
    indegree = [0] * (n + 1)
    queue = deque()
    coins = list(map(int,input().split()))
    coins.insert(0,0)
    free = set(map(int,input().split())) #I don't need to make them
    for i in range(1,n + 1):
        edge = list(map(int,input().split()))
    
        indegree[i] = edge[0]
        for v in edge[1:]:
            graph[v].append(i)

    for i in free:
        coins[i] = 0

    ans = [0] * (n + 1)
    for i in range(1, n + 1):
        if indegree[i] == 0:
            queue.append(i)
            ans[i] = coins[i]

    while queue:
        p = queue.popleft()
 
        for nei in graph[p]:
            ans[nei] += min(ans[p],coins[p])
            indegree[nei] -= 1

            if indegree[nei] == 0:
                queue.append(nei)

    for i in range(1,n + 1):
        ans[i] = min(ans[i],coins[i])
    print(*ans[1:])


        

