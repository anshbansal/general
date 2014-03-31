__author__ = 'Aseem'

import numbers_ab
import primes
from itertools import count


def prob_112():
    #TODO May be Optimized - 7 sec
    bouncy = 0
    for i in count(2):
        if numbers_ab.is_bouncy_num(i):
            bouncy += 1

        if bouncy/i == 0.99:
            return i


def prob_124():
    #TODO May be Optimized - 1.672 sec
    return sorted(
        [(primes.product_of_prime_factors(i), i)
         for i in range(1, 100001)])[9999][1]


if __name__ == "__main__":
    import sys
    import time

    RULER = "====="
    LIST_FUNC = [i for i in dir(sys.modules[__name__])
                 if i.startswith('prob_') is True]
    for fname in LIST_FUNC:
        timm_t = time.time()
        print(RULER + RULER + fname + RULER + RULER)
        print(locals()[fname]())
        print("TIME " + RULER +  str(time.time() - timm_t))