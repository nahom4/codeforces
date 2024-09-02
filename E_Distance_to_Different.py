n,k = map(int,input().split())
Mod = 998244353
def dp(n,k):

    if n <= 0 and k > 0:
        return float("-inf")
    
    if k <= 0 and n > 0:
        return float("-inf")

    if n <= 0 and K <= 0:
        return 1

    '''
        6 2 diff = 4
                
        1 2 3 4

    '''
    prod = float("-inf")
    for diff in range(k):
        prod = max(prod,dp(n - diff,k - diff))

    return prod


print(dp(n,k) % Mod)