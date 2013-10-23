#!python3
from help_in_test import tests
import import_from_parent_dir

#The following line needs to be changed
import largest_prime_factor as cur_module
list_funcs = [x for x in dir(cur_module)
              if x.startswith('_') is False]


for i in list_funcs:
    f = getattr(cur_module, i)
    #The following tests need to be changed
    test1 = True
    list_tests = [test1]

    #The number in following function call needs to be changed
    tests(f, list_tests, num_args = 1)


    
