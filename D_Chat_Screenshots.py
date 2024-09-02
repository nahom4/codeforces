from collections import defaultdict,deque
t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    graph = defaultdict(list)
    indegree = [0] * (n + 1)
    queue = deque()
    for _ in range(k):
        order = list(map(int,input().split()))[1:]

        for i in range(len(order) - 1):
            graph[order[i]].append(order[i + 1])
            indegree[order[i + 1]] += 1
    
    for i in range(1,n + 1):
        if indegree[i] == 0:
            queue.append(i)

    
    ans = []
    while queue:
        node = queue.popleft()
        ans.append(node)

        for nei in graph[node]:
            indegree[nei] -= 1

            if indegree[nei] == 0:
                queue.append(nei)

    if len(ans) == n:
        print('YES')
    else:
        print('NO')

        
