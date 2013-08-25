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

def timing(f, num_args, times = 100000):
    def test1(f):
        args = []
        for i in range(num_args):
            args.append(random.randint(1, 1000))
        f(*args)
    def test2(f):
        args = []
        for i in range(num_args):
            args.append(random.randint(100000, 1000000))
        f(*args)

    print("Timing Test")
    print(Timer(lambda: test1(f)).timeit(number = times))
    print(Timer(lambda: test2(f)).timeit(number = times))
    print('-----------')

def tests(f, list_tests, num_args):
    print(f.__name__)
    print('-----------')
    if correctness(list_tests) is True:
        timing(f, num_args)
