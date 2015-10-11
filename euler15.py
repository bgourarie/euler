import math;

#idea
# let's count how many cells are left or up from us.

def moveLeft(xy):
    if xy[0] > 0 :
        return 1;
    else:
        return 0;

def moveUp(xy):
    if xy[1] > 0:
        return 1;
    else :
        return 0;

def countBack(xy):
    count = 0;
    if moveLeft(xy) == 0 :
        if moveUp(xy) == 0:
            return count + 1;
        else : # we move up one more...
            return countBack([xy[0],xy[1]-1]);
    else: #moveLeft == 1
        if moveUp(xy) == 0 :
            return countBack([xy[0]-1,xy[1]]);
        else:
            count+= countBack([xy[0]-1,xy[1]])
            count+= countBack([xy[0],xy[1]-1]);

    return count;

for i in range(2,10):
    print countBack([i,i]);

# this is wayyy too inefficent to use for 20x20 grid.

# however, there's a pattern, its not actaully the n-th line of pascal's triangle, but the 2n-th (?)
def pascal(n):
    line = [1];
    for k in range(n):
        line.append(line[k]* (n-k)/(k+1))
    return line

for i in range(41):
    print pascal(i);


#but thats still wrong
    #what abut catalan numbers

def catalan(n):
    prod = 1
    for k in range(2,n+1):
        prod = prod * (n+k)/k;
    return prod;

print catalan(20)
print countBack([20,20]);
