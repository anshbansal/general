import math
from itertools import permutations

def is_prime(num):
    '''Checks whether a number is prime or not'''
    if num == 2:
        return True
    elif num < 2 or num % 2 == 0:
        return False
    
    temp = int(round(math.sqrt(num))) + 1
    for i in xrange(3,temp,2):
        if num % i:
            pass
        else:
            return False
    else:
        return True

largest = 0
for j in xrange(1,9):
    for i in permutations(xrange(1,j + 1)):
        temp = 0
        for c in i:
            temp *= 10
            temp += c
        if temp > largest and is_prime(temp):
            largest =  temp
    
print largest
