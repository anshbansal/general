from random import randint
from timeit import Timer

def correctness(list_tests):
    print("Correctness Test")
    if not all(list_tests):
        return False
    print('Correct')
    print('-----------')
    return True

def timing(func, num_args):
    def test(func, a, b):
        nums = [randint(a, b) for i in range(num_args)]
        func(*nums)

    ranges = [(1, 100), (100, 10000), (10000, 1000000)]

    print("Timing Test")
    for i in ranges:
        timings = Timer(lambda: test(func, *i)).repeat(6, 10000)
        min_time = min(timings)
        print(min_time)
    print('-----------')

def tests(f, list_tests, num_args):
    print(f.__name__)
    print('-----------')
    if correctness(list_tests) is True:
        timing(f, num_args)
