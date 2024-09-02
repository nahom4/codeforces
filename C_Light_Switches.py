t = int(input())
for _ in range(t):
    n, k = map(int, input().split()) 
    array = list(map(int, input().split()))
    array.sort()
    
    fastest, slowest = array[0], array[0]
    valid = True

    for i in range(1, n): #64 40 50 68 70 10
                
        #10 40 50 64 65 68 70  k = 5
        time = array[i] 
        diff = time - fastest

        # Calculate the required adjustment
        div = diff // (2 * k)
        rm = diff % (2 * k) 
    
        # Determine the total time increment needed 1 10000000000 
        if rm > k:
            summ = (div + 1) * (2 * k)
        else:
            summ = div * (2 * k)

        fastest += summ
        slowest += summ

        # Adjust fastest and slowest
        fastest = max(time, fastest)
        slowest = min(time, slowest)
        # print(fastest,slowest)
        # If the difference exceeds k, it's invalid
        if fastest - slowest >= k:
            valid = False
            break

    if valid:
        print(fastest)
    else:
        print(-1)
