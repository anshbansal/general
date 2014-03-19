from itertools import chain, count
import math


def num_distinct_prime_factors(num):
    """returns the num of distinct prime factors for num > 0"""
    ans = 0
    sqrt_num = math.floor(math.sqrt(num)) + 1
    for i in chain([2], range(3, sqrt_num, 2)):
        if not(num % i):
            ans += 1
            num //= i
        while not (num % i):
            num //= i
    return ans if num == 1 else ans + 1


def prob_047():
    nums = 0
    for i in count(1):
        if num_distinct_prime_factors(i) == 4:
            nums += 1
            if nums == 4:
                return i - 3
        else:
            nums = 0

if __name__ == "__main__":
    print(prob_047())


