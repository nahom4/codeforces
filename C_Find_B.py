t = int(input())
for _ in range(t):
    n,q = map(int,input().split())
    nums = list(map(int,input().split()))

    prefix = [0] * (n + 1)
    count = [0] * (n + 1)
    for i in range(n):
        count[i] = count[i - 1]
        prefix[i] = prefix[i - 1]
        if nums[i] == 1:
            count[i] += 1
            
        else:
            prefix[i] += nums[i]

    
    for _ in range(q):
        l,r = map(int,input().split())
        ones = count[r - 1] - count[l - 2]
        sm = prefix[r - 1] - prefix[l - 2]

        if (r - l + 1) > 1 and  sm - (r - l + 1)  >= 0: #none of them can be zero so we still need (r - l + 1) - ones are good ones
            print('YES')
        
        else:
            print('NO')

    
