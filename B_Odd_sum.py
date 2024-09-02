n = int(input())
array = list(map(int,input().split()))

negative = list(filter(lambda num : num < 0 and num % 2 != 0,array))
positive = list(filter(lambda num : num > 0,array))
odd = list(filter(lambda num : num % 2 != 0,positive))
even = list(filter(lambda num : num % 2 == 0,positive))

ans = sum(even) + sum(odd)
negative.sort()
odd.sort()
if ans % 2 == 0:
    diff = float("inf")
    if odd:
        diff = min(diff,odd[0])
    if negative:
        diff = min(diff,abs(negative[-1]))

    print(ans - diff)

else:
    print(ans)



