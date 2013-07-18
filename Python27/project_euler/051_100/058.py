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


primes = 0
non_primes = 1

ratio = 1.0

n = 1
while ratio >= 0.1:
    n += 2
    temp = n * n
    temp2 = n - 1
    
    nums = [temp, temp - temp2, temp - 2*temp2, temp - 3*temp2]

    for num in nums:
        if is_prime(num):
            primes += 1
        else:
            non_primes += 1

    ratio = primes/(float(non_primes) + primes)

print "n = ",n
