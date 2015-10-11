#It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
#sequence defined by
# n/2 if n is even
# 3n+1 if n is odd
#Which starting number, under one million, produces the longest chain?


#brute force!

def collatzLength(n):
    curr = n;
    length = 1;
    while curr != 1:
        if curr % 2 == 0 :
            curr = curr/2
        else:
            curr = 3*curr +1
        length += 1
    return length


print collatzLength(13)
i=1
maxLength = 10
start = 13
while i < 1000000 :
    x = collatzLength(i)
    if x > maxLength:
        maxLength = x
        start = i
    i+=1;

print start
