import math
t = int(input())
for _ in range(t):
    n,a,b = map(int,input().split())
    nums = list(map(int,input().split()))

    g = math.gcd(a,b)
    nums.sort()
    for i in range(n): # 1 1 2 6
        nums[i] = nums[i] % g

    # print(nums)
    mn = nums[-1] - nums[0]
    for i in range(1,n): #1 3 4 4   3 3 5
        mn = min(mn,abs(nums[i] - (nums[i - 1] + g)))
        # print(mn)
    print(mn)

