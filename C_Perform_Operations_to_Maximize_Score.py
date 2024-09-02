t = int(input())

for _ in range(t):
    n,k = map(int,input().split())
    array = list(map(int,input().split()))
    array = [(val,i) for i,val in enumerate(array)]
    b = list(map(int,input().split()))

    array.sort()
    valid = set()
    for i in range(n):
        if b[array[i][1]]:
            valid.add(i)

    array = list(map( lambda x : x[0], array))
    if n == 1:
        print(b[0] * k + array[0])
        continue

    md = n // 2 # the right most md
    even = 0
    for i in range(n): 
        #1 1 2 5  #k = 4
        #1 1 0 0
        curr = 0
        if i < md: #md is md
            if i in valid or md in valid:
                curr += array[i] + k + array[md]
        else: # md = md - 1
            if i in valid or (md - 1) in valid:
                   curr += array[i] + k + array[md - 1]

        print(curr)
        even = max(even,curr)

    if not n % 2:
        print(even)
        continue

    odd = 0
    # 1 3 4 5 6 three cases in this one right
    for i in range(n): # 3 3 3 md = 1 # 
        curr = array[i] 
        if i > md: #md and md - 1 are mids
            curr += (array[md] + array[md - 1]) // 2
            if i in valid:
                curr += k
            elif md in valid or (md - 1) in valid:
                curr += k // 2

        elif i < md: #md and md + 1 are mids
            curr += (array[md] + array[md + 1]) // 2
            if i in valid:
                curr +=  k  
            elif md in valid or (md + 1) in valid:
                curr += k // 2
        else:#md - 1 and md + 1 are mids
            curr += (array[md - 1] + array[md + 1]) // 2
            if i in valid:
                curr += k
            elif (md - 1) in valid or (md + 1) in valid:
                curr += k // 2

        odd = max(odd,curr)

    print(odd)




