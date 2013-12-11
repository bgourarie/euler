# project euler

# problem 1
sum = 0
for i in range(0,1000):
    if i%3 ==0 or i%5 ==0:
        sum+= i

print "sum of multiples of 3 or 5 lower than 1000 = " +str(sum)


# problem 2.. sum of even elements of fibonacci sequence starting 1,2,3,5,8...
# up to the element which exceeds 4 million
def fib(int1, int2):
    return int1+int2

fibSum= 2 # 2 is even, 1 and 3 are not
currVal=fib(1,2)
pre1= 1 #curr= fib(pre1,pre2)
pre2= 2

while currVal<4000000:
    pre1= pre2
    pre2= currVal
    currVal=fib(pre1,pre2)
    if currVal%2==0:       
        fibSum+=currVal

print "Sum of even Fibonacci elements <4 million is " + str(fibSum)


# problem 3. Prime factors of 600851475143
# this could be a very complex problem if desired. However, I'll choose simplicity over efficiency
# since this is a quick problem.
'''
number= 600851475143

for i in range(0,number/5):
    if i%2==1: # can ignore even numbers
        if number%i==0:
            print i
'''

#problem 4: palindromic numbers made from 3 digit numbers

def isPalindrome(test)
    asString= str(test)
    

