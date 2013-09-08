import random
from timeit import Timer

def correctness(list_tests):
    print("Correctness Test")
    for i in list_tests:
        if i is False:
            return False
    print('Correct')
    print('-----------')
    return True

def timing(func, num_args, times = 100000):
    def test(func, a, b):
        nums = [random.randint(a, b) for i in range(num_args)]
        func(*nums)

    print("Timing Test")
    print(Timer(lambda: test(func, 1, 1000)).timeit(number = times))
    print(Timer(lambda: test(func, 100000, 1000000)).timeit(number = times))
    print('-----------')

def tests(f, list_tests, num_args):
    print(f.__name__)
    print('-----------')
    if correctness(list_tests) is True:
        timing(f, num_args)
