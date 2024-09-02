t = int(input())

for _ in range(t):
    n = int(input())
    array = list(map(int, input().split()))

    # Separate odd and even elements based on their indices
    odd = []
    even = []
    for i in range(n):
        if i == 0:
            continue
        if i % 2 == 0 :
            even.append([array[i], i])
        else:
            odd.append([array[i], i])

    # Sort the even elements in descending order and the odd elements in ascending order
    even.sort(reverse=True)
    odd.sort()

    ans = [0] * n
    val = n

    # Assign high values to the odd-indexed elements
    for _, index in odd:
        ans[index] = val
        val -= 1

    val = 1

    # Assign low values to the even-indexed elements
    for _, index in even:
        ans[index] = val
        val += 1

    ans[0] = val
    # Print the rearranged array
    print(*ans)
