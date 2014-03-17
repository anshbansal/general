import math, time
def is_prime(num):
    '''Checks whether a number is prime or not'''
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

def primes_list(num, isprime = [2]):
    '''Works nicely if called again for the same or lower number'''
    if num > len(isprime) + 2:
        first_new = len(isprime) + 2
    
        isprime += [num for num in xrange(first_new ,num + 1)]
        for i in xrange(2,num + 1):
            if isprime[i-2]:
                if i <= first_new:
                    j = first_new//i + 1
                else:
                    j = 2
                temp = j * i
                while temp <= num:
                    isprime[temp-2] = 0
                    j += 1
                    temp = j * i
    
    return filter(lambda x: x, isprime[:num - 1])
###
def is_prime2(num):
    '''Checks whether a number is prime or not      '''
    #REQUIRES primes_list() function and math module
    primes = primes_list(int(round(math.sqrt(num))) + 1)
    for i in primes:
        if num > i:
            if num % i == 0:
                return False
        else:
            break
    return True
