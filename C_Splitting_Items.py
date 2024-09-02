t = int(input())
for _ in range(t):
    n,k = map(int,input().split())

    array = list(map(int,input().split()))

    array.sort(reverse=True)
    sm = sum(array)
    odd = 0
    for i in range(1,n,2): #10 1
        odd += array[i]

    curr = sm - 2 * odd
    for i in range(1,n,2): #go over the odd indices
        if array[i] < array[i - 1]:
            curr -= min(k,array[i - 1] - array[i])
            k -= min(k,array[i - 1] - array[i])

    print(curr)

