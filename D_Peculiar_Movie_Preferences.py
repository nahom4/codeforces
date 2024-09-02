
t = int(input())
for _ in range(t):
    n = int(input())
    ls = []
 
    for _ in range(n):
        ls.append(input())
 
 
    #first check single character
    valid = False
    for char in ls:
        if len(char) == 1:
            valid = True
            
    if valid:
        print('YES')
        continue
 
    #check for self pairs
    mp = set()
 
    for char in ls[::-1]:
        if char[::-1] in mp: #2 by 3 front and bac
            valid = True
            break
        if len(char) == 3 and char[:2][::-1] in mp:
            valid = True
            break
 
        mp.add(char)
 
    mp = set()
 
    for char in ls:
        if char[:: -1] in mp: #2 by 3 front and bac
            valid = True
            break
        if len(char) == 3 and char[::-1][:2] in mp:
            valid = True
            break
        
        mp.add(char)
 
    for char in ls:
        if char[0] == char[-1]:
            valid = True
 
    if valid:
        print('YES')
        continue
 
    print('NO')
 