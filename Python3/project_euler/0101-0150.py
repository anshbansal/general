__author__ = 'Aseem'

import numbers_ab
import primes
from itertools import count


def prob_112():
    #TODO May be Optimized - 7.576 sec
    bouncy = 0
    for i in count(2):
        if numbers_ab.is_bouncy_num(i):
            bouncy += 1

        if bouncy/i == 0.99:
            return i


def prob_124():
    #TODO May be Optimized - 1.952 sec
    listt_tuples = [(primes.product_of_prime_factors(i), i)
                    for i in range(1, 100001)]
    return sorted(listt_tuples)[-1][1]


if __name__ == "__main__":
    import sys
    import time

    RULER = "====="
    LIST_FUNC = [i for i in dir(sys.modules[__name__])
                 if i.startswith('prob_') is True]
    for fname in LIST_FUNC:
        timm_t = time.time()
        print(RULER + RULER + fname + RULER + RULER + str(locals()[fname]()))
        temp_time = time.time() - timm_t
        if temp_time > 1.0:
            print("TIME " + RULER +  str(temp_time))