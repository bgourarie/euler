# -*- coding: utf-8 -*-

'''
The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)2 = 552 = 3025

Hence the difference between the sum of the squares of the
first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first
one hundred natural numbers and the square of the sum.
'''

def sum_of_squares(list_x):
    sq_list= [x*x for x in list_x]
    return sum(sq_list)
def square_sum(list_x):
    return sum(list_x)*sum(list_x)

s1= sum_of_squares(range(1,101))
s2=  square_sum(range(1,101))
print abs(s1-s2)
