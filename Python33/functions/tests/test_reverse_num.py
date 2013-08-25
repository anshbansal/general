#!python3
from help_in_test import tests

import import_from_parent_dir
import_from_parent_dir.main()

#The following line needs to be changed
import reverse_num as cur_module
list_funcs = [x for x in dir(cur_module)
              if x.startswith('_') is False]

for i in list_funcs:
    f = getattr(cur_module, i)
    #The following tests need to be changed
    test1 = (f(-34) == -43)
    test2 = (f(34) == 43)
    test3 = (f(0) == 0)
    list_tests = [test1, test2, test3]

    #The number in following function call needs to be changed
    tests(f, list_tests, 1)
