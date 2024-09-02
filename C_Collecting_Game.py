t = int(input())

for _ in range(t):
    n = int(input())
    nums = list(map(int,input().split()))
    nums = [(num,i) for i,num in enumerate(nums)]
    prefix_sum = []
    nums.sort()
    running_sum = 0
    for num,idx in nums:
        running_sum += num
        prefix_sum.append((num,idx,running_sum))
    
    prev = float('inf')
    ans = [0] * n
    for i,(num,idx,running_sum) in enumerate(prefix_sum[::-1]):
         #[(1, 2, 1), (2, 4, 3), (4, 3, 7), (5, 1, 12), (20, 0, 32)
        if running_sum  < prev:
            count = n - i - 1

        prev = num

        ans[idx] = count 
    
    print(*ans)
