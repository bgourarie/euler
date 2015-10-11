import math

def triangleNum(n):
    return (n*(n+1))/2;

print triangleNum(7);

# initially wrote my own  but it was too slow, got this from:
# http://stackoverflow.com/questions/6800193/what-is-the-most-efficient-way-of-finding-all-the-factors-of-a-number-in-python
def countDivisors(n):
    return set(reduce(list.__add__,([i,n//i] for i in range(1,int(math.sqrt(n))+1) if n % i == 0)));

print countDivisors(triangleNum(7));


x = 500
#(10000 is divisible by 500, so the bare minimum of logic
#suggests that it could have >500 factors.
# obviously, it has far fewer, but its a starting point.
l=[1]
while (len(l)-1)<500:
    x=x + 1;
    l=countDivisors(triangleNum(x));


# got stuck here for awhile, misread the problem and was returning x rather than the triangleNumber.
print triangleNum(x)
