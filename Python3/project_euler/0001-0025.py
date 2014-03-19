__author__ = 'Aseem'

from lcm import lcm_of_range
from primes import largest_prime_factor, nth_prime, primes_list
from series import sum_numbers, sum_squares, sum_multiples_upto


def prob_0001():
    print(sum_multiples_upto((3, 5), 1000))


def aux_0002(num):
    #TODO Refactor
    """Returns the sum of even fibonacci numbers below num"""
    a, b = 1, 2
    total = 0
    while b < num:
        if b % 2 == 0:
            total += b
        a, b = b, a + b

    return total


def prob_0002():
    print(aux_0002(4000000))


def prob_0003():
    print(largest_prime_factor(600851475143))


def aux_0004():
    #TODO Refactor
    largest = 0
    for i in range(100, 1000):
        for j in range(i + 1, 1000):
            num = i * j
            if num > largest and num == int(str(num)[::-1]):
                    largest = num
    return largest


def prob_0004():
    print(aux_0004())


def prob_0005():
    print(lcm_of_range(1, 21))


def prob_0006():
    print(sum_numbers(100) ** 2 - sum_squares(100))


def prob_0007():
    print(nth_prime(10001))


def aux_0008():
    #TODO Refactor
    with open('Resources\\008.txt') as f:
        number = ''
        for line in f:
            number += line[:-1]

    largest = 0
    for i in range(995):
        product = 1
        for j in range(5):
            product *= int(number[i + j])
        if product > largest:
            largest = product
    return largest


def prob_0008():
    print(aux_0008())


def prob_0009():
    for c in range(1, 997):
        for b in range(1, c):
            a = 1000 - b - c
            if b > a > 0 and a*a + b*b == c*c:
                print(a * b * c)
                return


def prob_0010():
    print(sum(primes_list(2000000)))


if __name__ == "__main__":
    import sys
    RULER = "====="
    LIST_FUNC = [i for i in dir(sys.modules[__name__])
                 if i.startswith('prob_') is True]
    for fname in LIST_FUNC:
        print(fname + RULER, end="")
        locals()[fname]()