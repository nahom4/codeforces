from collections import defaultdict
t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    array = list(map(int,input().split()))
    graph = defaultdict(list)

    for _ in range(n - 1):
        u,v = map(int,input().split())
        graph[u].append(v)
        graph[v].append(u)


    print(graph)
    '''
        1 

        2  4

    3        5
        2 2 n, k
        1 3 array
        1 2   1 --> 2  target == 2
    '''
    target = 0
    for i in range(n):
        target ^= array[i]

    print(target)
    visited = set()
    cuts = 0
    def dfs(node):
        stack = [node]
        global cuts
        curr = 0
        while stack:
            node = stack.pop()
            if node in visited:
                continue
            
            visited.add(node)
            
            print(curr)
            for nei in graph[node]:
                stack.append(nei)

            curr ^= array[node - 1]
            print(curr,'before',node)
            if curr == target:
                print(curr,'about',target)
                cuts += 1
                curr = 0

        
        print(curr,target,cuts)
        return curr

    if not target or (not dfs(1) and cuts > 1):
        print('YES')
    else:
        print('NO')
    