t = int(input())
array  = []
for _ in range(t):
    array.append(list(map(int,input().split()))[::-1])

#[0,2],[2,5],[3,8]
def binarySearch(target):
    left,right = -1,len(array)

    while left + 1 < right:
        mid = left + (right - left) // 2
        if array[mid][1] > target:
            right = mid
        else:
            left = mid

    return right

index = 0
for i in range(len(array)):
    index += array[i][1]
    array[i][1] = index

ans = float("-inf")
for i in range(len(array)):
    curr = array[i - 1][1] + 1 if i > 0 else 0
    target = index - curr - 1
    right = binarySearch(target)
    currSkill = array[right][0] + array[i][0]
    ans = max(ans,currSkill)

print(ans)

    






    

