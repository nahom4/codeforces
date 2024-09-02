
from collections import Counter

n,m,x,y = map(int,input().split())
mat = []
for _ in range(n):
    mat.append(tuple(input()))

# print(mat)
mat = list(zip(*mat))
mat = [Counter(col) for col in mat]
black,white = [0] * (m + 1),[0] * (m + 1)

for i in range(m):
    black[i] = black[i - 1] + mat[i]['.']
    white[i] = white[i - 1] + mat[i]['#']

black_cost = [float('inf')] * (m + 1)
white_cost = [float('inf')] * (m + 1)
black_cost[-1] = 0
white_cost[-1] = 0
for i in range(m):
    for j in range(min(i + x - 1,m),min(m,i + y)):#we could paint it black or white
        black_cost[j] = min(white_cost[i - 1] + white[j] - white[i - 1],black_cost[j])
        white_cost[j] = min(black_cost[i - 1] + black[j] - black[i - 1],white_cost[j])
        # print(black_cost,j)

print(min(white_cost[-2],black_cost[-2]))