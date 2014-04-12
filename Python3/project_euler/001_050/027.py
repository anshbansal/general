__author__ = 'Aseem'

from itertools import count
import primes
import time


def num_primes(a, b):
    for n in count(0):
        if not primes.is_prime(n * n + a * n + b):
            break
    return n


def prob_027():
    #TODO Maybe optimized - 1.734 sec
    b_list = primes.primes_list(1000)
    max_primes = (0, 0)
    for a in range(-999, 1000):
        for b in b_list:
            number_primes = num_primes(a, b)
            if number_primes > max_primes[0]:
                max_primes = (number_primes, a*b)

    return max_primes[1]


s = time.time()
print(prob_027())
print(time.time() - s)
