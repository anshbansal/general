__author__ = 'Aseem'

import combinatorics
import files
import lcm
import primes
import series


RESOURCES = 'Resources'


def prob_0001():
    return series.sum_multiples_upto((3, 5), 1000)


def prob_0002():
    a, b, limit = 1, 2, 4000000
    total = a + sum(b for b in series.fibonacci(a, b, limit) if b % 2 == 0)
    return total


def prob_0003():
    return primes.largest_prime_factor(600851475143)


def prob_0004():
    #TODO Refactor
    largest = 0
    for i in range(100, 1000):
        for j in range(i + 1, 1000):
            num = i * j
            if num > largest and num == int(str(num)[::-1]):
                    largest = num
    return largest


def prob_0005():
    return lcm.lcm_of_range(1, 21)


def prob_0006():
    return series.sum_numbers(100) ** 2 - series.sum_squares(100)


def prob_0007():
    return primes.nth_prime(10001)


def prob_0008():
    #TODO Refactor
    number = ''
    for line in files.get_lines(RESOURCES, '008.txt'):
        number += line

    largest = 0
    for i in range(995):
        product = 1
        for j in range(5):
            product *= int(number[i + j])
        if product > largest:
            largest = product
    return largest


def prob_0009():
    for c in range(1, 997):
        for b in range(1, c):
            a = 1000 - b - c
            if b > a > 0 and a*a + b*b == c*c:
                return a * b * c


def prob_0010():
    return sum(primes.primes_list(2000000))


def prob_0013():
    total = sum(int(line)
                for line in files.get_lines(RESOURCES, '013.txt'))
    return str(total)[:10]


def prob_0015():
    return combinatorics.combinations(40, 20)


def prob_0016():
    #TODO Can be refactored into reusable
    num = str(2 ** 1000)
    return sum(int(i) for i in num)

if __name__ == "__main__":
    import sys
    RULER = "====="
    LIST_FUNC = [i for i in dir(sys.modules[__name__])
                 if i.startswith('prob_') is True]
    for fname in LIST_FUNC:
        print(fname + RULER, end="")
        print(locals()[fname]())