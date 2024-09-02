n,x = list(map(int,input().split()))

array = list(map(int,input().split()))

bounces = 1
distance = 0

for i in range(n):
    distance += array[i]
    if distance <= x:
        bounces += 1

print(bounces)