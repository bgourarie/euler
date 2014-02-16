def sieve(n):
    s = [True] * n
    s[0] = s[1] = False # not prime..
    for (i, isprime) in enumerate(s):
        if isprime:
            yield i
            for j in xrange(i*i,n,i):
                s[j]=False

'''    

print n
primes_list=list(sieve(n))
primes_found=len(primes_list)
print primes_found
while(primes_found<10,001):
    n+=primes_list[primes_found-1]
    print n
    primes_list=list(sieve(n))
    primes_found=len(primes_list)

print primes_list[10001]
'''

def sundaram(max_n):
    numbers= range(3,max_n+1,2)
    half= (max_n)//2
    initial= 4

    for step in xrange(3,max_n+1,2):
        for i in xrange(initial, half, step):
            numbers[i-1]=0
        initial+= 2*(step+1)

        if initial>half:
            return [2] +filter(None, numbers)

#print sundaram(100001)
n=100001
primes_list=sundaram(n)
primes_found=len(primes_list)
print primes_found
while(primes_found<10001):
    n+=primes_list[primes_found-1]
    #print n
    primes_list=sundaram(n)
    primes_found=len(primes_list)
    print primes_found
print primes_list[10000]
print primes_list[10001]

                  
                  
