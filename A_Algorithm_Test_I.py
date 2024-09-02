from collections import Counter
import math
n = int(input())
array = list(map(int,input().split()))
cnt = len(Counter(array))
print(math.factorial(cnt))