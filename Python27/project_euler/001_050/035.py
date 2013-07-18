#Taking 9.6 seconds
import math
def is_prime(num):
    '''Checks whether a number is prime or not'''
    #REQUIRES MATH MODULE
    if num == 2:
        return True
    elif num % 2 == 0 or num < 2:
        return False
    
    temp = int(round(math.sqrt(num))) + 1
    
    for i in xrange(3,temp,2):
        if num % i == 0:
            return False
    else:
        return True

def circular_shift(num, shift):
    '''Returns a number circularly shifted '''
    num = str(num)
    length = len(num)
    shift %= length
    return int(num[length - shift:] + num [:length - shift])

def is_circular_prime(num, length):
    for check in xrange(length):
        if not is_prime(circular_shift(num, check + 1)):
            return False
    else:
        return True

def p():
    circulars = 0
    for i in xrange(1,1000000):
        if  is_circular_prime(i, len(str(i))):
            circulars += 1
            
    print circulars

import time

s = time.time()
p()
print (time.time() - s)
