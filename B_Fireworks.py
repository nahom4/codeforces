t = int(input())
for _ in range(t):
    a,b,m = map(int,input().split())

    print(m // a + m // b + 2)
