n,d = map(int,input().split())
s = input()
cache = {}
#let me do it bottom up
def dp(i):
    if i >= len(s) - 1:
        return 1


    if s[i] == '0':
        return float("inf")

    if i in cache:
        return cache[i]

    mn = float("inf")
    for j in range(1,d + 1):
        mn = min(mn,dp(i + j))

    cache[i] = mn + 1
    return cache[i]

ans = dp(0)
if ans == float("inf"):
    print(-1)
else:
    print(ans - 1)