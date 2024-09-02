from collections import Counter
t = int(input())

for _ in range(t):
    n,m = map(int,input().split())
    s = input()

    ct = Counter(s)
    letters = ["A","B","C","D","E","F","G"]
    miss = 0
    for _ in range(m):
        for char in letters:
            if ct[char] == 0:
                miss += 1

            else:
                ct[char] -= 1

    print(miss)


