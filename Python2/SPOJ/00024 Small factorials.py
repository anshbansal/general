import math, sys
from itertools import islice
def p():
    numbers = int(next(sys.stdin))
    nums = [int(i) for i in islice(sys.stdin,numbers)]
    for i in nums:
        print math.factorial(i)

p()
