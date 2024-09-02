'''
    NENSNE
    ans is going to be where the left and the right are going to be equal
    as long it is one we are good 
    separate the x and y axis handle them by a single function

'''

dic = {"N" : 1, "E" : 1,"S" : -1, "W" : -1}
xD = ["E","W"]
yD = ["N","S"]

def traverse(lis,s):
       
    left = 0
    total = 0

    for i in range(len(s)):
        if s[i] in lis:
            total += dic[s[i]]

    print(total,'total')
    runningSum = 0
    ans = -1
    while left < len(lis) - 1:
        if s[i] in lis:
            runningSum += dic[s[left]]

        if runningSum == total // 2:
            ans = left
        left += 1

    return total,ans

t = int(input())
for _ in range(t):
    n = int(input())
    s = input()

    xTotal,xAns = traverse(xD,s)
    yTotal,yAns = traverse(yD,s)

    print(xAns,yAns)
    ans = [None] * n

    for i in range(n):
        if s[i] in xD:
            if xAns < i:
                ans[i] = 'R'
            else:
                ans[i] = "H"
        else:
            if yAns < i:
                ans[i] = "R"
            else:
                ans[i] = "H"

    if xTotal % 2 != 0 or yTotal % 2 != 0 :
        print(-1)
    else:
        print(*ans)
        






