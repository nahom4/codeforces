n,k,p = map(int,input().split())

pr = list(map(int,input().split()))
o = list(map(int,input().split()))
pr.sort()
o.sort()

mn = float("inf")
for i in range(k - n + 1):
    ans = float("-inf")
    for j in range(n):
        ans = max(ans,abs(o[i + j] - pr[j]) + abs(o[i + j] - p))

    mn = min(mn,ans)

print(mn)