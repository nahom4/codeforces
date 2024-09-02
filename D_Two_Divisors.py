n = int(input())
array = list(map(int,input().split()))
import math

def SieveOfEratosthenes(n):
    # Initialize a list to mark non-primes
    prime = [True for i in range(n + 1)]
    p = 2
    
    # Only iterate while p * p <= n (which is the square root of n)
    while (p * p <= n):
        # If prime[p] is still True, then it's a prime
        if prime[p]:
            # Mark multiples of p as non-prime
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    
    # Collect primes up to sqrt(n)
    target = []
    for p in range(2, n + 1):
        if prime[p]:
            target.append(p)
    
    return target

target = SieveOfEratosthenes(math.ceil(math.sqrt(max(array))))


first = [-1] * n
second = [-1] * n
for i,num in enumerate(array):
	for prime in target:
		if not (num % prime): #6 2
			while num > 1 and not (num % prime):
				num //= prime

			if num > 1:
				first[i] = prime
				second[i] = num

			break

print(*first)
print(*second)   