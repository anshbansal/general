#!python3
import random
from timeit import Timer
from import_from_parent_dir import main

REPEAT = 100000

def correctness(f):
    test1 = (f(-34) != -43)
    test2 = (f(34) != 43)
    test3 = (f(0) != 0)
    
    print("Correctness Test")
    if test1 or test2 or test3:
        return False
    print('Correct')
    print('-----------')
    return True

def timing(f):
    def test1(f):
        f(random.randint(1, 1000))
    def test2(f):
        f(random.randint(100000, 1000000))

    print("Timing Test")
    print(Timer(lambda: test1(f)).timeit(number = REPEAT))
    print(Timer(lambda: test2(f)).timeit(number = REPEAT))
    print('-----------')

def tests(f):
    print(f.__name__)
    print('-----------')
    if correctness(f) is True:
        timing(f)

if __name__ == "__main__":
    main()
    from reverse_num import rev_num
    tests(rev_num)
