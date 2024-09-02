t = int(input())

for _ in range(t):
    n = int(input())
    array = list(map(int,input().split()))

    stack = []
    power = 0
    
    for i in range(n):

        if array[i] != 0:
            continue

        mx = max(array[:i + 1])
        idx = array.index(mx)
        array[idx] = 0
        power += mx

    print(power)

        