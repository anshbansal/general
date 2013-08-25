#!python3
import random
from timeit import Timer
import import_from_parent_dir

def timing(f, times = 100000):
    def test1(f):
        f(random.randint(1, 1000),
          random.randint(1, 1000))
    def test2(f):
        f(random.randint(100000, 1000000),
          random.randint(100000, 1000000))

    print("Timing Test")
    print(Timer(lambda: test1(f)).timeit(number = times))
    print(Timer(lambda: test2(f)).timeit(number = times))
    print('-----------')

def tests(f):
    print(f.__name__)
    print('-----------')
    timing(f)


if __name__ == "__main__":
    import_from_parent_dir.main()
    import lcm as cur_module

    list_funcs = [x for x in dir(cur_module)
                  if x.startswith('_') is False]
    for i in list_funcs:
        tests(getattr(cur_module, i))
