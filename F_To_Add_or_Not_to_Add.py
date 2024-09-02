n,k = map(int,input().split())
array = list(map(int,input().split()))

array.sort()
prefix = [0] * n
suffix = [0] * n
for i in range(1,n):
    prefix[i] = (array[i] - array[i - 1]) * i + prefix[i - 1]

for i in range(n - 2,-1,-1):
    suffix[i] = (array[i + 1] - array[i]) * (n - i - 1) + suffix[i + 1]
print(array)
print(prefix)
print(suffix)