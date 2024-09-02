t = int(input())

for _ in range(t):
    n = int(input())
    nums = list(map(int,input().split()))

    if nums.count(nums[0]) == n:
        print('NO')
        continue

    nums.sort()
    nums.reverse()
    back = nums.pop()
    nums.insert(0,back)

    print('YES')
    print(*nums)