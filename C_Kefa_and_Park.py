from collections import defaultdict, deque
 
v, m = map(int, input().split())
cats = list(map(int, input().split()))
paths = 0
 
graph = defaultdict(list)
 
# Build our graph
for _ in range(v - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
 
queue = deque([(1, cats[0])])
visited = {1}
 

while queue:
    cur, catCount = queue.popleft()
 
    if catCount > m:
        continue
 
    # Check if cur is a leaf node
    if len(graph[cur]) == 1 and cur != 1:
        paths += 1
 
    for n in graph[cur]:
        if n in visited:
            continue
 
        if cats[n - 1] == 1:
            queue.append([n, catCount + cats[n - 1]])
        else:
            queue.append([n, 0])
 
        visited.add(cur)
 

print(paths)
