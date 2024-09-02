from collections import defaultdict,Counter
t = int(input())
for _ in range(t):
    n,m = map(int,input().split())
    graph = defaultdict(list)
    for _ in range(m):
        u,v = map(int,input().split())
        graph[u].append(v)
        graph[v].append(u)


    firstLevel = None
    for key in graph:
        if len(graph[key]) == 1:
            firstLevel = key
            break
    
    secondLevel = None

    for node in graph[firstLevel]:
        if len(graph[node]) != 1:
            secondLevel = node
            break

    thirdLevel = None
    for node in graph[secondLevel]:
        if len(graph[node]) != 1:
            thirdLevel = node
            break

    print(len(graph[thirdLevel]),len(graph[secondLevel]) -1)


