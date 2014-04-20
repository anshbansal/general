#!python3
from help_in_test import tests
import import_from_parent_dir

#The following line needs to be changed
import is_prime as cur_module
list_funcs = [x for x in dir(cur_module)
              if x.startswith('_') is False]

for i in list_funcs:
    f = getattr(cur_module, i)
    #The following tests need to be changed
    test1 = (f(1) == 0)
    test2 = (f(2) == 1)
    test3 = (f(3) == 1)
    test4 = (f(-1) == 0)
    test5 = (f(-2) == 0)
    test6 = (f(0) == 0)
    list_tests = [test1, test2, test3, test4,
                  test5, test6]

    #The number in following function call needs to be changed
    tests(f, list_tests, num_args = 1)
