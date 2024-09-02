#range update and count those that are greater than k
n,k,q = map(int,input().split())

prefixArray = [0] * (200000 + 2)

for _ in range(n):
    left,right = map(int,input().split())
    prefixArray[left] += 1
    prefixArray[right + 1] -= 1

for i in range(1,len(prefixArray)):
    prefixArray[i] += prefixArray[i - 1]

#count
count = [0] * len(prefixArray)
if prefixArray[0] > k:
    count[0] = 1

for i in range(1,len(prefixArray) - 1):
    count[i] = count[i - 1]
    if prefixArray[i] >= k:
        count[i] += 1


for _ in range(q):
    left,right = map(int,input().split())
    ans = count[right] - count[left - 1]
    print(ans)

