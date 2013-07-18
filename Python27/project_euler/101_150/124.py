#Can be optimized. Took 90 seconds
import time
s = time.time()
def product_of_prime_factors(num):
    '''Returns the prime factors of a number'''
    ans = 1

    if num % 2 == 0:
        ans *= 2
        num /= 2
        while num % 2 == 0:
            num /= 2

    i = 3
    while i <= num:
        if num % i == 0:
            ans *= i
            num /= i
            while num % i == 0:
                num /= i

        i += 2

    return ans

p = product_of_prime_factors

funct = []
for i in xrange(1, 100001):    
    funct.append((p(i), i))
funct.sort()
print "\n\n", funct[9999]
print (time.time() - s)
