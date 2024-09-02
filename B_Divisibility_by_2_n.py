t = int(input())

def power_of_2(num):
    if num == 0:
        return 1

    if num % 2 != 0: 
        return 0

    return 1 + power_of_2(num // 2)

for _ in range(t):
    n = int(input())
    array = list(map(int, input().split())) 

    total = 0
    power_of_index = []
    for i in range(n):
        total += power_of_2(array[i])
        power_of_index.append(power_of_2(i + 1))

    power_of_index.sort(reverse=True)
    i = 0
    while total < n and i < n:
        total += power_of_index[i]
        i += 1

    if total < n:
        print(-1)
    else:
        print(i)




