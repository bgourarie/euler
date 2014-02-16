# find the largest prime factor of 600851475143



#attempted using sieve of eratosthenes and some basic factorization.
# but of course, since the sieve has massive overhead, that failed. instead we use
# some naive factorization method, and only add them to a list if they are not
#divisible by any prior factors..
import math

def primes(n):
    primeFac=[]
    d=2
    while d*d<=n:
        while (n % d)==0:
            primeFac.append(d)
            n /= d
        d += 1
    if n >1:
        primeFac.append(n)
    return primeFac

def factor(N):
    #ourSieve=sieve(N)
    maxFactor=0
    # find factors:
    divisors = [ d for d in range(2,N//2+1) if N % d == 0 ]
    for d in divisors:
        if d>maxFactor and all (d %od != 0 for od in divisors if od != d):
            maxFactor=d;
            
    return maxFactor

def isPrime(d):
    return 
def isPrime(x, sieve):    
    return sieve[x]; #return if we know it to be prime, or not.

def sieve(n):
    N=n
    sieve=[True]*N;
    for i in range(2,N):
         if(sieve[i]):
            j=i;
            while (j*i)<N:
                sieve[j*i]=False;
                j+=1;
    return sieve

number= 600851475143
print sieve(7)
print primes(number)
#print isPrime(number)
#print factor(number)

