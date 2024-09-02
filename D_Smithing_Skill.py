n,m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = list(map(int,input().split()))

total = sum(c)

pair = zip(a,b)
pair = [(tp[0] - tp[1],i) for i,tp in enumerate(pair)]
pair.sort()
print(pair)
ans = 0

for index,diff in pair:
    #let me calculate how much I can get here
    #I hate math

    '''
        10 20 20
        10 20 20
        0 0 0
        1 10
        u
        2 10
        3 30
        4 40
        5 50
        
        8
        4 turns 40
        9 10 19 20 = 58
        It's not impelementations problem
 
    '''
    if a[index] < total:

        