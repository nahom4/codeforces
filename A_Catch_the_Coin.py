n = int(input())
for _ in range(n):
    x,y = map(int,input().split())
    y -= abs(x)
    # print(y)
    if y >= -1 * abs(x) - 1:
        print('YES')
    else:
        print('NO')