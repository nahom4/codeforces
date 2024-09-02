s = list(input())
n = len(s)
prefixArray = [0] * (len(s) + 1)
s.append("$")

for i in range(n):
    prefixArray[i + 1] += prefixArray[i ]
    if s[i] == s[i + 1]:
        prefixArray[i + 1] += 1

q = int(input())
for _ in range(q):
    left,right = map(int,input().split())
    print(prefixArray[right - 1] - prefixArray[left - 1])
