#Can be optimized. Took 145 seconds
import math, time

def num_distinct_prime_factors(num):
    '''Returns the prime factors of a number'''
    ans = 0

    if num % 2 == 0:
        ans += 1
        num /= 2
        while num % 2 == 0:
            num /= 2

    i = 3
    while i <= num:
        if num % i == 0:
            ans += 1
            num /= i
            while num % i == 0:
                num /= i

        i += 2

    return ans

def p():
    a = [0, 0, 0, 0]

    i = 1
    while True:
        a[:3] = a[1:4]
        a[3] = num_distinct_prime_factors(i)
        
        if a == [4, 4, 4, 4]:
            break

        i += 1

    print "Ans", i - 3

s = time.time()
p()
print (time.time() - s)
