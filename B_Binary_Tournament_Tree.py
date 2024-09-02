t = int(input())

for _ in range(t):
    n = int(input())
    array = list(map(int,input().split()))
    indexMap = dict()
    for i in range(n):
        indexMap[array[i]] = i
    ans = [0] * n

    def dfs(array,depth):
        if not array:
            return

        mx = max(array)
        idx = array.index(mx)
        ans[indexMap[mx]] = depth
        left = array[:idx]
        right = array[idx + 1:]

        dfs(left,depth + 1)
        dfs(right,depth + 1)

    
    dfs(array,0)

    print(*ans)


