import sys
from math import factorial
from itertools import islice
def p():
    numbers = int(next(sys.stdin))
    nums = [int(i) for i in islice(sys.stdin,numbers)]
    for i in nums:
        print(factorial(i))

p()
