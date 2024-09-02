n,q = map(int,input().split())

array = list(map(int,input().split()))

prefixArray = [0] * (n + 2)

for _ in range(q):
    left,right = map(int,input().split())
    prefixArray[left] += 1
    prefixArray[right + 1] -= 1


for i in range(1,n + 1):
    prefixArray[i] += prefixArray[i - 1]

ans = 0
array.sort(reverse = True)
prefixArray.sort(reverse = True)

for i in range(n):
    ans += prefixArray[i] * array[i]

print(ans)
