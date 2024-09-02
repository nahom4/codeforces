t = int(input())

for _ in range(t):
    n = int(input())

    array = list(map(int,input().split()))
    ans = [i for i in range(1,n + 1)]
    for i in range(1,n):
        if array[i] == array[i - 1]:
            ans[i],ans[i - 1] = ans[i - 1],ans[i]

    valid = True
    for i in range(n):
        if i + 1 == ans[i]:
            valid = False

    if valid:
        print(*ans)
    else:
        print(-1)

