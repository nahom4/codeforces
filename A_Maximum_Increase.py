#stupid dp
n = int(input())
array = list(map(int,input().split()))

ans = [1] * n

for i in range(1,n):
    if array[i - 1] < array[i]:
        ans[i] += ans[i - 1] 

print(max(ans))