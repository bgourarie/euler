'''
2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest positive number that is
evenly divisible by all of the numbers from 1 to 20
'''
'''
#we'll need to make a list of the numbers in the range 1 to x
# which are not mutliples of other numbers in the range...
def candidates(y):
    seen=[x in range(y)]
    added=[]
    for i in range(y):
        for d in range(i,y):
            if
    '''
mults=[16,18,20,12,14,11,13,15,17,19]
        
def product(listX):
    prod=1
    for x in listX:
        prod*=x
    return prod
candidate= product(mults)
success=True

    for i in range(1,20):
        if  (candidate % i) != 0:
            success=False

    if success:
        print candidate
