__author__ = 'Aseem'

import common
import numbers_ab
import primes
from itertools import count


def prob_112():
    bouncy = 0
    for i in count(2):
        if numbers_ab.is_bouncy_num(i):
            bouncy += 1

        if bouncy/i == 0.99:
            return i


def prob_124():
    #TODO Bug present
    listt_tuples = [(primes.product_of_prime_factors(i), i)
                    for i in range(1, 100001)]
    return sorted(listt_tuples)[-1][1]

if __name__ == "__main__":
    common.run_all(__name__)