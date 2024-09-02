from collections import Counter

n = int(input())
nums = [(key,count) for key,count in Counter((map(int,input().split()))).items()]

nums.sort()
n = len(nums)
cache = [0] * (n + 1)
cache[0] = nums[0][0] * nums[0][1]
for i in range(1,n):
    num,count = nums[i]
    curr = num * count
    if nums[i - 1][0] + 1 == nums[i][0]:
        cache[i] = max(cache[i - 2] + curr,cache[i - 1])
    else:
        cache[i] = max(cache[i - 1] + curr,cache[i - 2] + curr)
    

print(max(cache))




