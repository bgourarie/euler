# -*- coding: cp1252 -*-
'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

def isPalindrome(n):
    # we count the characters in n, push half of them on a stack. (discard middle if odd)
    # we go through the second half (after discard if odd)
    # and verify that each char matches what we pop.
    charStack= []
    stringN=str(n)
    length= len(stringN)
    
    for i in range( length/2):
        charStack.append(stringN[i])
    if length%2 != 0 :
        mid = length/2+1
    else: mid= length/2;
    for i in range(mid, length):
        if not charStack.pop()== stringN[i]:
            return False
    return True
''' testing...

print isPalindrome(123456)==False
print isPalindrome(123456654321)==True
print isPalindrome(123454321)==True
print isPalindrome(12345432)==False
    '''

# now we just start checking products...
largest=1
lowerBound=999
while largest==1:
    for x in range(lowerBound,1000):
        for y in range(lowerBound, 1000):
            curr= x*y
            #print curr
            if isPalindrome(curr):
                if curr > largest:
                    largest=curr
    lowerBound-=100
print largest
