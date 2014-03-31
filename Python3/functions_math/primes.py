__author__ = 'Aseem'

import itertools
import math
import numbers_ab
import operator


def is_prime(num):
    """Checks whether a number is prime or not"""
    if num == 2:
        return True
    if num % 2 == 0 or num < 2:
        return False

    temp = int(math.sqrt(num)) + 1
    for i in range(3, temp, 2):
        if num % i == 0:
            return False
    return True


def largest_prime_factor(num):
    """Returns the largest prime factor for num > 0"""
    ans = 0
    sqrt_num = int(math.sqrt(num)) + 1
    for i in itertools.chain([2], range(3, sqrt_num, 2)):
        while not (num % i):
            ans = i
            num //= i
    return ans if num == 1 else num


def nth_prime(num):
    """"Returns the Nth prime"""
    pos = num
    fun = primes_list(pos)
    while len(fun) < num:
        pos *= 2
        fun = primes_list(pos)
    return fun[num - 1]


def primes_list(num):
    """Returns list of prime numbers"""
    if num < 2:
        return []

    isprime = [num for num in range(3, num + 1, 2)]
    temp2 = int(math.sqrt(num)) + 1
    for i in range(3, temp2, 2):
        if isprime[(i - 3) // 2]:
            j = 3
            temp = j * i
            while temp <= num:
                isprime[(temp - 3) // 2] = 0
                j += 2
                temp = j * i

    return [2] + [x for x in isprime if x]


def _prime_factors_base(num, seed, operate, update_value=None):
    ans = seed
    sqrt_num = math.floor(math.sqrt(num)) + 1
    for i in itertools.chain([2], range(3, sqrt_num, 2)):
        if num % i:
            continue

        while num % i == 0:
            num //= i

        ans = operate(ans, i if update_value is None else update_value)
    return num, ans


def num_distinct_prime_factors(num):
    """returns the num of distinct prime factors for num > 0"""
    num, ans = _prime_factors_base(num, 0, operator.add, 1)
    if num == 1:
        return ans
    else:
        return ans + 1


def product_of_prime_factors(num):
    num, ans = _prime_factors_base(num, 1, operator.mul)
    return ans * num


def is_circular_prime(num, length):
    for i in str(num):
        if not (int(i) % 2):
            return False
    for check in range(length):
        if not is_prime(numbers_ab.circular_shift(num, check + 1)):
            return False
    return True