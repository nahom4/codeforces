from collections import defaultdict
t = int(input())
for _ in range(t):
    n = int(input())
    array = list(map(int,input().split()))


    ct = 0
    front = defaultdict(int)
    middle = defaultdict(int)
    back = defaultdict(int)
    equal = defaultdict(int)
    left = 0
    while left + 2 < n:
        lis = array[left : left + 3]
        ft = tuple(lis[1 : ])
        md = tuple(lis[ : 1] + lis[2 :])
        bk = tuple(lis[:2])
        whole = tuple(lis)
        # print(lis)
  
        ct += front[ft]

        ct += middle[md]
        ct += back[bk]
        ct -= 3 * equal[whole]

        front[ft] += 1
        middle[md] += 1
        back[bk] += 1
        equal[whole] += 1

        left += 1

    print(ct)
        
