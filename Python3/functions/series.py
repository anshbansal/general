__author__ = 'Aseem'

from functions import common


def _next_collatz(cur):
    if cur % 2:
        return 3 * cur + 1
    else:
        return cur // 2


@common.Memoize
def len_collatz(num):
    if num == 1:
        return 1
    else:
        return 1 + len_collatz(_next_collatz(num))


def fibonacci(a, b, limit=None):
    """Lazily generates Fibonacci numbers"""
    loop_indefinitely = limit is None
    while loop_indefinitely or b < limit:
        yield b
        a, b = b, a + b


def sum_numbers(num):
    return (num * (num + 1)) // 2


def sum_squares(num):
    return (num * (num + 1) * (2 * num + 1)) // 6


def sum_multiples_upto(multiples_of, limit):
    return sum(i for i in range(1, limit) if any(i % num == 0 for num in multiples_of))