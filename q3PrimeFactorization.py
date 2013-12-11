# find the largest prime factor of 600851475143



# attempt using Fermat's factorization method, as outlined at
#http://en.wikipedia.org/wiki/Fermat%27s_factorization_method
import math

# this finds ONE of the (not-necessarily-prime) factors of N. we need it to find Any/ALL
# also we need to test for prime, hence the method below
def factor(N):
    a = math.ceil(math.sqrt(N))
    b = float(a*a - N)
    while not(float(math.sqrt(b))-int(math.sqrt(b))==0):
        a=a+1
        b=a*a-N
    return max(a+math.sqrt(b),a-math.sqrt(b), N/(a+math.sqrt(b)), N/(a-math.sqrt(b)))

# this doesn't work
def isPrime(N):
    primeCandidate=factor(N)
    return primeCandidate == factor(primeCandidate) or factor(primeCandidate)==1

number= 600851475143
print factor(number)
