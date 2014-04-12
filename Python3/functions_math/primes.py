__author__ = 'Aseem'

import itertools
import math
import numbers_ab


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


def primes_list_mem(num, isprime=[3]):
    """Returns list of Prime numbers

    Advantage:
    Half memory usage
    Takes 1/10th time if called in the same run for same or lower number
    Improvement in speed if it has been called before

    Disadvantage:
    Has storage between function calls - Takes up a lot of memory space"""
    if num < 2:
        return []

    if num > 2 * len(isprime) + 2:
        def mapping(x):
            return (x - 3)//2

        first_new = 2 * len(isprime) + 3
        isprime += [num for num in range(first_new, num + 1, 2)]

        temp2 = int(math.sqrt(num)) + 1
        for i in range(3, first_new, 2):
            if isprime[mapping(i)]:
                j = first_new//i
                if j == 1:
                    j = 3
                elif j % 2 == 0:
                    j += 1

                temp = j * i
                while temp <= num:
                    isprime[mapping(temp)] = 0
                    j += 2
                    temp = j * i

        for i in range(first_new, temp2, 2):
            if isprime[mapping(i)]:
                j = 3
                temp = j * i
                while temp <= num:
                    isprime[mapping(temp)] = 0
                    j += 2
                    temp = j * i

    return [2] + [x for x in isprime[:(num - 1)//2] if x]


def prime_factors(num):
    sqrt_num = math.floor(math.sqrt(num)) + 1
    for i in itertools.chain([2], range(3, sqrt_num, 2)):
        if num % i:
            continue

        while num % i == 0:
            num //= i
        yield i
    if num != 1:
        yield num


def num_distinct_prime_factors(num):
    """returns the num of distinct prime factors for num > 0"""
    return sum(1 for _ in prime_factors(num))


def product_of_prime_factors(num):
    ans = 1
    for i in prime_factors(num):
        ans *= i
    return ans


def is_circular_prime(num, length):
    for i in str(num):
        if not (int(i) % 2):
            return False
    for check in range(length):
        if not is_prime(numbers_ab.circular_shift(num, check + 1)):
            return False
    return True