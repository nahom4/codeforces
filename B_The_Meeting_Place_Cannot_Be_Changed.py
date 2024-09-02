delta = 1e-6
def check(arr,speed,mid):
    index = None
    maxValue = float("-inf") 

    for i in range(len(arr)):
        diff = abs(arr[i] - mid)
        time = diff / speed[i]
        if time >= maxValue:
            index = arr[i]
            maxValue = time

    return index >= mid,maxValue


n = int(input())

x = list(map(int, input().split()))   
speed = list(map(int,input().split()))

pairs = list(zip(x, speed))

sorted_pairs = sorted(pairs, key=lambda pair: pair[0])
x, speed = zip(*sorted_pairs)
ans = float("inf")
left,right = min(x) - 1, max(x) + 1
while (right - left) > delta:
    mid = left + (right - left) / 2   

    valid,time = check(x,speed,mid)
    ans = min(ans,time)
    if valid:
        left = mid
    else:
        right = mid

print(ans)






