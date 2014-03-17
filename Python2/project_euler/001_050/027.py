import math, time

def primes_list(num):
    ''' Returns list of prime numbers'''
    ''' erat2() from the file "Generating List of prime numbers" '''
    #REQUIRES MATH MODULE
    if num < 2:
        return []

    isprime = [num for num in xrange(3,num + 1,2)]
    #temp2's expression placed in xrange function => performance-loss
    temp2 = int(math.sqrt(num)) + 1
    for i in xrange(3, temp2 ,2):
        if isprime[(i-3)/2]:
            j = 3
            temp = j * i
            while temp <= num:
                isprime[(temp-3)/2] = 0
                j += 2
                temp = j * i
    
    return [2] + filter(lambda x: x, isprime)

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

def num_primes(a,b):
    total = 0
    n = 0
    while True:
        if is_prime(n * n + a * n + b):
            total += 1
            n += 1
        else:
            return total

def p():
    b_list = primes_list(1000)
    max_primes = 0
    max_primes_product = 0
    for a in xrange(-999, 1000):
        for b in b_list:
            primes = num_primes(a,b)
            if primes > max_primes:
                max_primes = primes
                max_primes_product = a * b

    print max_primes_product
            
            
s = time.time()
p()
print (time.time() - s)
