n  = int(input())
m = 360
grid = [[False] * m for _ in range(n)]
turns = []

for i in range(n):
    turn = int(input())
    turns.append(turn)



first_turn = turns[0]
left = (-1 * first_turn) % 360
right = (first_turn) % 360
grid[0][left] = True
grid[0][right] = True

for i in range(1,n)
    for j in range(m):

        if grid[i - 1][j]:
    
            left = (j - val) % 360
            right = (j + val) % 360

            grid[i][left]=  True
            grid[i][right] = True

if grid[n - 1][0]:
    print("YES")

else:
    print("NO")
