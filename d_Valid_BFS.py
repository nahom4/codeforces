from collections import defaultdict,deque
n = int(input())
graph = defaultdict(list)
for _ in range(n - 1):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

sequence = list(map(int,input().split()))
#root 1
visited = {1}
queue = deque([1])
parent = {1 : -1}
while queue:

    for _ in range(len(queue)):
        node = queue.popleft()
        for n in graph[node]:
            if n not in visited:
                parent[n] = node
                queue.append(n)
                visited.add(n)


index = {-1 : -1}
for i in range(len(sequence)):
    index[sequence[i]] = i

valid = True
for i in range(len(sequence) - 1):
    curr,nxt = sequence[i],sequence[i + 1]
    if index[parent[curr]] > index[parent[nxt]]:
        valid = False

if valid:
    print('Yes')
else:
    print('No')
