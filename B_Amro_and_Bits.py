t = int(input())
for _ in range(t):
    n = int(input())

    if n == 1:
        print(3)

    elif n % 2 != 0:
        print(1)

    else:
        mask = 1
        while (mask & n) == 0:
            mask = mask << 1

        if mask == n:
            print(mask + 1)
        else:
            print(mask)
    