#https://www.geeksforgeeks.org/sieve-of-eratosthenes/,https://www.geeksforgeeks.org/python-program-for-find-largest-prime-factor-of-a-number/
import math
def SieveOfEratosthenes(n, k):
    p = 2
    while (p * p <= n and p<=k):
         
        if (prime[p] == True):
             
            for i in range(p * 2, k+1, p):
                prime[i] = False
        p += 1


def maxPrimeFactors (n):
     
    maxPrime = -1
     
    while n % 2 == 0:
        maxPrime = 2
        n >>= 1     # equivalent to n /= 2
         
    # n must be odd at this point, 
    # thus skip the even numbers and 
    # iterate only for odd integers
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            maxPrime = i
            n = n / i
     
    # This condition is to handle the 
    # case when n is a prime number 
    # greater than 2
    if n > 2:
        maxPrime = n
     
    return int(maxPrime)

n=int(raw_input())
k=maxPrimeFactors(n)
prime = [True for i in range(k+1)]
SieveOfEratosthenes(n, k)
max=k

i=2
pr=[]
while(i<=max):
	if(prime[i]==True):
		if(n%i == 0):
			pr.append(i)
	i+=1

res=n
for x in pr:
	res=(res*(x-1))/x

print res,
