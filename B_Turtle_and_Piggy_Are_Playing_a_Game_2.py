t = int(input())

for _ in range(t):
    n = int(input())
    nums = list(map(int,input().split()))

    nums.sort()
    left = 0
    right = n - 1
    #take the mid
    turn = True
    while left < right:
        if turn:
            left += 1
            turn = False

        else:
            right -= 1
            turn = True

    print(nums[left])