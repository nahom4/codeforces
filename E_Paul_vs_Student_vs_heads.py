n = int(input())
A = list(map(int,input().split()))
m = int(input())
B = list(map(int,input().split()))

#pre process
for i in range(1,n):
    A[i] += A[i - 1]

for i in range(1,m):
    B[i] += B[i - 1]

#[1,2,3,4,5]
#[1,3,6,10,15]

ans = 0
cityB = 0
cityA = 0
while cityA < n and cityB < m: #[11,13,16,21,28] ,[11,18,21,28]
    if A[cityA] > B[cityB]:
        cityB += 1
    elif A[cityA] < B[cityB]:
        cityA += 1

    else:
        ans += 1
        cityA += 1
        cityB += 1

if A[-1] != B[-1]:
    print(-1)
else:
    print(ans)
    