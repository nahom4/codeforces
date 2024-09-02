t = int(input())
for _ in range(t):
    n = int(input())
    array = list(map(int,input().split()))

    left = 0
    ans = 0
    while left  < n:#[1 2 3 -1 -2] [1, 3, -2]
        curr = array[left] # curr = -1
                                    #- * -  > 0 + * + > 0
        while left + 1 < n and array[left] * array[left + 1] > 0: 
            curr = max(curr, array[left],array[left + 1]) # curr = -1
            left += 1
        
        ans += curr # -1
        left += 1

    3 + -1 = 2
    print(ans)