from collections import defaultdict,deque,Counter
#it's actually a graph problem
n = int(input())
heads = defaultdict(deque) # {KEY : DEQUE}
count = Counter()
graph = defaultdict(list)
back = [] # to keep track of number inserted at the back
removed = set()

for _ in range(n):
   
    inp = input().split()
    if inp[0] == "insert":
        _,u,v = inp 
        
        if v in heads and heads[v]: # heads[v] DEQUE[0] FIRST OCCURRENCE
            graph[heads[v][0]].append((u,count[u]))
        else:
            back.append((u,count[u]))

        heads[u].append((u,count[u]))
        count[u] += 1
            
    if inp[0] == "remove":
        _,operand = inp
        if operand in heads and heads[operand]: #heads[operand] -> queue [((3,2)]
            removed.add(heads[operand].popleft())   #3,1),

ans = []
def dfs(node):
    stack = [node]
    while stack:
        node = stack.pop()
        if node not in removed:
            ans.append(node[0])

        for nei in graph[node]:
            stack.append(nei)

for val in back:
    dfs(val)

print(' '.join(ans))


