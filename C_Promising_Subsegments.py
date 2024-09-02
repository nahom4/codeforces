import sys
from collections import Counter
input = lambda : sys.stdin.readline.strip()

t = int(input())
for _ in range(t):
    n,m,k = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))

    bCount = Counter(b)
    aCount = Counter()
    count = 0
    left = 0
    ans = 0

    for i in range(n):
        aCount[a[i]] += 1
        if aCount[a[i]] <= bCount[a[i]]:
            count += 1

        if i >= m:
            aCount[a[left]] -= 1
            if aCount[a[left]] < bCount[a[left]]:
                count -= 1
            left += 1

        if i - left + 1 == m:
            if count >= k:
                ans += 1

    print(ans)

        






