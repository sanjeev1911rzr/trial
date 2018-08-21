import math
def SieveOfEratosthenes(n):
    p = 2
    while (p * p <= n):
         
        if (prime[p] == True):
             
            for i in range(p * 2, n+1, p):
                prime[i] = False
        p += 1

n=int(raw_input())
prime = [True for i in range(n+1)]
SieveOfEratosthenes(n)

res=[True for i in range(n+1)]

i=2

while(i*2<n):
    if(prime[i]==True):
        if(n%i==0):
            k=1
            while(i*k<n):
                res[i*k]=False
                k+=1
    i+=1


i=1
count=0
while(i<n):
    if(res[i]==True):
        count+=1
        print i,
    i+=1

print(count)


