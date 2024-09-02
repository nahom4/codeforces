from collections import defaultdict,deque
t = int(input())
for _ in range(t):
    n,m,a,b,c = map(int,input().split())
    p = list(map(int,input().split()))
    graph = defaultdict(list)

    for _ in range(m):
        u,v = map(int,input().split())
        graph[u].append(v)
        graph[v].append(u)

    def bfs(start,end):
        print(start,end)
        level = 0
        queue = deque([start])
        visited = set()
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()

                if node == end:
                    return level
                for nei in graph[node]:
                    if not nei in visited:
                        queue.append(nei)
                        visited.add(nei)

            level += 1

    p.sort()
    routes = [[a,b],[a,c],[b,c]]
    distance = {}
    for route in routes:
        distance[tuple(route)] = bfs(*route)

    for i in range(1,n):
        p[i] += p[i - 1]
    #we have three cities right? yes
    #The thing that is causing is the price
    # we two right the good one and the bad one
    # a -> b and a -> c
    p.append(0)
    ans = 0
    direction = [(a,b),(a,c)]
    left = 0
    cost = 0
    for d in direction:
        curr = p[distance[d]] - p[left - 1]
        left = distance[d]
        curr += 


    #direct pathc a b bc and 2ab bc


    #second path a c c b and 2ac ab

    