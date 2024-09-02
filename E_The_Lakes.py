from collections import deque
t = int(input())
for _ in range(t):
    n,m =map(int,input().split())
    matrix = [list(map(int,input().split())) for _ in range(n)]
    mx = 0
    direction = [(1,0),(-1,0),(0,1),(0,-1)]
    visited = set()

    def bfs(row,col):
        
        queue = deque([(row,col)])
        depth = 0
        while queue:
            r,c = queue.popleft()
            if (r < 0 or r >= n ) or (c < 0 or c >= m):
                continue

            if (r,c) in visited:
                continue

            if matrix[r][c] == 0:
                continue

            depth += matrix[r][c]
            visited.add((r,c))

            for x,y in direction:
                nx,ny = x + r,y + c
                queue.append((nx,ny))
                    
        return depth
                
                
    for i in range(n):
        for j in range(m):
            if not (i,j) in visited:
                mx = max(mx,bfs(i,j))
                
    print(mx)
