import sys
from collections import Counter
import random
input = lambda : sys.stdin.readline().strip()

x = random.randint(1, 10**5)
t = int(input())
for _ in range(t):
    n,m,k = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))

    bCount = Counter()
    for num in b:
        bCount[num ^ x] += 1
    aCount = Counter()
    count = 0
    left = 0
    ans = 0

    for i in range(n):
        aCount[a[i]^ x] += 1
        if aCount[a[i] ^ x] <= bCount[a[i]^ x]:
            count += 1

        if i >= m:
            aCount[a[left]^ x] -= 1
            if aCount[a[left]^ x] < bCount[a[left]^ x]:
                count -= 1
            left += 1

        if i - left + 1 == m:
            if count >= k:
                ans += 1

    print(ans)

        






