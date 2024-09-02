from collections import defaultdict
n = int(input())
graph = defaultdict(list)
for _ in range(n):
    u,_,v = input().split()
    graph[v.lower()].append(u.lower())



def dfs(node):
     
    d = 0
    for n in graph[node]:
        d = max(d,dfs(n))

    return d + 1

print(dfs("polycarp"))

