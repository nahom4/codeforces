t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    lis = sorted(list(set(s)))
    newS = ""

    dic = {}
    left,right = 0,len(lis) - 1

    while left <= right:
        dic[lis[left]] = lis[right]
        dic[lis[right]] = lis[left]
        left += 1
        right -= 1
    for i in range(len(s)):
        newS += dic[s[i]]

    print(newS)
