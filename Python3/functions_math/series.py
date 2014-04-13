__author__ = 'Aseem'


def collatz(num):
    """"Lazily generated collatz sequence"""
    def next_num(cur):
        if cur % 2:
            return 3 * cur + 1
        else:
            return cur // 2

    while num != 1:
        num = next_num(num)
        yield num


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