#Took 21 seconds
import math, time
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

def p():
    total = 0
    divisors = [2, 3, 5, 7, 11, 13, 17]
    for i in permutations(xrange(10)):
        if i[0] == 0:
            continue
        
        temp = 0
        for c in i:
            temp *= 10
            temp += c

        temp = str(temp)        
        for j in xrange(7, 0, -1):
            if int(temp[j:j + 3]) % divisors[j - 1]:
                break
        else:
            total += int(temp)
        
    print total

s = time.time()
p()
print (time.time() - s)
