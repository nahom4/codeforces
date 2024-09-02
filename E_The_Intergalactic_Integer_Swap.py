import math
n = int(input())
array = list(map(int,input().split()))

fromLeft = list(array)
fromRight = list(array)


for i in range(1,n):
    fromLeft[i] = math.gcd(array[i],fromLeft[i - 1])


for i in range(n - 2,-1,-1):
    fromRight[i] = math.gcd(array[i],fromRight[i + 1])

ans = 0 
for i in range(n):#[2]
    left,right = 0,0
    if i - 1 >= 0:
        left = fromLeft[i - 1]

    if i + 1 < n:
        right = fromRight[i + 1]

    currGcd = math.gcd(left,right)
    currGcd = max(currGcd,math.gcd(currGcd,array[i]))

    ans = max(ans,currGcd)

print(ans)

    
