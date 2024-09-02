n,k = map(int,input().split())
array = list(map(int,input().split()))


array.sort()
def isPossible(diff):
    
    left,right = 0,n - 1
    operation = 0
    while left < right and operation <= k:

        width = array[right] - array[left]
        if width  > diff:
            currOperation = width - diff
            if currOperation + operation > k:
                return False

            else:
                operation += currOperation

        left += 1
        right -= 1

    return True
            

mn,mx = min(array),max(array)
left, right = -1,mx - mn + 1

while left + 1 < right:
    mid = left + (right - left) // 2

    if isPossible(mid):
        right = mid
    
    else:
        left = mid

print(right)
