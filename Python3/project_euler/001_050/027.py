__author__ = 'Aseem'

from itertools import count
import primes
import time


def first_non_prime(x, y):
    for n in count(0):
        if not primes.is_prime(n * n + x * n + y):
            return n


def prob_027():
    b_list = primes.primes_list(1000)
    max_primes, ans = 0, 0
    for a in range(-999, 1000):
        for b in b_list:
            number_primes = first_non_prime(a, b)
            if number_primes > max_primes:
                max_primes, ans = number_primes, a*b
    return ans


s = time.time()
print(prob_027())
print(time.time() - s)
