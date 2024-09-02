from collections import defaultdict,deque
n,m = map(int,input().split())
graph = defaultdict(list)
color = [0] * n
queue = deque()
indegree = [0] * (n +  1)
for _ in range(m):

    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)
    indegree[u] += 1
    indegree[v] += 1



visited = set()
def dfs(node):

    stack = [node]
    valid = True
    while stack:
        node = stack.pop()
        if node in visited:
            continue

        visited.add(node)

        valid = valid & (len(graph[node]) == 2)
       
        for nei in graph[node]:      
            stack.append(nei)

    return valid


count = 0
for node in graph:
    if node in visited:
        continue

    if dfs(node):
        count += 1

print(count)




