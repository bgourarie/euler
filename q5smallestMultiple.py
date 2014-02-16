'''
2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest positive number that is
evenly divisible by all of the numbers from 1 to 20
'''
''' this will use LeastCommon Multiple.. so we'll need to do some prime factoring..
'''
def getPrimeFactors(n):
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
    
def countOccurences(arr):
    distinct=[]
    counts=[]
    k=0
    for i in range(len(arr)):
        x=arr[i]
        if not x in distinct:
            distinct.append(x)
            k+=1
            counts.append(0)
            for y in arr:
                if y==x:
                    counts[k-1]+=1
    results=[]
    for i in range(len(counts)):
        results.append([distinct[i],counts[i],i])
    return results

def mergePrimeFactors(arr):
    occurences=[]
    for m in arr:
        factors=getPrimeFactors(m)
        n_occur=countOccurences(factors)
        occurences.append(n_occur);
    factor=[]
    count=[]
    
    for y in occurences:
        # y = a list of factors of a given number
        for x in y:
            # x= [prime, power, index]
            if  x[0] in factor:
                # go through each one, if we've seen it, we check how many times,
                #and save the largest..
                for i in range(len(factor)):
                    if x[0]==factor[i]:
                        if x[1]>count[i]:
                            count[i]=x[1]            
            else:
                factor.append(x[0])
                count.append(x[1])
    toast=[]
    for i in range(len(count)):
        toast.append([factor[i],count[i]])
    return toast

def product(primePowers):
    prod=1
    for i in primePowers:
        for p in range(i[1]):
            prod*= i[0]
    return prod
print mergePrimeFactors([36,72,90])#,52,156,23,423,12904])


print product(mergePrimeFactors(range(30)))
