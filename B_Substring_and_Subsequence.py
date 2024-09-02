t = int(input())

for _ in range(t):
    a = input()
    b = input()

    #actually let me just brute force it.
    mx = 0
    for i in range(len(b)):

        ct = 0
        bLeft = i
        aLeft = 0
        while aLeft < len(a):
            if bLeft < len(b) and b[bLeft] == a[aLeft]:
                bLeft += 1

            aLeft += 1

        mx = max(mx,bLeft - i)

    
    print(len(a) + len(b) - mx)



