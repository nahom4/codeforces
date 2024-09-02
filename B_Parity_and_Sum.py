t = int(input())
for _ in range(t):
    n = int(input())
    array = list(map(int,input().split()))

    odd = list(filter(lambda num : num % 2 != 0,array))
    even = list(filter(lambda num : num % 2 == 0,array))

    # print(odd,even)
    biggest = 0
    if odd:
        biggest = max(odd)
    ct = 0
    even.sort()
    for num in even:#[3, 1, 1] [4, 6, 2]
        #either 1 or two operations
        ct += 1
        if num >= biggest:
            # print("here",num,biggest)
            biggest += num
            ct += 1

        biggest += num

    ct = min(ct,len(even) + 1)
    if odd:
        print(ct)
    else:
        print(0)