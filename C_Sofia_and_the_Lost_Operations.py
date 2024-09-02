from collections import Counter
t = int(input())

'''
4
3 1 7 8
2 2 7 10
5
10 3 2 2 1
'''
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))

    m = int(input())
    d = list(map(int,input().split()))

    cdT = Counter(d)
    need = Counter()
    for i in range(n):
            if a[i] != b[i]:
                need[b[i]] += 1


    valid = True
    stock = Counter()
    for key in b:
        if cdT[key]:
            stock[key] = cdT[key]


    for key in need:
        if need[key] > cdT[key]:
            valid = False

    # print(valid)
    for i in range(m): # 2 3
      
        if d[i] in need:
            stock[d[i]] -= 1
            if stock[d[i]] == 0:
                stock.pop(d[i])
        else:
            if not stock:
                valid = False
    
    if valid:
        print('YES')
    
    else:
        print("NO")