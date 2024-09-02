from collections import defaultdict,deque
t = int(input())

for _ in range(t):
    input()
    n,k = map(int,input().split())
    friends = list(map(int,input().split()))
    graph = defaultdict(list)
    queue = deque()
    visited = {1}

    for _ in range(n - 1):
        u,v = map(int,input().split())
        graph[u].append(v)
        graph[v].append(u)

    for node in friends:
        queue.append((node,node))
        visited.add(node)

    queue.append((1,1))
    
    valid = False
    while queue:
        room,player = queue.popleft()
        if player == 1 and len(graph[room]) == 1 and room != 1:
            valid = True

        for n in graph[room]:
            if n not in visited:
                queue.append((n,player))
                visited.add(n)
    
    if valid:
        print('YES')

    else:
        print('NO')
